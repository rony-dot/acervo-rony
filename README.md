# Acervo Rony

Transcrições das entrevistas do Rony Meisler em podcasts, e o skill de Claude Code construído a partir delas.

**Estado atual:** 11 entrevistas · ~13,5 horas · ~154 mil palavras.

---

## O que tem aqui

| Pasta | O quê |
|---|---|
| `transcricoes/texto/` | As transcrições limpas, com timestamp a cada minuto. É o que se lê. |
| `transcricoes/raw/` | Legendas originais do YouTube (`.json3`, fora do git) + o conversor. |
| `skill/` | O skill `rony-meisler`. Symlinkado em `~/.claude/skills/`, então editar aqui atualiza o skill. |
| `novo-episodio.sh` | Pipeline de um comando para adicionar uma entrevista nova. |

---

## Adicionar uma entrevista nova

```bash
./novo-episodio.sh https://youtu.be/XXXXXXXX
```

Baixa a legenda automática em português, converte em texto limpo, numera e nomeia pelo canal. Aceita várias URLs de uma vez.

Depois, no Claude Code, dentro desta pasta:

> lê a transcrição nova e atualiza o skill

O fluxo completo de cada episódio novo é: **transcrever → ler → destilar no skill → commitar**.

### Se o vídeo não tiver legenda automática

O script avisa. Nesse caso é preciso Whisper (`yt-dlp -x --audio-format mp3` e transcrever o áudio), o que custa API — só vale para vídeos sem legenda.

---

## As entrevistas

| # | Podcast | Episódio | Duração | Publicado |
|---|---|---|---|---|
| 01 | Café com Ferri | Por que ele é um dos maiores nomes do Brasil? | 92 min | jul/2026 |
| 02 | Futurum Talks | #56 — As maiores lições de empreendedorismo | 70 min | jun/2026 |
| 03 | ROI Hunters | #349 — Criou uma marca de R$ 2 bi e largou tudo | 85 min | jun/2026 |
| 04 | TalksbyLeo | #238 — Depois da Reserva: a nova tese | 89 min | jun/2026 |
| 05 | Startups / MVP | A hora certa de começar e de sair de um negócio | 75 min | mai/2026 |
| 06 | Made in Brasil | #174 — Como criou e escalou a Reserva | 77 min | mai/2025 |
| 07 | Os Sócios | A virada de chave que fez criar a Reserva (corte) | 7 min | dez/2022 |
| 08 | Powercast | #248 — A verdade sobre vender uma empresa bilionária | 75 min | jun/2026 |
| 09 | Entusiasta | #084 — com Bernardo Britto | 81 min | jun/2026 |
| 10 | Marcas Rebeldes | #01 — Piloto, com João Branco | 65 min | jun/2025 |
| 11 | Excepcionais | Marcas bilionárias sem perder valores morais | 91 min | ago/2026 |

As URLs originais ficam em `transcricoes/raw/urls.txt`.

**Créditos.** As entrevistas pertencem aos canais que as produziram — Café com Ferri, Futurum Talks, ROI Hunters, TalksbyLeo, Startups/MVP, Made in Brasil, Os Sócios, Powercast, Entusiasta, Marcas Rebeldes e Excepcionais. Este acervo reúne transcrições geradas a partir das legendas automáticas dos vídeos públicos, para estudo e consulta. Assista aos episódios completos nos canais originais — os links estão em `urls.txt`.

---

## O skill

`skill/SKILL.md` + 12 arquivos em `skill/references/`:

`frameworks` · `marca-e-branding` · `vendas-e-varejo` · `financas-e-modelo` · `marca-pessoal-e-conteudo` · `ia-e-futuro` · `investimentos-e-negocios-atuais` · `venda-sucessao-e-socios` · `rotina-e-habitos` · `voz-e-estilo` · `trajetoria-e-numeros` · `opinioes-e-polemicas`

Aciona sozinho ao criar conteúdo no estilo dele, aplicar seus frameworks ou responder "o que o Rony pensa sobre X".

**Regra ao atualizar:** quando um número ou uma posição divergir entre entrevistas, a mais recente manda — e a divergência fica registrada em `trajetoria-e-numeros.md`. Opiniões datadas (cenário político, previsões) vão marcadas com o mês.

---

## Notas

- Transcrição vem de legenda automática do YouTube: boa para extrair conhecimento, imprecisa em nomes próprios e números falados. Confira antes de citar.
- Material de uso pessoal — as transcrições incluem falas dos entrevistadores.
