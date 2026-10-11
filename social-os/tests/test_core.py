import json
import subprocess
import sys
import unittest
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from sos.core import (carregar_config, checar_gate, risco_calculado, risco_efetivo,  # noqa: E402
                      chave_utm, link_utm, ler_chave, proximo_horario)
from sos.clients import Metricool  # noqa: E402

CFG = carregar_config()
RONY = "1a4d872b-594c-81b7-bd04-0002d9a65d9b"
MICHEL = "5ce0407b-de46-4936-a472-149eb6c189cb"
TZ = ZoneInfo("America/Sao_Paulo")


def linha(**kw):
    base = {"ID": 7, "Post": "Corte: caixa vs DRE", "Status": "Aprovado", "Aprovado por": [RONY],
            "Risco": "Baixo", "Origem": "Corte de podcast", "Plataforma": "TikTok",
            "Hook": "Varejo não quebra no resultado.", "Legenda": "Pensa comigo. Fui.",
            "Mídia": "https://cdn.exemplo.com/v.mp4", "CTA": "comenta VENDAS"}
    base.update(kw)
    return base


class Gate(unittest.TestCase):
    def test_aprovado_pelo_rony_passa(self):
        self.assertTrue(checar_gate(linha(), CFG).ok)

    def test_sem_aprovador_bloqueia(self):
        r = checar_gate(linha(**{"Aprovado por": []}), CFG)
        self.assertFalse(r.ok)
        self.assertIn("nenhum humano", " ".join(r.motivos))

    def test_status_diferente_bloqueia(self):
        for s in ("Aguardando aprovação", "Rascunho IA", "Ajustar", "Agendado", None):
            self.assertFalse(checar_gate(linha(Status=s), CFG).ok, s)

    def test_michel_aprova_baixo_risco(self):
        self.assertTrue(checar_gate(linha(**{"Aprovado por": [MICHEL]}), CFG).ok)

    def test_michel_nao_aprova_alto_risco(self):
        r = checar_gate(linha(**{"Aprovado por": [MICHEL], "Risco": "Alto"}), CFG)
        self.assertFalse(r.ok)

    def test_ia_nao_rebaixa_risco_por_origem(self):
        # Texto nativo declarado Baixo continua Alto, então Michel não basta.
        l = linha(**{"Aprovado por": [MICHEL], "Origem": "Texto nativo", "Risco": "Baixo"})
        self.assertEqual(risco_efetivo(l, CFG), "Alto")
        self.assertFalse(checar_gate(l, CFG).ok)

    def test_ia_nao_rebaixa_risco_por_termo(self):
        l = linha(**{"Aprovado por": [MICHEL], "Legenda": "Parceria com a Stone. Fui."})
        self.assertEqual(risco_calculado(l, CFG)[0], "Alto")
        self.assertFalse(checar_gate(l, CFG).ok)

    def test_risco_vazio_conta_como_alto(self):
        self.assertEqual(risco_efetivo(linha(Risco=None), CFG), "Alto")

    def test_usuario_desconhecido_bloqueia(self):
        self.assertFalse(checar_gate(linha(**{"Aprovado por": ["intruso"]}), CFG).ok)

    def test_aceita_formatos_de_id_do_notion(self):
        self.assertTrue(checar_gate(linha(**{"Aprovado por": json.dumps([f"user://{RONY}"])}), CFG).ok)

    def test_video_sem_midia_bloqueia(self):
        self.assertFalse(checar_gate(linha(**{"Mídia": None}), CFG).ok)

    def test_linkedin_texto_sem_midia_passa(self):
        self.assertTrue(checar_gate(linha(Plataforma="LinkedIn", **{"Mídia": None}), CFG).ok)

    def test_travessao_bloqueia(self):
        r = checar_gate(linha(Legenda="Pensa comigo — isso muda tudo."), CFG)
        self.assertFalse(r.ok)
        self.assertIn("travessão", " ".join(r.motivos))

    def test_limite_do_x(self):
        self.assertFalse(checar_gate(linha(Plataforma="X", Legenda="a" * 281, **{"Mídia": None}), CFG).ok)


