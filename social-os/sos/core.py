"""Regras determinísticas do Social OS.

Tudo que decide se algo pode ir a público mora aqui, em código testado, e não
só no prompt das rotinas. A rotina lê a linha do Notion, converte para o dict
abaixo e chama `checar_gate`. Se o gate disser não, nada é agendado.

Formato da linha (chaves = nomes das propriedades no Notion):
    {"ID": 12, "Status": "Aprovado", "Aprovado por": ["<user-id>"],
     "Risco": "Baixo", "Origem": "Corte de podcast", "Plataforma": "TikTok",
     "Legenda": "...", "Hook": "...", "Mídia": "https://...", "CTA": "comenta VENDAS"}
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, time
from pathlib import Path
from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl
from zoneinfo import ZoneInfo

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"

ORDEM_RISCO = {"Baixo": 0, "Alto": 1}


def carregar_config(path: Path | str = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _normalizar_ids(valor) -> list[str]:
    """Aceita lista de ids, 'user://<id>', JSON string ou None."""
    if not valor:
        return []
    if isinstance(valor, str):
        try:
            valor = json.loads(valor)
        except json.JSONDecodeError:
            valor = [valor]
    return [str(v).removeprefix("user://").strip() for v in valor if v]


# --------------------------------------------------------------------------
# Risco
# --------------------------------------------------------------------------

def risco_calculado(linha: dict, cfg: dict) -> tuple[str, list[str]]:
    """Risco mínimo que a linha merece, independente do que a IA declarou."""
    motivos = []
    origem = linha.get("Origem") or ""
    if origem not in cfg["risco"]["origens_baixo_risco"]:
        motivos.append(f"origem '{origem or 'vazia'}' exige aprovação do Rony")

    texto = " ".join(str(linha.get(k) or "") for k in ("Post", "Hook", "Legenda")).lower()
    # Palavra inteira: "lula" não pode casar com "celular".
    achados = [t for t in cfg["risco"]["termos_forcam_alto"]
               if re.search(rf"(?<!\w){re.escape(t)}(?!\w)", texto)]
    if achados:
        motivos.append("termos sensíveis: " + ", ".join(achados))

    return ("Alto" if motivos else "Baixo"), motivos


def risco_efetivo(linha: dict, cfg: dict) -> str:
    declarado = linha.get("Risco") or "Alto"  # vazio conta como Alto
    calculado, _ = risco_calculado(linha, cfg)
    return max(declarado, calculado, key=lambda r: ORDEM_RISCO.get(r, 1))


# --------------------------------------------------------------------------
# Gate de publicação
# --------------------------------------------------------------------------

@dataclass
class ResultadoGate:
    ok: bool
    motivos: list[str] = field(default_factory=list)
    risco: str = "Alto"
    aprovadores: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        if self.ok:
            return f"LIBERADO (risco {self.risco}, aprovado por {', '.join(self.aprovadores)})"
        return "BLOQUEADO: " + " | ".join(self.motivos)


def checar_gate(linha: dict, cfg: dict) -> ResultadoGate:
    motivos: list[str] = []
    risco = risco_efetivo(linha, cfg)

    if linha.get("Status") != "Aprovado":
        motivos.append(f"Status é '{linha.get('Status')}', precisa ser 'Aprovado'")

    ids = _normalizar_ids(linha.get("Aprovado por"))
    aprovadores_cfg = cfg["aprovadores"]
    nomes_validos = []
    if not ids:
        motivos.append("'Aprovado por' vazio: nenhum humano aprovou")
    for uid in ids:
        pessoa = aprovadores_cfg.get(uid)
        if not pessoa:
            motivos.append(f"usuário {uid} não está na lista de aprovadores")
        elif risco in pessoa["pode_aprovar"]:
            nomes_validos.append(pessoa["nome"])
    if ids and not nomes_validos:
        motivos.append(f"risco {risco}: nenhum aprovador com alçada (Alto = só Rony)")

    plat = linha.get("Plataforma")
    pcfg = cfg["plataformas"].get(plat)
    if not pcfg:
        motivos.append(f"plataforma desconhecida: {plat}")
    else:
        if pcfg["precisa_midia"] and not linha.get("Mídia"):
            motivos.append(f"{plat} exige arquivo em 'Mídia'")
        legenda = linha.get("Legenda") or ""
        if pcfg["limite_texto"] and len(legenda) > pcfg["limite_texto"]:
            motivos.append(f"legenda com {len(legenda)} caracteres, limite de {plat} é {pcfg['limite_texto']}")
        if pcfg["limite_texto"] and not legenda.strip():
            motivos.append("legenda vazia")

    texto = " ".join(str(linha.get(k) or "") for k in ("Hook", "Legenda"))
    for proibido in cfg["voz"]["proibido"]:
        if proibido in texto:
            motivos.append(f"contém '{proibido}' ({cfg['voz']['proibido_motivo']})")

    return ResultadoGate(ok=not motivos, motivos=motivos, risco=risco, aprovadores=nomes_validos)


# --------------------------------------------------------------------------
# UTM / atribuição
# --------------------------------------------------------------------------

def chave_utm(post_id: int | str, plataforma: str, cfg: dict) -> str:
    """Chave única de atribuição: sos-<id>-<sigla>. Ex.: sos-42-ig."""
    sigla = cfg["plataformas"][plataforma]["sigla"]
    num = str(post_id).upper().removeprefix("SOS-")
    return f"sos-{num}-{sigla}"


def link_utm(post_id, plataforma: str, cta: str, cfg: dict, destino: str | None = None) -> str | None:
    destino = destino or cfg["utm"]["destinos"].get(cta)
    if not destino:
        return None
    partes = urlsplit(destino)
    query = dict(parse_qsl(partes.query))
    query.update({
        "utm_source": cfg["plataformas"][plataforma]["utm_source"],
        "utm_medium": cfg["utm"]["medium"],
        "utm_campaign": chave_utm(post_id, plataforma, cfg),
    })
    return urlunsplit(partes._replace(query=urlencode(query)))


_RE_CHAVE = re.compile(r"sos-(\d+)-([a-z]+)", re.I)


def ler_chave(texto: str | None) -> tuple[int, str] | None:
    """Extrai (id, sigla) de qualquer string que contenha a chave UTM."""
    if not texto:
        return None
    m = _RE_CHAVE.search(texto)
    return (int(m.group(1)), m.group(2).lower()) if m else None


# --------------------------------------------------------------------------
# Horários
# --------------------------------------------------------------------------

def proximo_horario(plataforma: str, agora: datetime, ocupados: list[datetime], cfg: dict,
                    preferido: datetime | None = None, dias_busca: int = 14) -> datetime:
    """Primeiro horário livre da plataforma respeitando antecedência e teto diário.

    `ocupados`: datas/horas já agendadas NESTA plataforma (Metricool + fila).
    `preferido`: 'Data sugerida' da linha. É usado se estiver livre e no futuro.
    """
    tz = ZoneInfo(cfg["timezone"])
    agora = agora.astimezone(tz)
    minimo = agora + timedelta(minutes=cfg["horarios"]["antecedencia_minima_min"])
    teto = cfg["horarios"]["max_por_dia"].get(plataforma, 1)
    ocupados = [o.astimezone(tz) for o in ocupados]

    def livre(dt: datetime) -> bool:
        if dt < minimo:
            return False
        if any(abs((dt - o).total_seconds()) < 3600 for o in ocupados):
            return False
        return sum(1 for o in ocupados if o.date() == dt.date()) < teto

    if preferido is not None:
        preferido = preferido.astimezone(tz) if preferido.tzinfo else preferido.replace(tzinfo=tz)
        if livre(preferido):
            return preferido

    janelas = [time.fromisoformat(h) for h in cfg["horarios"]["janelas"][plataforma]]
    for d in range(dias_busca):
        dia = (agora + timedelta(days=d)).date()
        for h in janelas:
            dt = datetime.combine(dia, h, tzinfo=tz)
            if livre(dt):
                return dt
    raise RuntimeError(f"sem horário livre para {plataforma} nos próximos {dias_busca} dias")
