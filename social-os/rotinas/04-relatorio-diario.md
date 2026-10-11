# Rotina 04: Relatório de 1 página (dias úteis, ~7h)

Leia antes `rotinas/00-preambulo.md` e siga o setup.

**Objetivo:** um e-mail que o Rony lê em 90 segundos no celular e que responde: *o conteúdo de ontem trouxe dinheiro? O que está esperando por mim?* Mede dinheiro, não curtida.

## 1. Coletar (janela: ontem 00:00 a 23:59; na segunda, sexta a domingo)

| Métrica | Fonte |
|---|---|
| Posts publicados (por plataforma) | Fila de Aprovação, Status Publicado, `Link publicado` |
| Views, engajamento, outlier (IG) | Sandcastles `channel_recap` canal `da2d77da-1d5d-472a-ac64-96af5e2e3caf`, 3 dias |
| Views e seguidores das outras redes | Windsor.ai conector `metricool` (se conectado) |
| Seguidores ganhos no período | Windsor `metricool` / Sandcastles `get_personal_analytics` |
| Cliques no link | Windsor `googleanalytics4` conta "Site Rony": sessões por `session_campaign` que comece com `sos-` |
| Assinantes MDD por post | `python3 -m sos atribuicao --desde <data> --publicacao MDD` (beehiiv; precisa de credencial) |
| Leads ManyChat por post | Planilha ManyChat (coluna chave_utm) |
| Leads e convites | Leads & Comunidade, criados no período |
| Fila | Fila de Aprovação: contagem por Status |

Fonte que falhar: escreva "n/d (motivo)" na célula. Nunca estime sem marcar "~".

## 2. Atribuir e gravar

Para cada post publicado nos últimos 7 dias, atualize em **Publicados**: `Views`, `Seguidores ganhos`, `Cliques no link`, `Assinantes MDD (UTM)`, `Leads ManyChat`, `Leads gerados` (Leads & Comunidade com aquele Post de origem). A chave que liga tudo é `Chave UTM` (`sos-<ID>-<sigla>`).

## 3. Escrever o e-mail (HTML mobile, max-width 600px, fonte do sistema)

Assunto: `📊 Social OS: <dia> <DD/MM>: <N> assinantes, <N> leads, <N> esperando você`

Blocos, nesta ordem, e nada além:

1. **Uma frase** que diz se ontem foi bom ou ruim e por quê (com número).
2. **Funil de ontem** (tabela de 1 linha por etapa): Posts → Views → Seguidores → Cliques → Assinantes MDD → Leads (palestra/parceria/investimento). Ao lado de cada número: variação vs. média dos 7 dias anteriores.
3. **O post que trouxe dinheiro**: o post com mais assinantes + leads (não o com mais views). Título, plataforma, números do funil dele, link, e 1 linha de por que funcionou. Se o de mais views for outro, cite-o em 1 linha mostrando a diferença.
4. **Esperando você** (com links diretos para o Notion):
   - N posts em Aguardando aprovação (link do Kanban "Aprovar"); destaque os de risco Alto, que só ele aprova, e os que vão sair nas próximas 24h.
   - Leads quentes (palestra, imprensa, parceria, investimento): quem, o quê, link.
5. **Alertas** (só se houver): posts em Erro, gates bloqueados, fontes não lidas, credenciais faltando.
6. **Uma decisão** que o sistema pede ao Rony hoje (ex.: "LinkedIn rende 4x mais clique que X: mover 2 posts de X para LinkedIn?").

## 4. Enviar

Envie com o Gmail `send_message` para `config.json > email_relatorio` (só para esse endereço, nunca para terceiros). Se o envio falhar, crie rascunho e diga no resumo.

## 5. Resumo

Uma linha: enviado/rascunho, e as fontes n/d.
