# PRUMO: plano de construção da ferramenta para a "Arbitragem de IA para Negócios Locais"

> Base: o episódio *"The $1,000/hour 1-person AI business"* (Greg Isenberg com James Dickerson, "The Boring Marketer", publicado em 26/10/2026), a transcrição e os slides que você mandou, e três frentes de pesquisa feitas em 01/11/2026: engenharia reversa do Boring Marketer, stack e APIs, e mercado Brasil e EUA.
> Nome de trabalho: **Prumo**, o fio de prumo do pedreiro. É a ferramenta que mostra onde o funil do negócio local está torto.
> As fontes estão no fim. Rótulos usados no texto: **[C]** = confirmado em fonte primária, **[E]** = estimativa minha que precisa ser validada.

---

## 0. Resumo em uma página

**A tese, em uma linha.** Negócios locais de ticket alto já pagam caro por lead e perdem parte desses leads num funil quebrado. Você encontra os que valem a pena, mostra o vazamento em dinheiro, reconstrói a página e o funil na marca deles antes de pedir qualquer coisa, e cobra implantação mais mensalidade para medir e otimizar. A IA é a fábrica e não aparece no discurso de venda.

**O que ele realmente montou (engenharia reversa):**
- Ele **não** tem um "SaaS de agência". Tem três coisas:
  1. **Claude Code como sistema operacional**, com MCPs simples (Perplexity, Firecrawl, Playwright, Meta, GA, Maps).
  2. **Skills de copy e posicionamento** em formato de arquivo.
  3. **Uma biblioteca proprietária de funis reais validados**, o BoringFunnels: os funis entram por continuarem anunciando e por tirarem nota 11 ou 12 num checklist de 12 pontos. A biblioteca é exposta como MCP para o agente.
- Prospecção e pitch rodam como "MCPs que eu construí": achar, pontuar, achar o contato, montar o pitch e entregar, em cerca de 15 minutos por prospect.
- Ele monetiza em três camadas:
  - **Serviço:** implantação de US$2,5–5 mil mais mensalidade de cerca de US$1,5 mil.
  - **Ferramenta:** BoringFunnels Pro a US$299/ano.
  - **Comunidade e skills:** US$49/mês, e US$199 pelo pacote de skills.

**O que proponho:** construir o equivalente brasileiro com a mesma arquitetura "agent-first". O Prumo é ao mesmo tempo:
1. Um **app web** (painel do operador, proposta interativa para o prospect e relatório para o cliente).
2. Um **servidor MCP + skills** para operar tudo do Claude Code em linguagem natural, como "acha desentupidoras em Campinas que valham pitch".
3. Uma **fábrica de funis multi-tenant** que publica as páginas dos clientes.
4. Uma **camada de medição centrada em WhatsApp**.

**O que muda no Brasil.** O funil quebra no **WhatsApp**: 79% das empresas mandam o lead para o WhatsApp [Leadster], e 86% o usam como canal principal [RD Station]. A versão brasileira do vazamento "anúncio ≠ página" é: anúncio → página → botão de WhatsApp escondido → ninguém responde em 5 minutos → lead perdido, e nada disso é medido. O Prumo vende **"mais conversas que viram orçamento e mais orçamentos que viram serviço"**.

**Sequência recomendada (14 semanas até a v1):**

| Fase | Semanas | Objetivo |
|---|---|---|
| Fase 0, concierge | 1–2 | Operar manualmente com Claude Code e skills, fechar o primeiro case grátis |
| Fase 1 | 3–7 | Motor de prospecção e auditoria, e o gerador de pitch |
| Fase 2 | 8–11 | Fábrica de funis, fechamento e cobrança |
| Fase 3 | 12–14 | Medição de WhatsApp e ligação, e relatório de ROI |

Depois disso, a ferramenta vira produto vendável para outras agências (o caminho "BoringFunnels Pro").

---

## 1. Engenharia reversa: o serviço ponta a ponta narrado no podcast

### 1.1 A cadeia de valor, etapa por etapa

