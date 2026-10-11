# Rotina 01: Conteúdo da semana (domingo, 16h)

Leia antes `rotinas/00-preambulo.md` e siga o setup.

**Objetivo:** deixar na Fila de Aprovação a semana seguinte inteira (segunda a domingo), adaptada por plataforma, pronta para o Rony ou o Michel aprovarem na segunda de manhã.

## 1. Ler a voz e as regras

Leia, nesta ordem: `marca/voz-e-plataformas.md` e os arquivos que ele manda ler (voz-e-estilo.md; Prompt Mestre A3, A6 e A7; Acervo BIGVU Base de exclusão; Gabarito das Duas Séries se for o caso).

## 2. Montar o brief de pesquisa (o que já está funcionando)

Não refaça a pesquisa que as rotinas existentes já fazem: **consuma** o que elas deixaram no Notion.

- **Padrões — Hooks e Formatos**: os 10 com maior outlier médio e Confiança testada.
- **Formatos Trending**: score ≥ 65, não Saturando.
- **Pautas**: Status Aprovada, ainda sem Produção.
- **Roteiros BigVu Escolhidos Semanal**: a semana de gravação atual (Status A gravar / Gravado).
- **Produção**: peças com Etapa = Edição ou Agendado que ainda **não** têm linha na Fila (cheque a relação Peça).
- **Sandcastles**: `top_hooks` e `top_topics` da watchlist em 7 dias; `channel_recap` do @rony (canal `da2d77da-1d5d-472a-ac64-96af5e2e3caf`) em 14 dias para saber o que já saiu.
- **Fila de Aprovação**: linhas com Status = **Ajustar**. Leia o campo `Feedback` de cada uma: são prioridade número 1 (seção 4).

Salve um resumo em `saidas/brief-AAAA-MM-DD.md` (hooks vencedores lado a lado: frase literal dos 3 primeiros segundos + por que funcionou). Esse arquivo é o brief; tudo abaixo nasce dele.

## 3. Gerar a semana

**Mix alvo** (ajuste se o material da semana pedir, e diga por quê):

| Saída | Qtd/semana | Origem preferida |
|---|---|---|
| Vídeo curto (cada um vira 3 linhas: Instagram Reels, TikTok, YouTube Shorts) | 5 vídeos | Produção (já gravado) > Corte de podcast > Roteiro BIGVU |
| Instagram Carrossel | 2 | Pauta aprovada ou Padrão com prova |
| LinkedIn | 3 | Texto nativo a partir do vídeo da semana com melhor tese |
| X | 5 | Texto nativo / frase do Rony com fonte |
| Threads | 3 | Texto nativo |

**Cortes de podcast:** leia `../transcricoes/texto/`. Escolha trechos de 30 a 75s com uma tese inteira e um número concreto. Para cada corte, registre no corpo da página: arquivo, timestamp início e fim, transcrição literal do trecho, hook escrito na tela, e o link do episódio original. Cheque contra o Acervo BIGVU e o `channel_recap` para não repetir tema já publicado.

**Para cada linha criada na Fila** (`config.json > notion.fila_aprovacao`):

- `Post`: título editorial curto.
- `Plataforma`, `Formato`, `Origem`, `Hook`, `Legenda` (texto final, já adaptado à plataforma e dentro do limite), `CTA`, `Palavra-gatilho`.
- `Peça` (relação com Produção) quando existir.
- `Data sugerida`: um horário das janelas de `config.json > horarios` para aquela plataforma, distribuindo a semana sem passar do teto diário. O mesmo vídeo em IG, TikTok e Shorts **pode** sair no mesmo dia, em horários diferentes.
- `Risco`: rode `python3 -m sos risco --linha <json>` e use o `risco_minimo`. Escreva o motivo em `Motivo do risco`. Você pode subir o risco, nunca baixar.
- `Link UTM`: crie a linha primeiro, pegue o `ID` gerado e rode `python3 -m sos utm --id <ID> --plataforma "<P>" --cta "<CTA>"`. Atualize a linha com o link.
- `Status`:
  - **Aguardando aprovação** se a peça está completa (texto pronto e, quando a plataforma exige, `Mídia` preenchida).
  - **Rascunho IA** se falta mídia (corte a editar, carrossel a diagramar, vídeo a gravar). No corpo, escreva o **briefing de produção** para o Michel: o que editar, timestamps, texto de cada slide, B-roll. Quando o Michel subir a mídia, ele mesmo muda para Aguardando aprovação.
- **Corpo da página**, sempre: (a) a legenda/texto completo, (b) "Por que esta peça": qual padrão/hook/formato do brief inspirou e com qual número (outlier, views) e link, (c) "Fontes" de qualquer número citado, (d) o briefing de produção, se houver.

Crie em lotes de até 5 linhas por chamada.

## 4. Linhas em "Ajustar"

Para cada uma: leia o `Feedback`, reescreva o que foi pedido (só isso), anexe no `Log` "v2 AAAA-MM-DD: <o que mudou>" e volte para **Aguardando aprovação**. Se o feedback for "não gostei" sem direção, mude o ângulo e explique a mudança no Log.

## 5. Checagens antes de terminar

- Rode o gate em modo seco em todas as linhas que você deixou "Aguardando aprovação", **simulando** `Status=Aprovado` e `Aprovado por=[Rony]` só no JSON local (nunca no Notion): `python3 -m sos gate --linha <json>`. Qualquer motivo que não seja de aprovação (travessão, limite, mídia) você corrige agora.
- Nenhum tema repetido do Acervo BIGVU / últimos 60 dias.
- Os três CTAs de comment-gate copiados *verbatim* do Prompt Mestre A6.

## 6. Resumo final (curto)

Quantas linhas por plataforma, quantas aguardando aprovação vs. rascunho, o que o Michel precisa produzir (lista), os 3 hooks mais fortes da semana e de onde vieram, e qualquer fonte que falhou.
