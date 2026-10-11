"""CLI do Social OS. Rode de dentro de social-os/:  python3 -m sos <comando>

  risco      --linha L.json                   risco mínimo + motivos (usado pelo redator)
  utm        --id N --plataforma P --cta C    link com UTM de atribuição
  gate       --linha L.json                   LIBERADO/BLOQUEADO (exit 1 se bloqueado)
  agendar    --linha L.json [--ocupados O.json] [--dry-run]
                                              gate + horário + POST no Metricool
  atribuicao --desde AAAA-MM-DD               novos assinantes beehiiv por chave UTM
  teste-metricool                             valida credenciais (lista perfis)

Saída sempre em JSON numa linha (fácil para a rotina ler).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

from .core import (carregar_config, checar_gate, risco_calculado, link_utm,
                   chave_utm, ler_chave, proximo_horario)


def _ler(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _out(obj, code=0):
    print(json.dumps(obj, ensure_ascii=False, default=str))
    sys.exit(code)


def _dt(s, tz):
    if not s:
        return None
    d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=tz)


def main(argv=None):
    p = argparse.ArgumentParser(prog="sos")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nome in ("risco", "gate"):
        s = sub.add_parser(nome)
        s.add_argument("--linha", required=True)
    s = sub.add_parser("utm")
    s.add_argument("--id", required=True)
    s.add_argument("--plataforma", required=True)
    s.add_argument("--cta", required=True)
    s = sub.add_parser("agendar")
    s.add_argument("--linha", required=True)
    s.add_argument("--ocupados", help="JSON: lista de datetimes ISO já agendados nesta plataforma")
    s.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("atribuicao")
    s.add_argument("--desde", required=True)
    s.add_argument("--publicacao", default="MDD")
    sub.add_parser("teste-metricool")
    a = p.parse_args(argv)

    cfg = carregar_config()
    tz = ZoneInfo(cfg["timezone"])

    if a.cmd == "risco":
        risco, motivos = risco_calculado(_ler(a.linha), cfg)
        _out({"risco_minimo": risco, "motivos": motivos})

    if a.cmd == "utm":
        _out({"chave": chave_utm(a.id, a.plataforma, cfg),
              "link": link_utm(a.id, a.plataforma, a.cta, cfg)})

    if a.cmd == "gate":
        r = checar_gate(_ler(a.linha), cfg)
        _out({"ok": r.ok, "risco": r.risco, "aprovadores": r.aprovadores, "motivos": r.motivos},
             0 if r.ok else 1)

    if a.cmd == "agendar":
        linha = _ler(a.linha)
        r = checar_gate(linha, cfg)
        if not r.ok:  # trava dura: sem gate, sem chamada à API
            _out({"agendado": False, "motivos": r.motivos}, 1)
        ocupados = [_dt(x, tz) for x in (_ler(a.ocupados) if a.ocupados else [])]
        quando = proximo_horario(linha["Plataforma"], datetime.now(tz), ocupados, cfg,
                                 preferido=_dt(linha.get("Data sugerida"), tz))
        from .clients import Metricool, ErroAPI
        if a.dry_run:
            payload = Metricool.montar_payload(linha, quando, cfg["plataformas"][linha["Plataforma"]]["metricool"],
                                               cfg["timezone"], [linha["Mídia"]] if linha.get("Mídia") else [])
            _out({"agendado": False, "dry_run": True, "quando": quando.isoformat(), "payload": payload})
        try:
            resp = Metricool(cfg).agendar(linha, quando)
        except ErroAPI as e:
            _out({"agendado": False, "erro": str(e)}, 2)
        dados = resp.get("data", resp) if isinstance(resp, dict) else {}
        _out({"agendado": True, "quando": quando.isoformat(), "aprovado_por": r.aprovadores,
              "id_metricool": dados.get("id") or dados.get("uuid"), "resposta": dados})

    if a.cmd == "atribuicao":
        from .clients import Beehiiv
        desde = datetime.fromisoformat(a.desde).replace(tzinfo=tz)
        subs = Beehiiv(cfg).novos_assinantes(a.publicacao, desde)
        por_chave = Counter()
        for s in subs:
            k = ler_chave(s.get("utm_campaign"))
            por_chave[f"sos-{k[0]}-{k[1]}" if k else (s.get("utm_source") or "sem_utm")] += 1
        _out({"publicacao": a.publicacao, "desde": a.desde, "total": len(subs),
              "por_chave": dict(por_chave.most_common())})

    if a.cmd == "teste-metricool":
        from .clients import Metricool
        _out({"ok": True, "perfis": Metricool(cfg).perfis()})


if __name__ == "__main__":
    main()