| # | Etapa | O que ele faz ou diz | Evidência |
|---|---|---|---|
| 1 | **Escolher nicho e cidade** | Ticket alto e urgente (US$2–20 mil): encanamento, HVAC, hood cleaning, implantes, árvores, sport courts, grama sintética, fossa, chaminé, calhas, crawl space, geradores, neve. "1 nicho, 1 cidade, 6 meses." | Episódio [C] |
| 2 | **Descobrir** | "Find me plumbers in Dallas worth pitching" → raspa Google Maps, Google e Yelp → 100 empresas em cerca de 1 min. Em outro vídeo: Apify ou Outscraper, conselhos estaduais de licença, associações do setor, bibliotecas de anúncios, revistas locais de luxo (quem compra página inteira) | Episódio e vídeo -JienW-k_1o [C] |
| 3 | **Qualificar** | Nº de reviews, **velocidade de reviews**, nº de técnicos, receita "encontrável", meta acima de US$2M/ano. Prompt mostrado: *"50+ reviews, nota ≥ 4,2, dono ainda opera, equipe de 2–20, anota site, se roda Google/Meta ads e sinais de crescimento; rankeie por fit; marque toda inferência como inferência."* | [C] |
| 4 | **Auditar** | "Meus MCPs passaram pelos anúncios e sites e acharam os vazamentos exatos." O agente audita **como se fosse um morador**: quanto tempo para achar o telefone e o agendamento, se existe oferta clara e um primeiro passo com preço, o que acontece depois do formulário. Nos encanadores de Dallas: 4 de 5 sem congruência anúncio-página, 3 de 5 sem a nota do Google, 4 de 5 obrigando a rolar 3 telas. Em Charlotte: 9 de 11 sem captura de email, 8 de 11 sem primeiro passo com preço, 9 de 11 com problemas no telefone, **0 com problema de tráfego** | [C] |
| 5 | **Montar o pitch** | Cerca de 15 min depois: "pitch na marca deles", e-mail do dono e proposta já no 1º e-mail. O funil é refeito na identidade do prospect e enviado como **link**, mais um vídeo pessoal (Loom). E-mail modelo: *"agendar uma inspeção me levou 4 toques… reconstruí a página em torno de inspeção grátis na sua marca… vale 15 minutos?"* Meta de cerca de 100 envios por dia | [C] |
| 6 | **Aquisição de relacionamento** | Dream 100 (Chet Holmes), preeminência (Jay Abraham), message-to-market (Dan Kennedy, com voz do cliente tirada do Reddit local), **lumpy mail** (conexão de latão + carta "você conserta vazamentos, eu conserto os do seu marketing"), café da manhã e meetups locais, Meta ads por raio. Marca da agência conectada ao nicho ("Leak Proof"), nada de estética Stripe | [C] |
| 7 | **Fechar** | Conta de ROI: US$13 mil/mês → 100 leads a US$129 → 20% de vazamento = **US$2.600/mês desperdiçados**. Um serviço de US$1.714 paga o trabalho. Implantação + mensalidade; performance depois; **1º trabalho grátis em troca de depoimento em vídeo** | [C] |
| 8 | **Construir o funil** | Um funil por campanha. Busca "new furnace installation" vai para o **quiz reparar ou substituir**; "quick service" vai para o **tune-up de US$79**. Os 5 arquétipos: free check, tripwire US$79–99 (que "paga os anúncios"), instant price (com upload de fotos e orçamento por IA), quiz e VSL do dono. Também advertorial e follow-up por SMS, e-mail e retargeting | [C] |
| 9 | **Medir e otimizar** | Mensalidade para "testar, analisar dados de chamadas, otimizar". Relatório por Loom e "todos os dados a um prompt de distância". Voz por IA **não** (clientes desligavam) | [C] |

### 1.2 O que ele realmente tem por baixo (stack)

| Camada | O que usa | Evidência |
|---|---|---|
| Ambiente | Claude Code (Opus, plano Max), Codex e Cursor como alternativas | [C] masterclass fev/2026 |
| MCPs | Perplexity (pesquisa), Firecrawl e Playwright (concorrência e auditoria), Meta Ads MCP, Google Analytics MCP (feito por ele), Zapier MCP, Google Maps Grounding MCP (Gemini). Recomendação dele: "manter o stack de MCP simples" | [C] |
| Skills | positioning-angles, direct-response-copy, lead-magnet, orchestrator, keyword research, DTC ads, front-end-design da Anthropic. O pacote de 17 skills custa US$199 | [C] |
| Biblioteca | **BoringFunnels**: funis reais, do anúncio ao último e-mail, com o "movimento" de cada etapa. Curadoria por anúncios que continuam rodando e checklist de 12 pontos. Botão "Copy for your agent". Kit com 4 entradas: build, improve one page, audit, rewrite copy. Pro: biblioteca e skills via MCP, US$299/ano | [C] |
| Demais | Apify (Maps), DataForSEO + Firecrawl + Perplexity (keyword tool), Meta Marketing API + CAPI (skill no GitHub), Remotion (anúncios em vídeo), Vercel, GitHub | [C] |
| Não encontrado | Fonte da estimativa de receita e funcionários; GoHighLevel; CallRail; Ads Transparency. Provavelmente ficam dentro do MCP privado | [E] |

**Lição de arquitetura.** O ativo defensável dele **não é o código**, é **a biblioteca curada de funis vencedores mais o checklist de 12 pontos**, empacotados para agentes. O Prumo precisa nascer com o mesmo DNA: uma **Biblioteca Prumo de funis brasileiros validados** como fosso.

### 1.3 Checagem dos números do podcast

| Número | Situação |
|---|---|
| CPL de US$129 em encanamento | **Confirmado** (LocaliQ 2025: encanamento US$129,02, HVAC US$127,74–129,02, conversão de 7,6%) |
| 112 mil empresas | Plausível só como estabelecimentos com funcionários. O IBISWorld soma cerca de 245 mil |
| "14% com IA integrada" | Sem fonte. A ServiceTitan diz 25% em uso |
| Ticket de US$1.714 | Ilustrativo. O reparo médio de HVAC é cerca de US$1.205 (Housecall Pro) |

