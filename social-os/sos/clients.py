"""Clientes HTTP mínimos (só stdlib) para Metricool e beehiiv.

Credenciais vêm de variáveis de ambiente (nomes em config.json). Nada de token
em arquivo do repositório.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime


class ErroAPI(RuntimeError):
    pass


def _http(metodo: str, url: str, headers: dict, corpo: dict | None = None, timeout: int = 30):
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(url, data=dados, method=metodo, headers={
        "Accept": "application/json", **({"Content-Type": "application/json"} if dados else {}), **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode() or "{}"
            return json.loads(txt)
    except urllib.error.HTTPError as e:
        raise ErroAPI(f"{metodo} {url.split('?')[0]} -> {e.code}: {e.read().decode()[:500]}") from None


def _env(nome: str) -> str:
    v = os.environ.get(nome)
    if not v:
        raise ErroAPI(f"variável de ambiente {nome} não definida (configure em Environment > secrets)")
    return v


# --------------------------------------------------------------------------
# Metricool
# --------------------------------------------------------------------------

# Campos específicos por rede. Validados contra a doc pública do scheduler
# (POST /v2/scheduler/posts). Se o Metricool recusar algum, o erro volta com a
# mensagem da API e a linha vai para Status=Erro com o texto no Log.
DADOS_POR_PLATAFORMA = {
    "Instagram Reels":     {"instagramData": {"type": "REEL"}},
    "Instagram Carrossel": {"instagramData": {"type": "POST"}},
    "Instagram Stories":   {"instagramData": {"type": "STORY"}},
    "YouTube Shorts":      {"youtubeData": {"type": "short", "privacy": "public"}},
    "TikTok":              {"tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE"}},
}


class Metricool:
    def __init__(self, cfg: dict):
        m = cfg["metricool"]
        self.base = m["base_url"].rstrip("/")
        self.token = _env(m["env_token"])
        self.params = {"userId": _env(m["env_user_id"]), "blogId": _env(m["env_blog_id"])}
        self.tz = cfg["timezone"]
        self.cfg = cfg

    def _url(self, caminho: str, **extra) -> str:
        return f"{self.base}{caminho}?{urllib.parse.urlencode({**self.params, **extra})}"

    def _h(self):
        return {"X-Mc-Auth": self.token}

    def perfis(self):
        return _http("GET", self._url("/admin/simpleProfiles"), self._h())

    def agendados(self, inicio: datetime, fim: datetime):
        url = self._url("/v2/scheduler/posts", start=inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                        end=fim.strftime("%Y-%m-%dT%H:%M:%S"), timezone=self.tz)
        return _http("GET", url, self._h())

    def normalizar_midia(self, url_midia: str) -> str:
        """Metricool exige mídia 'normalizada' (baixada para o CDN dele)."""
        url = f"{self.base}/actions/normalize/image/url?{urllib.parse.urlencode({'url': url_midia, **self.params})}"
        r = _http("GET", url, self._h())
        return r if isinstance(r, str) else r.get("url") or r.get("data") or url_midia

    @staticmethod
    def montar_payload(linha: dict, quando: datetime, rede: str, tz: str, midia: list[str]) -> dict:
        corpo = {
            "publicationDate": {"dateTime": quando.strftime("%Y-%m-%dT%H:%M:%S"), "timezone": tz},
            "text": linha.get("Legenda") or "",
            "providers": [{"network": rede}],
            "autoPublish": True,
            "draft": False,
        }
        if midia:
            corpo["media"] = midia
        corpo.update(DADOS_POR_PLATAFORMA.get(linha["Plataforma"], {}))
        if linha["Plataforma"] == "YouTube Shorts":
            corpo["youtubeData"]["title"] = (linha.get("Hook") or linha.get("Post") or "")[:100]
        return corpo

    def agendar(self, linha: dict, quando: datetime, dry_run: bool = False) -> dict:
        rede = self.cfg["plataformas"][linha["Plataforma"]]["metricool"]
        midia = [linha["Mídia"]] if linha.get("Mídia") else []
        if midia and not dry_run:
            midia = [self.normalizar_midia(m) for m in midia]
        corpo = self.montar_payload(linha, quando, rede, self.tz, midia)
        if dry_run:
            return {"dry_run": True, "payload": corpo}
        return _http("POST", self._url("/v2/scheduler/posts"), self._h(), corpo)


# --------------------------------------------------------------------------
# beehiiv
# --------------------------------------------------------------------------

class Beehiiv:
    BASE = "https://api.beehiiv.com/v2"

    def __init__(self, cfg: dict):
        b = cfg["beehiiv"]
        self.key = _env(b["env_api_key"])
        self.pubs = {nome: os.environ.get(var) for nome, var in b["env_publicacoes"].items()}

    def novos_assinantes(self, publicacao: str, desde: datetime, max_paginas: int = 20) -> list[dict]:
        """Assinantes criados desde `desde`, com campos UTM. Ordenado do mais novo."""
        pub = self.pubs.get(publicacao)
        if not pub:
            raise ErroAPI(f"publicação '{publicacao}' sem ID no ambiente")
        corte = int(desde.timestamp())
        saida, cursor = [], None
        for _ in range(max_paginas):
            q = {"limit": 100, "order_by": "created", "direction": "desc"}
            if cursor:
                q["cursor"] = cursor
            r = _http("GET", f"{self.BASE}/publications/{pub}/subscriptions?{urllib.parse.urlencode(q)}",
                      {"Authorization": f"Bearer {self.key}"})
            for s in r.get("data", []):
                if int(s.get("created", 0)) < corte:
                    return saida
                saida.append({k: s.get(k) for k in ("id", "created", "status", "utm_source",
                                                    "utm_medium", "utm_campaign", "referring_site")})
            cursor = r.get("next_cursor")
            if not r.get("has_more") or not cursor:
                break
        return saida
