# Social OS: o time de social media do Rony que roda sozinho, mas não publica sozinho

> A IA pesquisa, escreve, agenda, responde o simples e mede o dinheiro. **Nada vai a público sem um humano dizer sim.** A fronteira é uma decisão de arquitetura, não uma promessa de prompt: ela está em código testado (`sos/core.py`).

## Como funciona

```
 PESQUISA (já existia)          CONTEÚDO                 APROVAÇÃO (humano)        PUBLICAÇÃO                MEDIÇÃO
 ─────────────────────          ────────                 ──────────────────        ──────────                ───────
 Radar diário 6h30   ─┐
 Top 20 BIGVU sexta  ─┤  Rotina 01 (dom 16h)     Notion "📤 Fila de        Rotina 02 (de hora em     Rotina 04 (7h, dias úteis)
 Digest sábado       ─┼─► 1 peça → 8 saídas  ──►  Aprovação" (Kanban)  ──►  hora): gate em código ──►  post → seguidor → clique
 Sandcastles         ─┤   por plataforma         Rony aprova tudo          → Metricool agenda no     → assinante MDD → lead
 Transcrições podcast─┘   + UTM + risco          Michel aprova risco Baixo  horário ótimo             e-mail de 1 página
                                                                                    │
                                                 Rotina 03 (5x/dia): comentários simples respondidos na voz;
                                                 DMs, "quanto custa?", convites → "🎯 Leads & Comunidade"
```

| Módulo do blueprint | Onde está | Quem faz |
|---|---|---|
| 1. Pesquisa | Rotinas que já existiam (Radar, Top 20 BIGVU, Digest, Sandcastles) + brief em `rotinas/01` passo 2 | IA |
| 2. Conteúdo | `rotinas/01-conteudo-semanal.md` | IA rascunha, Michel produz mídia |
| Aprovação | Notion **📤 Fila de Aprovação** + `sos/core.py::checar_gate` | **Humano** |
| 3. Publicação | `rotinas/02-publicador.md` + `python3 -m sos agendar` + Metricool | IA, só depois do gate |
| 3. Comunidade | `rotinas/03-comunidade.md` + `marca/politica-comunidade.md` + ManyChat | IA no simples, humano no resto |
| Orquestração e relatório | `rotinas/04-relatorio-diario.md` | IA |

## O gate (a parte que não pode falhar)

`python3 -m sos agendar` só chama o Metricool se **tudo** for verdade (`sos/core.py`, 25 testes em `tests/`):

1. `Status = Aprovado` e `Aprovado por` preenchido por alguém da lista em `config.json > aprovadores`.
2. **Risco efetivo** = o maior entre o declarado e o calculado. A IA não consegue rebaixar:
   - Baixo só para `Corte de podcast` e `Repost/adaptação` sem termo sensível.
   - Alto para todo o resto, e sempre que aparecer Stone, preço, oferta, política, tragédia, investimento etc.
3. Risco Alto: só o Rony aprova. Michel aprova Baixo.
4. Mídia presente quando a plataforma exige, legenda dentro do limite, sem travessão.

E nas rotinas: a IA **nunca** escreve `Status = Aprovado` nem `Aprovado por`. Isso é humano.

> Limite honesto: o Notion não registra *quem* editou cada propriedade, então a lei 1 do preâmbulo é regra de processo, não trava técnica. A trava técnica é o gate em código: mesmo que um campo fosse preenchido indevidamente, só passa quem está na lista de aprovadores e com a alçada certa.

## Como o Rony usa (5 minutos por dia)

1. **7h**: lê o e-mail "📊 Social OS".
2. Abre a Fila no Notion, visão **Aprovar (Kanban)**. Para cada card em *Aguardando aprovação*:
   - **Aprovar**: preenche `Aprovado por` com o próprio nome e move para **Aprovado**. Em até 1h está agendado.
   - **Ajustar**: move para **Ajustar** e escreve em `Feedback` o que mudar. Volta revisado no domingo seguinte, ou antes se você pedir.
   - **Rejeitar**: move para **Rejeitado** (de preferência com 1 linha no Feedback: o sistema aprende).
3. Abre **🎯 Leads & Comunidade › Leads abertos** quando o e-mail apontar lead quente.

**Michel:** produz a mídia dos cards em *Rascunho IA* (briefing no corpo da página), cola o link em `Mídia` e move para *Aguardando aprovação*. Pode aprovar cards de risco **Baixo**. Responde os leads encaminhados para ele.