→ No Prumo, **todo número de pitch sai de dados do próprio prospect ou de benchmark com fonte**, nunca do podcast.

---

## 2. Adaptação ao Brasil: decisões de produto

1. **O WhatsApp é a landing page de verdade.** A auditoria de 12 pontos ganha um bloco de WhatsApp:
   - botão na 1ª dobra;
   - mensagem pré-preenchida com contexto;
   - **tempo de 1ª resposta**, medido por "cliente oculto" automatizado;
   - horário de atendimento;
   - follow-up depois de 24h.
2. **Ranking de nichos para começar** [E, a validar com dados de CNPJ e do Planejador de Palavras-chave]:
   1. **Ar-condicionado com PMOC.** É o análogo direto do HVAC: urgência no verão, contrato recorrente obrigatório pela Lei 13.589/18.
   2. **Implantes e protocolo.** Ticket de R$2,5–40 mil, mas com mais agências concorrentes e as regras do CFO.
   3. **Planejados e marcenaria.** São 245 mil CNPJs, ticket de R$15–80 mil.
   4. **Desentupidora, limpa-fossa e dedetização.** Urgência e contratos; ticket menor, volume maior. Dedetização tem 33,8 mil empresas.
   5. **Diesel, guincho e mecânica pesada.** Mesmo nicho da Diesel Dudes.
   6. Energia solar: dor alta, mas o mercado encolheu 29% em 2025 e o caixa está curto.
   - Evitar: autoescola (risco regulatório) e advocacia (Provimento 205/2021 da OAB).
3. **Porte pelo CNPJ.** O critério "acima de US$2M" vira:
   - regime "Demais" ou EPP no teto;
   - mais de 3 anos de CNPJ;
   - nº de filiais;
   - capital social;
   - velocidade de reviews nos últimos 90 dias;
   - anúncios ativos no Google ou no Meta;
   - opcionalmente, faturamento presumido da Speedio.
4. **"Lumpy mail" brasileiro.** A sequência:
   - (a) e-mail com link da página refeita;
   - (b) vídeo de 60–90 s mostrando o anúncio dele, a página dele e o WhatsApp sem resposta;
   - (c) **visita presencial** com um objeto do nicho (manômetro brandeado para ar-condicionado, peça de PVC para desentupidora) e a auditoria impressa, com o anúncio circulado e um QR "fale comigo no WhatsApp";
   - (d) Dream 100 em associações locais (ACI, CDL, BNI, ABRAVA) e feiras (Febrava).
5. **WhatsApp frio é proibido** pela política da Meta, e API não oficial dá ban. O WhatsApp só entra **depois do opt-in** (QR da carta, resposta ao e-mail, contato no evento).
6. **Moeda e preço.** As mensalidades no Brasil ficam entre R$1,5 e 5 mil, então o modelo precisa de **volume com custo marginal mínimo** ou de **componente por performance**. É exatamente aí que a ferramenta se paga.

---

## 3. O produto: módulos do Prumo, da escolha ao produto final

Cada módulo corresponde a uma etapa da seção 1.1. Cada um tem uma tela no app, uma ferramenta no MCP e um job assíncrono.

### M1 · Radar (escolher nicho e cidade)
- **Entrada:** cidade, raio e lista de nichos candidatos.
- **Processo:**
  - nº de CNPJs ativos por CNAE no município (base aberta da Receita / Casa dos Dados);
  - nº de anunciantes no Google para 5–10 termos do nicho na cidade (SerpApi/DataForSEO na SERP e no Transparency Center);
  - CPC e volume de busca (Keyword Planner / DataForSEO);
  - ticket médio (tabela interna com fonte).
- **Saída:** **Score de Oportunidade** = densidade de anunciantes × ticket × urgência × (1 − sofisticação média das páginas, a partir de uma amostra de 10 auditorias).
- **Decisão:** escolher 1 nicho e 1 cidade. O sistema **trava o foco** e desencoraja abrir um segundo mercado antes de 6 meses ou de 10 clientes.

### M2 · Garimpo (descobrir e enriquecer)
- **Fontes:**
  - Google Maps via Outscraper (US$3/1k empresas, com reviews datados);
  - Places API (New) como alternativa "oficial";
  - CNPJ (Casa dos Dados, BrasilAPI) cruzado por nome, telefone e endereço: razão social, porte, data de abertura, CNAE, **QSA (nome do sócio-administrador)**;
  - site;
  - Instagram;
  - Doctoralia no caso de saúde.
- **Contato do decisor:** nome do sócio (QSA) + e-mail do domínio (Outscraper Emails/Hunter) + telefone comercial. Sempre marcar a **fonte de cada dado** (exigência da LGPD e regra do próprio James: "marque toda inferência").
- **Fit Score (0–100):**

