# Rotina 02: Publicador (de hora em hora, 7h às 22h)

Leia antes `rotinas/00-preambulo.md` e siga o setup.

**Objetivo:** levar ao Metricool tudo que um humano aprovou, e só isso. Depois, fechar o ciclo dos que já saíram.

## A. Agendar o que foi aprovado

1. Consulte a Fila (`config.json > notion.fila_aprovacao`) com `Status = Aprovado`. Nada? Pule para B.
2. Monte a lista de horários ocupados por plataforma: linhas da Fila com Status Agendado (campo `Data sugerida`) **mais** `GET /v2/scheduler/posts` do Metricool para os próximos 14 dias, se a credencial existir.
3. Para cada linha aprovada, escreva o JSON da linha e o JSON de ocupados daquela plataforma e rode:

   ```bash
   python3 -m sos agendar --linha linha.json --ocupados ocupados.json
   ```

   - **exit 0** (`agendado: true`): atualize a linha: `Status = Agendado`, `ID Metricool`, `Data sugerida` = `quando` devolvido, e acrescente ao `Log`: "AAAA-MM-DD HH:MM agendado no Metricool para <quando>, gate liberado (aprovado por <nomes>)". Se `Link UTM` estiver vazio, gere com `python3 -m sos utm`.
   - **exit 1** (gate bloqueou): **não tente contornar**. Se o motivo for alçada ("Alto = só Rony"), mude `Status` para **Aguardando aprovação** e escreva no Log "Michel aprovou mas o risco é Alto: precisa do Rony (<motivos>)". Qualquer outro motivo (mídia, limite, travessão): `Status = Ajustar` e o motivo no `Feedback`.
   - **exit 2** (erro de API): `Status = Erro`, mensagem no Log. Não tente de novo nesta rodada.
   - Credenciais do Metricool ausentes: não mude a linha; registre "Metricool sem credencial" no resumo.

## B. Fechar o ciclo do que já saiu

Para linhas com `Status = Agendado` e `Data sugerida` há mais de 30 minutos:

1. Consulte o post no Metricool (`GET /v2/scheduler/posts/{id}` via `sos.clients.Metricool`, ou a listagem por período). Se publicado, pegue o link público.
2. Atualize a linha: `Status = Publicado`, `Link publicado`.
3. Crie a linha correspondente em **Publicados** (`config.json > notion.publicados`) se ainda não existir: `Post`, `Plataforma` (mapeie Instagram Stories para "Stories"; X e Threads ainda não existem como opção em Publicados, então registre só na Fila), `Data`, `Link`, `Status = Publicado`, `Chave UTM` (`sos-<ID>-<sigla>`), `Fila Social OS` (relação), `Peça` (se houver), `Linha de conteúdo` conforme o CTA. Relacione de volta em `Publicação` na Fila.
4. Se a Peça em Produção tiver todas as linhas da Fila publicadas, mude `Etapa` da Peça para Publicado.

## C. Resumo (só se algo mudou)

Uma linha por item: agendado / bloqueado (motivo) / erro / publicado. Se nada mudou, responda só "sem mudanças".