## Setup: o que falta ligar (checklist)

| # | Item | Quem | Como |
|---|---|---|---|
| 0 | **Ligar as rotinas** | Rony | Em claude.ai › Routines, abrir cada rotina "Social OS · 0X" (criadas **pausadas**), adicionar o repositório `rony-dot/acervo-rony` e os conectores Notion, Gmail, Google Drive, Sandcastles, Windsor.ai e Composio, e ativar. Sem isso elas rodam sem acesso ao Notion. |
| 1 | **Credenciais Metricool** | Rony | Metricool › Configurações › API: copiar *userToken*, *userId* e o *blogId* da marca. Adicionar no ambiente do Claude (menu do ambiente › Edit › secrets/variáveis) como `METRICOOL_USER_TOKEN`, `METRICOOL_USER_ID`, `METRICOOL_BLOG_ID`. Nunca colar no chat. Teste: `python3 -m sos teste-metricool`. |
| 2 | **Conectar as 6 redes no Metricool** | Rony/Michel | IG @rony, LinkedIn, TikTok, YouTube, X, Threads na mesma marca (blogId). |
| 3 | **Credenciais beehiiv** | Rony | `BEEHIIV_API_KEY`, `BEEHIIV_PUB_MDD`, `BEEHIIV_PUB_RONY` (as mesmas do `placar_negocio.py` do Mac). |
| 4 | **Windsor.ai › conectar Metricool** | Rony | Dá views e seguidores das redes além do IG para o relatório. Hoje o Windsor só tem GA4 "Site Rony" e IG @manualdedonos. |
| 5 | **ManyChat › planilha de leads** | Michel | Em cada fluxo de palavra-chave (VENDAS, QUERO, palavra do e-mail): ação *Google Sheets › Insert row* na planilha [Social OS · Leads ManyChat](https://docs.google.com/spreadsheets/d/1VbHuY3qOi5_KXqhUljyt_T6K9h_outB-i1tWtobFQow/edit) (já criada, pasta Conteúdos Social) com colunas `data, plataforma, handle, palavra, chave_utm, post_link`. O link enviado na DM deve ser o `Link UTM` do post. |
| 6 | **URLs de destino dos CTAs** | Rony | Confirmar/trocar as landing pages em `config.json > utm.destinos` (estão provisórias). |
| 7 | **Comentários do @rony** | Rony | Conectar o Instagram @rony no Composio (ou Windsor › instagram com a conta @rony) para a rotina 03 ler e responder comentários. Sem isso, ela só processa ManyChat e Gmail. |

Até os itens 1 e 2 estarem prontos, o sistema já funciona em **modo rascunho**: gera a semana, a fila, os leads e o relatório; o publicador só registra "Metricool sem credencial" e não mexe nas linhas.

## Rotinas agendadas (claude.ai › Routines)

| Rotina | Quando (Brasília) | Arquivo |
|---|---|---|
| Social OS · 01 Conteúdo da semana | domingo 16h | `rotinas/01-conteudo-semanal.md` |
| Social OS · 02 Publicador | de hora em hora, 7h às 22h | `rotinas/02-publicador.md` |
| Social OS · 03 Comunidade | 9h, 12h, 15h, 18h, 21h | `rotinas/03-comunidade.md` |
| Social OS · 04 Relatório diário | dias úteis, 6h53 | `rotinas/04-relatorio-diario.md` |

O prompt de cada rotina só manda ler o arquivo. **Para mudar o comportamento, edite o `.md` e faça commit**; não precisa mexer na rotina.

## Comandos

```bash
cd social-os
python3 -m unittest discover -s tests          # 25 testes
python3 -m sos risco  --linha linha.json       # risco mínimo calculado
python3 -m sos gate   --linha linha.json       # LIBERADO / BLOQUEADO
python3 -m sos utm --id 42 --plataforma "LinkedIn" --cta "comenta VENDAS"
python3 -m sos agendar --linha linha.json --ocupados ocupados.json --dry-run
python3 -m sos atribuicao --desde 2026-10-01 --publicacao MDD
python3 -m sos teste-metricool
```

## Próxima fase (depois de 2 semanas rodando)

- Integrar o relatório como bloco do Brief Matinal (decisão do Rony: separado primeiro, para testar).
- Trocar as janelas fixas de horário pelo *best time* do Metricool com 30 dias de dado próprio.
- Escalar para Manual de Donos e Rebels Ventures: nova marca = novo bloco em `config.json` e novo `blogId`; o resto é igual.