| Peso | Critério |
|---|---|
| 25 | Porte (CNPJ) |
| 20 | Volume e nota de reviews (≥ 50, ≥ 4,2) |
| 15 | **Velocidade de reviews em 90 dias** |
| 20 | Anuncia no Google ou Meta (sinal de verba) |
| 10 | Dono ainda opera |
| 10 | Sinais de crescimento (vagas, filial nova) |

- **Saída:** lista ordenada → topo vira o **Dream 100** daquele mercado.

### M3 · Raio-X (auditoria de vazamentos)
- **Captura:**
  - anúncios ativos (texto e criativo, via SerpApi Transparency, DataForSEO e Meta Ad Library pela interface);
  - **a página de destino real de cada anúncio**, não a home;
  - screenshots mobile e desktop com Playwright;
  - Firecrawl `branding` (logo, cores, fontes);
  - PageSpeed.
- **Cliente oculto automatizado** (opcional e com cuidado): clica no WhatsApp e mede se há resposta e em quanto tempo. Usar um número próprio e uma mensagem neutra de orçamento; registrar só o tempo. *Avaliar com advogado; na dúvida, fazer manual na fase 0.*
- **Checklist Prumo de 12+4 pontos.** Claude com visão sobre screenshots e HTML devolve, para cada ponto, nota 0–2, evidência (recorte da tela) e correção sugerida:

| # | Ponto |
|---|---|
| 1 | A promessa do anúncio se repete no título da página (congruência) |
| 2 | Nota e nº de reviews do Google na 1ª dobra |
| 3 | CTA (ligar ou WhatsApp) visível sem rolar no celular |
| 4 | Oferta clara de primeiro passo (avaliação grátis, visita, check) |
| 5 | Primeiro passo com preço (tripwire) |
| 6 | Página específica por serviço ou campanha, não a home |
| 7 | Prova local (bairros atendidos, fotos reais da equipe) |
| 8 | Garantia ou reversão de risco |
| 9 | Velocidade mobile (LCP) |
| 10 | Leitura simples (5ª–7ª série: 11,1% vs 5,3% de conversão, segundo ele) |
| 11 | Captura de contato para follow-up |
| 12 | O que acontece depois do clique (confirmação, próximo passo) |
| W1 | WhatsApp na 1ª dobra |
| W2 | Mensagem pré-preenchida |
| W3 | Tempo de resposta |
| W4 | Horário e plantão visíveis |

- **Conta do dinheiro na mesa (R$/mês):**
  1. gasto estimado = nº de anúncios × CPC × volume (faixa);
  2. leads estimados = gasto ÷ CPL do nicho;
  3. vazamento = leads × (taxa benchmark − taxa estimada pela nota da auditoria);
  4. serviços perdidos = vazamento × taxa de fechamento × ticket.

  Sempre apresentada como **faixa com premissas abertas**. Nunca prometer número exato.

### M4 · Pitch Engine (proposta e página refeita na marca dele)
Isto reproduz os "15 minutos" do James. Gera automaticamente:
1. **Página refeita na marca do prospect**: template Prumo + tokens de marca do Firecrawl + copy de resposta direta, escolhendo um dos 5 arquétipos de funil pela intenção do anúncio dele. Publicada em `nome-do-prospect.prumo.page` com **noindex**, marca d'água "rascunho" e sem coleta de dados reais.
2. **Mini-relatório Raio-X** (1 página): 3 vazamentos com prints, a conta em R$ e o "antes e depois".
3. **Roteiro do vídeo de 60–90 s** para você gravar (ou Loom guiado com a tela da auditoria).
4. **E-mail 1 + follow-ups** no tom "morador que tentou contratar": *"Fui pedir orçamento de ar-condicionado pelo seu anúncio. Levei 4 toques pra achar o WhatsApp…"*
5. **Carta física + objeto sugerido + QR** para a visita ou envio.
6. **Proposta interativa** (página): calculadora de ROI com sliders que o dono ajusta (gasto, ticket, taxa de fechamento), escopo, preços e botão "quero começar" → M6.

Modelos: Sonnet para auditoria e copy em lote (Batch API, -50%), Opus só para o pitch final dos top 20, Haiku para classificação e limpeza. **[C] preços da API em seção 7.**

### M5 · Cadência (Dream 100 e relacionamento)
- CRM enxuto próprio (Postgres) com estágios: Garimpado → Auditado → Pitch pronto → Contatado → Conversou → Proposta → Cliente / Nutrir.
- **Cadência de 6 meses por conta (preeminência):**

| Semana | Toque |
|---|---|
| 0 | E-mail com página e vídeo |
| 1 | Visita ou carta com objeto |
| 2 | Ligação |
| Mensal | "Raio-X do mês": nova análise grátis dos anúncios, do concorrente e de uma tendência do bairro |
| Trimestral | Convite para café ou evento local |

