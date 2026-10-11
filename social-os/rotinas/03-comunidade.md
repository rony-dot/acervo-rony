# Rotina 03: Comunidade e leads (9h, 12h, 15h, 18h, 21h)

Leia antes `rotinas/00-preambulo.md` e siga o setup. Leia `marca/politica-comunidade.md` inteiro: ele define o que pode ser automático.

**Objetivo:** nenhum "quanto custa?" se perde. Comentários simples respondidos na voz; todo o resto vira lead com resposta sugerida para um humano enviar.

## 1. Coletar inbound desde a última rodada (janela = últimas 3h30)

- **ManyChat**: leia a planilha `config.json > comunidade.planilha_manychat_leads` pelo Google Drive. Cada linha nova = alguém disparou uma palavra-gatilho. Se o ID ainda for `PREENCHER_...`, registre "planilha ManyChat não configurada".
- **Comentários do @rony**: use a fonte conectada (ver tabela na política). Se nenhuma estiver conectada, registre "comentários não lidos: fonte não conectada" e siga.
- **Gmail** (rony@rebels.cc): `(palestra OR convite OR keynote OR parceria OR "media kit" OR imprensa OR entrevista) newer_than:1d -in:sent`. Só e-mails que citem rede social ou um post. O Brief Matinal já cuida do resto da caixa: não duplique.

## 2. Classificar cada item

Use a tabela da seção 2 da política. Antiduplicata: antes de criar, busque em Leads & Comunidade por `Handle` + `Mensagem` (mesmo texto nas últimas 72h = pula).

## 3. Agir

- **Comentário que passa em TODAS as condições da seção 1 da política**: responda pelo conector, na voz, curto. Registre no `Log` da linha do post na Fila: "resp auto @handle: <texto>". Respeite o teto de 30/dia (conte no Log de hoje).
- **Todo o resto**: crie linha em Leads & Comunidade com `Lead` (nome ou @), `Handle`, `Plataforma`, `Canal`, `Mensagem` (literal), `Intenção`, `Temperatura`, `Encaminhado para`, `Resposta sugerida` (seção 3 da política), `Link da conversa`, `Data`, `Post de origem` (relação com a Fila, pela chave UTM ou pelo link do post), `Status = Resposta sugerida`.
- **Leads ManyChat** (palavra-gatilho): o link já foi entregue pelo ManyChat. Crie a linha com `Intenção = Assinar MDD`, `Canal = ManyChat`, `Status = Respondido`, e relacione ao post pela `chave_utm` da planilha.

## 4. Alerta imediato

Se aparecer um lead **Quente** de Palestra, Imprensa ou Parceria, ou uma crise (reclamação com tração, acusação, tema sensível), envie **um e-mail** para `config.json > email_relatorio` com assunto "⚡ Social OS: <tipo> de <quem>", corpo de 5 linhas e link da linha no Notion. No máximo 3 alertas por dia; o resto espera o relatório das 7h.

## 5. Resumo

Contagens: respostas automáticas, leads criados por intenção, alertas enviados, fontes não lidas.
