# Política de comunidade: o que a IA responde sozinha e o que nunca responde

Decisão do Rony (11/10/2026): **comentários simples saem automaticamente; DMs e leads sempre passam por um humano.**

## 1. Comentários: resposta automática permitida SÓ se TODAS forem verdade

- É comentário público num post do @rony publicado pelo Social OS ou já existente.
- Cai num destes tipos:
  - **Elogio/agradecimento** ("top", "que aula", emoji de palmas): responde curto, na voz, sem CTA.
  - **Palavra-gatilho do ManyChat** (`vendas`, `quero`, ou a palavra do e-mail daquele post): o ManyChat já manda a DM. A IA só responde "Te mandei no direct. Fui." quando o ManyChat **não** respondeu publicamente.
  - **Pergunta factual cuja resposta está no próprio post** ("qual o nome do livro?"): responde com o que está no post.
- Não menciona preço, desconto, Stone, política, religião, saúde, processo, concorrente, ex-sócio.
- Não é crítica, reclamação, ataque, ironia ou tema sensível.
- Máximo **30 respostas automáticas por dia** e **1 por pessoa por post**.
- Toda resposta automática é registrada no Log da linha do post na Fila.

Em dúvida, **não responde**: vira linha em Leads & Comunidade com `Status = Novo`.

## 2. Nunca automático (vira linha em Leads & Comunidade com resposta sugerida)

| Sinal | Intenção | Temperatura | Encaminhar para |
|---|---|---|---|
| "quanto custa", "valor", "preço", "como assino" | Pergunta de preço / Assinar MDD | Quente | Michel |
| "palestra", "evento", "convite", "keynote", nome de empresa + data | Palestra | Quente | DMT Palestras |
| "investimento", "pitch", "startup", "rodada", "deck" | Investimento Rebels | Morno | Rebels Ventures |
| "parceria", "publi", "collab", marca pedindo contato | Parceria/Marca | Morno | Rony |
| "jornalista", "matéria", "entrevista", veículo | Imprensa | Quente | Rony |
| assinante com problema (não recebeu e-mail, cobrança) | Suporte/Assinante | Morno | Suporte MDD |
| reclamação, crítica, polêmica, tema sensível | Outro | (avaliar) | Rony |

Toda DM é tratada como linha 2, mesmo que pareça elogio.

## 3. Formato da resposta sugerida

- Na voz do Rony (ler `skill/references/voz-e-estilo.md`), curta, sem prometer preço, data ou condição.
- Termina com o próximo passo concreto (link com UTM, e-mail do time, "vou pedir pro Michel te chamar").
- A IA **não envia**. Michel ou Rony copiam, ajustam e enviam, e mudam `Status` para Respondido.

## 4. Fontes de inbound

| Fonte | Como a rotina lê |
|---|---|
| Comentários IG @rony | Metricool inbox (quando a API expuser) ou Composio Instagram, conta @rony. **Pendente de conexão**, ver README. |
| Leads ManyChat (vendas/quero) | Planilha Google que o ManyChat alimenta (`config.json > comunidade.planilha_manychat_leads`), lida pelo Google Drive. |
| DMs e e-mails de convite | Gmail (rony@rebels.cc) com `palestra OR convite OR parceria newer_than:1d`. |

Se uma fonte não estiver conectada, a rotina registra "fonte X não lida" no relatório e **não inventa** dado.