- E-mail via Instantly ou Smartlead com **domínios secundários aquecidos**, SPF, DKIM e DMARC, opt-out em 1 clique e no máximo cerca de 30–50 envios por caixa por dia.
- WhatsApp oficial (Cloud API via BSP) **só para quem deu opt-in**.
- Tarefas do dia geradas pelo agente: "visitar 5 em Barão Geraldo hoje, levar 5 kits".

### M6 · Fechamento (contrato e cobrança)
- Proposta aceita → contrato gerado de um modelo + **ZapSign API** (assinatura e webhook) → **Asaas**: cobrança da implantação (Pix ou cartão) + **mensalidade por Pix Automático** + NFS-e automática.
- Se escolher performance: cláusula de "lead qualificado" e "agendamento" ligada às métricas do M8.
- Onboarding automático depois do pagamento:
  - formulário com acessos (Google Ads, Meta BM, GBP, domínio, WhatsApp Business), fotos, ofertas e preços;
  - agendamento da gravação do VSL do dono;
  - criação do workspace do cliente.
- **Modo "Case Zero":** um contrato de R$0 de implantação em troca de depoimento em vídeo e permissão de uso dos números, com um checklist de captação do depoimento.

### M7 · Fábrica de funis (o produto final entregue)
- **Biblioteca Prumo**: 5 arquétipos × variações por nicho. Cada template é um componente Next.js/Astro alimentado por JSON (copy, oferta, tokens de marca, provas):

| Arquétipo | Versão Brasil (exemplo: ar-condicionado) |
|---|---|
| Free check | "Check-up grátis do seu split: descubra se está gastando luz à toa" |
| Tripwire | "Higienização completa por R$149" (paga o anúncio e abre a porta para o PMOC) |
| Cotação instantânea | Quiz de BTUs/ambientes → faixa de preço na hora; upload de foto do local → orçamento estimado por IA |
| Quiz "consertar ou trocar" | Idade do aparelho, tipo de defeito, conta de luz → recomendação + agendamento |
| VSL do dono | "Antes de trocar seu ar-condicionado, assista isso" (roteiro gerado, gravação no celular do dono) |

- **Um funil por grupo de anúncios.** O sistema sugere o mapeamento palavra-chave → funil a partir dos termos de pesquisa do cliente.
- **Toda CTA leva a WhatsApp com mensagem pré-preenchida e ID de sessão**, ou a click-to-call com número rastreável, mais um formulário de fallback.
- **Follow-up:** sequência por WhatsApp (utility/marketing, com opt-in coletado no próprio funil) e e-mail para quem não agendou; lembrete de agendamento; pedido de review no Google depois do serviço (o que alimenta a "velocidade de reviews" e fecha o ciclo).
- **Hospedagem:** multi-tenant em Vercel ou **Cloudflare for SaaS** (100 domínios grátis, depois US$0,10/domínio/mês), com o domínio do cliente via CNAME e SSL automático.
- **Anúncios:** criação e ajuste das campanhas via Google Ads API e Meta Marketing API, sempre em rascunho ou pausado, com aprovação humana (mesmo padrão da meta-ads-skill dele).

### M8 · Medição (ligação, WhatsApp e formulário até a venda)
- **WhatsApp:**
  - links wa.me com código curto na mensagem ("Olá! Quero meu check-up [#K7Q2]") ligados a sessão, UTM e gclid;
  - para Click-to-WhatsApp do Meta: `ctwa_clid` + Conversions API (business_messaging);
  - integração com a Cloud API ou o CRM do cliente para registrar conversa iniciada → orçamento → fechado.
- **Ligações:** números de encaminhamento do Google Ads (grátis, disponível no Brasil) e, no site, **DNI próprio** com pool de números Twilio BR (US$4,25 por número/mês) ou fornecedor nacional. Gravação e transcrição com aviso → Claude classifica (lead real, spam, cliente antigo; agendou ou não).
- **Conversões offline:** subir "orçamento" e "venda" para o Google via **Data Manager API** (obrigatória desde 15/06/2026 para upload offline) e para o Meta via CAPI. **Isso é o que faz o Google otimizar para venda, e é o argumento mais forte da mensalidade.**
- **Fechamento informado pelo cliente:** botão no WhatsApp do dono ("✅ fechou R$___") ou planilha ou CRM simples, porque sem venda informada não há ROI.

### M9 · Painel e relatório de ROI (prova mensal)
- Painel do cliente:
  - gasto;
  - conversas, ligações e formulários;
  - custo por conversa;
  - orçamentos;
  - vendas;
  - **ROI**;
  - antes e depois desde a implantação.
- **Relatório mensal automático**: página + PDF + roteiro de vídeo de 3 min, com o que testamos, o que ganhou e o próximo teste.
- **Motor de testes:** A/B de headline, oferta e CTA nos funis (split na borda) e alertas ("tempo de resposta no WhatsApp subiu para 47 min na terça").
- "Pergunte aos seus dados": chat sobre os números do cliente (a versão do "all the data one prompt away" do James).

---