class Utm(unittest.TestCase):
    def test_chave_e_link(self):
        self.assertEqual(chave_utm(42, "Instagram Reels", CFG), "sos-42-ig")
        self.assertEqual(chave_utm("SOS-42", "LinkedIn", CFG), "sos-42-li")
        url = link_utm(42, "LinkedIn", "comenta VENDAS", CFG)
        self.assertIn("utm_campaign=sos-42-li", url)
        self.assertIn("utm_source=linkedin", url)
        self.assertIn("utm_medium=social", url)

    def test_sem_destino(self):
        self.assertIsNone(link_utm(1, "X", "sem CTA", CFG))

    def test_ler_chave(self):
        self.assertEqual(ler_chave("foo sos-42-IG bar"), (42, "ig"))
        self.assertIsNone(ler_chave("orgânico"))


class Horarios(unittest.TestCase):
    agora = datetime(2026, 10, 12, 6, 0, tzinfo=TZ)  # segunda 6h

    def test_primeira_janela_apos_antecedencia(self):
        dt = proximo_horario("Instagram Reels", self.agora, [], CFG)
        self.assertEqual((dt.hour, dt.minute), (7, 30))

    def test_respeita_antecedencia(self):
        dt = proximo_horario("Instagram Reels", self.agora.replace(hour=7), [], CFG)
        self.assertEqual((dt.hour, dt.minute), (12, 15))

    def test_respeita_teto_diario(self):
        ocupados = [self.agora.replace(hour=8), self.agora.replace(hour=15)]  # LinkedIn: teto 1/dia
        dt = proximo_horario("LinkedIn", self.agora, ocupados, CFG)
        self.assertEqual(dt.date().day, 13)

    def test_preferido_livre_e_usado(self):
        pref = datetime(2026, 10, 14, 10, 0, tzinfo=TZ)
        self.assertEqual(proximo_horario("X", self.agora, [], CFG, preferido=pref), pref)

    def test_preferido_no_passado_e_ignorado(self):
        pref = datetime(2026, 10, 1, 10, 0, tzinfo=TZ)
        self.assertNotEqual(proximo_horario("X", self.agora, [], CFG, preferido=pref), pref)


class Payload(unittest.TestCase):
    def test_reels_e_shorts(self):
        q = datetime(2026, 10, 12, 19, 30, tzinfo=TZ)
        p = Metricool.montar_payload(linha(Plataforma="Instagram Reels"), q, "instagram", "America/Sao_Paulo", ["m"])
        self.assertEqual(p["publicationDate"], {"dateTime": "2026-10-12T19:30:00", "timezone": "America/Sao_Paulo"})
        self.assertEqual(p["instagramData"]["type"], "REEL")
        self.assertEqual(p["providers"], [{"network": "instagram"}])
        y = Metricool.montar_payload(linha(Plataforma="YouTube Shorts"), q, "youtube", "America/Sao_Paulo", ["m"])
        self.assertEqual(y["youtubeData"]["title"], "Varejo não quebra no resultado.")


class Cli(unittest.TestCase):
    def _rodar(self, *args):
        return subprocess.run([sys.executable, "-m", "sos", *args], cwd=RAIZ, capture_output=True, text=True)

    def test_agendar_bloqueado_nao_chama_api(self, ):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(linha(Status="Aguardando aprovação"), f)
        r = self._rodar("agendar", "--linha", f.name)
        self.assertEqual(r.returncode, 1)
        self.assertFalse(json.loads(r.stdout)["agendado"])

    def test_agendar_dry_run(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(linha(), f)
        r = self._rodar("agendar", "--linha", f.name, "--dry-run")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(json.loads(r.stdout)["dry_run"])


if __name__ == "__main__":
    unittest.main()