## 4. Arquitetura técnica

```
                ┌───────────────────────── Operador (você) ─────────────────────────┐
                │  Claude Code + Skills Prumo  ◄──MCP──►  Prumo MCP Server           │
                │  App Web (Next.js): Radar · Garimpo · Raio-X · Pitch · CRM · Painel│
                └───────────────┬───────────────────────────────────┬───────────────┘
                                │ API interna (tRPC/REST)           │
        ┌───────────────────────▼──────────┐          ┌─────────────▼─────────────┐
        │ Supabase (Postgres + Auth +      │          │ Jobs (Trigger.dev/Inngest) │
        │ Storage + RLS multi-tenant)      │◄────────►│ filas: garimpo, auditoria, │
        └───────────────────────▲──────────┘          │ pitch, publish, relatórios │
                                │                     └──┬───────┬────────┬───────┘
     ┌──────────────────────────┴───────┐               │       │        │
     │ Funis publicados (Astro/Next)    │   Workers Playwright  Claude API  Integrações:
     │ Cloudflare for SaaS / Vercel     │   (screenshots,       (Batch,     Outscraper, Casa dos Dados,
     │ + edge A/B + tracking script     │    cliente oculto)    visão)      SerpApi/DataForSEO, Firecrawl,
     └──────────────────────────────────┘                                  PageSpeed, ZapSign, Asaas,
                                                                           WhatsApp Cloud (BSP), Twilio,
                                                                           Google Ads/Data Manager, Meta
```

**Escolhas e por quê:**
- **Next.js + Supabase + Trigger.dev**: é o stack de vibe coder mais rápido, com RLS por cliente desde o primeiro dia.
- **Astro** para as páginas de funil: estáticas, rápidas (LCP conta na auditoria) e baratas.
- **MCP Server próprio** (TypeScript), com ferramentas `radar_mercado`, `garimpar`, `auditar`, `gerar_pitch`, `publicar_funil`, `relatorio_cliente`, `buscar_biblioteca`. Assim você opera como o James: em linguagem natural, com o Claude orquestrando, e o app web serve para revisar, aprovar e mostrar ao cliente.
- **Skills Prumo** (arquivos): `copy-resposta-direta-ptbr`, `auditoria-12+4`, `pitch-morador`, `oferta-tripwire`, `roteiro-vsl-dono`, `relatorio-roi`. Escritas e versionadas no repo.
- **Humano no circuito** em tudo que sai para fora (e-mail, publicação, anúncio, cobrança): o agente prepara e você aprova em lote.

**Modelo de dados (núcleo):**
- `mercado` (nicho, cidade, score)
- `empresa` (CNPJ, Maps place_id, site, porte, fit_score, fontes)
- `pessoa` (sócio ou decisor, base legal, opt-out)
- `anuncio`
- `pagina`
- `auditoria` (itens, evidências, dinheiro_na_mesa)
- `pitch` (página rascunho, e-mail, roteiro, carta)
- `toque` (cadência)
- `proposta`
- `contrato`
- `cliente`
- `funil` (template, versão, domínio)
- `evento` (sessão, clique_whatsapp, ligação, form)
- `conversao` (orçamento, venda, valor)
- `teste_ab`
- `relatorio`

---

## 5. Oferta, preço e a conta do ROI (Brasil)

**Marca por nicho** (a lição "Leak Proof"): por exemplo **"Gelo na Conta"** para ar-condicionado ou **"Cano Certo Marketing"** para desentupidora. É a marca do serviço; o Prumo é a fábrica invisível.

**Pacote padrão [E, a validar nas 10 primeiras conversas]:**

| Item | Preço |
|---|---|
| Implantação | **R$4.500–9.000**: Raio-X completo, 2–3 funis, tracking de WhatsApp e ligação, ajuste das campanhas, VSL |
| Mensalidade | **R$1.800–3.500/mês**: testes, conversões offline, relatório, pedido de reviews |
| Híbrido (para quebrar objeção) | R$1.200/mês + R$40–150 por orçamento agendado qualificado (definido no contrato e medido no M8) |
| Case Zero | 1º cliente de graça em troca de vídeo + números |

**Conta-modelo para o pitch [E, ilustrativa: ar-condicionado em Campinas]:**
- Gasto de R$8.000/mês em Google Ads, CPL de cerca de R$60 → cerca de 130 conversas por mês.
- Auditoria mostra WhatsApp escondido e página genérica → vazamento estimado de 20% = **26 conversas**, ou R$1.600 de mídia jogada fora.
- Fechamento de 25% × ticket misto de R$2.500 (instalação + contratos PMOC) → **≈ R$16 mil/mês em serviços que não aconteceram**.
- A mensalidade de R$2.500 se paga com **1 serviço**.

**Meta de negócio do operador solo:** 12–15 clientes × R$2,5 mil = **R$30–37 mil MRR** + implantações, com a ferramenta fazendo o trabalho de 3–4 pessoas.

**Segunda camada (como o James):** depois de 5 cases, vender o **Prumo como produto** para gestores de tráfego e agências: biblioteca + MCP + skills, por R$197–297/mês, mais uma comunidade.

---

## 6. Roadmap de construção

### Fase 0 · Concierge (semanas 1–2). Validar antes de codar
- Escolher o mercado com um "Radar manual": Casa dos Dados + 20 buscas no Google na cidade.
- Escrever as 6 skills Prumo e operar com Claude Code + Firecrawl MCP + Playwright MCP + Outscraper (CSV).
- Auditar 20 empresas, fazer 5 páginas refeitas, 5 vídeos e 3 visitas.
- **Critério de saída:** 1 Case Zero assinado e 3 conversas com dono. A auditoria manual precisa achar pelo menos 3 vazamentos em 80% dos casos.

### Fase 1 · Motor de prospecção (semanas 3–7)
- M1 Radar, M2 Garimpo (Outscraper + CNPJ + Fit Score), M3 Raio-X (Playwright + Firecrawl + Claude visão + checklist 12+4), M4 Pitch Engine (página rascunho multi-tenant, relatório, e-mail, roteiro), M5 CRM básico.
- MCP server com `garimpar`, `auditar` e `gerar_pitch`.
- **Critério:** "acha desentupidoras em Campinas que valham pitch" → 100 empresas → top 20 auditadas → 20 pitches prontos em **menos de 30 min e menos de R$60 de custo variável**.

### Fase 2 · Fechar e entregar (semanas 8–11)
- M6 (proposta interativa, ZapSign, Asaas com Pix Automático, onboarding) e M7 (biblioteca de 5 arquétipos para o 1º nicho, publicação com domínio próprio, follow-up por WhatsApp e e-mail, pedido de review).
- **Critério:** do aceite ao funil no ar em **menos de 72h**, com 90% do trabalho gerado e você só revisando.

### Fase 3 · Provar o ROI (semanas 12–14)
- M8 (código no WhatsApp, DNI Twilio, encaminhamento do Google, upload via Data Manager API e CAPI, "fechou R$" do dono) e M9 (painel, relatório mensal, A/B).
- **Critério:** relatório do 1º mês do Case Zero com custo por conversa e vendas atribuídas → vira o vídeo-depoimento.

### Depois (meses 4–6)
- 2º arquétipo de nicho só depois de 10 clientes no primeiro.
- Biblioteca curada de funis BR (anunciantes que anunciam há mais de 6 meses e tiram nota ≥ 11/12) → produto Prumo Pro.

---

## 7. Custo variável da máquina [C para preços unitários; E para o consumo]

| Etapa (por empresa) | Ferramenta | Custo aprox. |
|---|---|---|
| Descoberta + 50 reviews | Outscraper | US$0,003 + US$0,15 |
| CNPJ | Casa dos Dados / BrasilAPI | ~R$0,01 |
| Anúncios Google | DataForSEO / SerpApi | US$0,001–0,025 |
| Scrape + branding | Firecrawl | ~US$0,002–0,02 |
| Auditoria com visão | Claude Sonnet 5.5 (Batch) | ~US$0,02–0,05 |
| Pitch completo (só top 20%) | Claude Opus 5.5 | ~US$0,20–0,40 |
| **Total por prospect com pitch pronto** | | **≈ R$2–4** |

**Fixos iniciais:** cerca de R$1.000–1.800/mês, cobrindo:
- Supabase Pro
- Vercel ou Cloudflare
- Firecrawl Hobby/Standard
- Instantly
- domínios e caixas de e-mail
- Twilio
- Claude Max (para operar o Claude Code)

**Pontos de preço que mudaram e já entram no desenho:**
- WhatsApp cobra por mensagem entregue, com tarifa de serviço acima de 1.000/mês desde 01/10/2026.
- Upload de conversões offline do Google só pela Data Manager API (15/06/2026).
- A API da Meta Ad Library **não** devolve anúncios comerciais fora da UE.

---

## 8. Riscos e compliance

| Risco | Mitigação no produto |
|---|---|
| **LGPD na prospecção** (nome do sócio, e-mail nominal) | LIA documentado (Guia da ANPD de 2024), fonte de cada dado registrada, aviso da origem no 1º contato, opt-out em 1 clique que vale para todos os canais, sem guardar CPF, retenção de 12 meses para não clientes |
| **Termos de uso** (raspar Maps, Ad Library, Doctoralia) | Preferir APIs oficiais quando o custo permitir (Places API); não guardar dados do Google além do permitido; usar só agregados de Reclame Aqui; nenhuma conta falsa |
| **WhatsApp** | Nada de envio frio. API oficial só com opt-in; nenhum provedor não oficial |
| **Página refeita na marca do prospect** | Noindex, rótulo "proposta/rascunho", sem formulários ativos, retirada do ar em 30 dias ou a pedido |
| **Regras de conselhos** (CFO para odontologia, OAB) | Checklist de compliance por nicho dentro da skill de copy (sem antes e depois, sem promessa de resultado) |
| **Promessa de ROI** | Toda conta é faixa com premissas editáveis; nada de garantia de faturamento |
| **Dependência de um nicho sazonal** (ar-condicionado) | PMOC como receita de inverno; 2º nicho complementar (desentupidora) só depois de 10 clientes |
| **"Ninguém quer IA"** | A palavra IA não aparece em nada que o cliente vê. Vende-se conversa, orçamento e serviço |

---

## 9. Métricas que importam

| Frente | Métricas |
|---|---|
| **Máquina de prospecção** | Prospects/semana, % com ≥ 3 vazamentos, custo por pitch, taxa de resposta (meta de 5–10% com página + vídeo), conversas com dono por semana (meta de 5), pitch → cliente |
| **Entrega** | Tempo do aceite ao funil no ar (< 72h), custo por conversa antes e depois, % de conversas respondidas em 5 min, orçamentos, vendas atribuídas, ROI do cliente (meta ≥ 5×) |
| **Negócio** | MRR, churn (meta < 3%/mês), clientes por operador, margem bruta (> 80%) |

---

## 10. Decisões que preciso de você para começar

1. **Mercado inicial:** sugiro **ar-condicionado com PMOC** numa cidade de 500 mil a 2 milhões de habitantes onde você tenha rede (ACI, CDL, amigos donos). A alternativa é desentupidora e dedetização.
2. **Brasil apenas, ou Brasil + EUA?** O stack serve aos dois. Nos EUA as mensalidades são de 3 a 5 vezes maiores, mas há TCPA e A2P 10DLC e não há o diferencial do WhatsApp.
3. **Você opera, ou monta para uma equipe/franquia operar?** Isso muda a prioridade entre o MCP/Claude Code (operador técnico) e o app web (operador comercial).
4. **Marca do serviço** no nicho escolhido.

Com essas respostas, o próximo passo é escrever as 6 skills Prumo e rodar a Fase 0 no mercado escolhido. Dá para começar nesta mesma sessão: crio o repositório, o MCP server inicial e a skill de auditoria 12+4.

---

## Fontes principais

**Episódio e Boring Marketer**
- Episódio: https://www.youtube.com/watch?v=HKNpCwG3nlc · resumo: https://getscuttlebutt.substack.com/p/diesel-dudes-owner-main-street-plumbers
- "Stop Building AI Software. Sell to Main Street Instead." (preços e prompts): https://www.youtube.com/watch?v=-JienW-k_1o
- Masterclass de AI marketing (stack de MCPs e skills): https://www.youtube.com/watch?v=fVUlrpaWNxg · site da Diesel Dudes com Claude Code: https://www.youtube.com/watch?v=gWNFna6fgS8
- BoringFunnels: https://boringfunnels.com · GitHub: https://github.com/boringmarketer · comunidade: https://www.skool.com/the-vibe-marketers/about · https://www.thevibemarketer.com · Boring Agent: https://boringmarketing.com

**Benchmarks**
- LocaliQ home services 2025: https://localiq.com/blog/home-services-search-advertising-benchmarks/
- Unbounce: https://unbounce.com/conversion-benchmark-report/
- Leadster/Agendor, panorama de leads BR: https://www.agendor.com.br/blog/panorama-de-geracao-de-leads-no-brasil/
- RD Station sobre WhatsApp: https://www.rdstation.com/blog/conversacional/pesquisas-de-mercado-do-whatsapp-no-brasil/

**Contagens de empresas (Sebrae-PR)**
- Dedetização: https://sebraepr.com.br/comunidade/artigo/sebrae-em-dados-servicos-de-dedetizacao-2
- Marcenaria: https://www.sebraepr.com.br/comunidade/artigo/sebrae-em-dados-marcenaria
- Oficina mecânica: https://sebraepr.com.br/comunidade/artigo/sebrae-em-dados-oficina-mecanica

**APIs e preços**
- Outscraper: https://outscraper.com/pricing/
- Google Places: https://developers.google.com/maps/billing-and-pricing/pricing
- Casa dos Dados: https://portal.casadosdados.com.br/planos
- Firecrawl: https://docs.firecrawl.dev/features/scrape
- SerpApi: https://serpapi.com/pricing
- Meta Ad Library API: https://developers.facebook.com/docs/graph-api/reference/ads_archive/
- WhatsApp: https://developers.facebook.com/docs/whatsapp/pricing
- Asaas (Pix Automático): https://docs.asaas.com/docs/pix-automatico
- ZapSign: https://zapsign.co/pricing
- Cloudflare for SaaS: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/
- Google Data Manager API: https://support.google.com/google-ads/answer/15713840
- Twilio BR: https://www.twilio.com/en-us/guidelines/br/voice
- Claude API: https://platform.claude.com/docs/en/about-claude/pricing

**LGPD**
- Guia de legítimo interesse da ANPD (resumo): https://www.mattosfilho.com.br/unico/anpd-legitimo-interesse-lgpd/
