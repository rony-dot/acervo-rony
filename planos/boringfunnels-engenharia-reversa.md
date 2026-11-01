# BoringFunnels: engenharia reversa (01/11/2026)

> Este é o documento de referência factual. O plano de produto está em `mecanico-digital-plano-v2.md`.
> Coleta feita só em conteúdo público, sem autenticação:
> - páginas do site
> - headers e CSP
> - bundle JS público
> - metadados OAuth do MCP
> - vídeos do board em `/film/*.mp4`
> - vídeos no YouTube
> - posts no X
>
> Legenda: **[C]** = confirmado na fonte, **[I]** = inferido.

---

## 1. O que é, em uma frase

É uma **biblioteca curada de funis reais que estão dando dinheiro**. Cada funil é desmontado etapa por etapa, com a "jogada" (*move*) de cada uma. A biblioteca é **entregue ao agente de código do usuário** (Claude Code, Codex, Cursor) por MCP, junto com um **kit de skills e um board local** que planeja, escreve, desenha, testa e publica o funil do usuário. O plano Pro inclui ainda um **Client Finder**, que acha negócios locais para prospectar, mostra os vazamentos de cada um e gera o pitch com a correção já pronta. [C]

> "Your coding agent can build anything. Except a page that sells." (og.jpg) [C]

## 2. Stack [C]

| Camada | Ferramenta |
|---|---|
| Framework e hospedagem | Next.js (Turbopack), Vercel |
| Login e banco | Supabase |
| OAuth do MCP | O Supabase também é o servidor OAuth do MCP |
| Pagamento | Stripe Checkout |
| Email | Resend |
| Analytics | PostHog com proxy em `/ingest` e gravação de sessão, Meta Pixel + CAPI, gtag |
| Login Google | Google GSI (FedCM) |
| Afiliados | Rewardful |
| Indexação | Todas as páginas têm `noindex`. Não há robots, sitemap nem llms.txt. Produto fechado, sem SEO |

## 3. Mapa de páginas

**Públicas**
- `/`: landing do plano grátis, com o estudo da semana, uma amostra da biblioteca, "Then your agent builds yours", a comparação "Instead of…", FAQ e cadastro.
- `/start`: página de venda do Pro ("for AI services"), com P.S. assinado por James.
- `/clients`: página de venda do Client Finder.
- `/access`: login por link mágico e recuperação de compra pelo email do recibo do Stripe.
- `/terms`, `/privacy`, `/refunds`, `/removal`.
- `/upgrade` redireciona para `/clients#plans`.
- `/buy?plan=monthly|agency` vai para o Stripe.

**Atrás do login**
- `/library`, `/library?mode=funnels`, `/library/funnels/{slug}`, `/library/{slug}`, `/library/section/{página}/{seção}`
- `/account`, `/account/license`, `/account/changelog`, `/account/purchases`, `/account/settings`

**Endpoints**

| Endpoint | Função |
|---|---|
| `POST /api/join` | Cadastro: email + honeypot `company` |
| `POST /api/auth/google` | Login Google: `{credential, nonce, intent: join\|signin, next}` → `{to, created}` |
| `GET /api/me` | Sessão atual |
| `POST /api/request-access` | Pedido de link de acesso |
| `/auth/callback` | Retorno do link mágico |
| `GET /api/download?release=latest` | Download do kit (401 sem sessão) |
| `…/prompt?job=build\|page\|copy\|audit&url=` | Prompt do "Copy for your agent" em três níveis: funil, página e seção |
| `https://boringfunnels.com/mcp` | **MCP remoto via HTTP, OAuth 2.1**: Supabase com registro dinâmico de cliente, PKCE S256, escopos `openid email offline_access` |

## 4. Funcionalidades

### 4.1 Conta grátis [C]
- Cadastro pelo Google ou por email. O email traz um link e também um código de 6 dígitos.
- Toda semana chega o **estudo da semana completo**, que fica aberto "até domingo".
- Na biblioteca, o usuário grátis vê **só o 1º passo e a jogada** de cada funil.
- O botão **Copy for your agent** funciona.
- A **oferta Pro aparece logo depois do cadastro**, com opção de pular.
- O sistema registra quais estudos cada pessoa abre por semana.

### 4.2 Estudo da semana, o "funil percorrido" [C]
- Exemplo: Tony Polecastro, 5-Day Guitar Challenge, com anúncio rodando há 482 dias.
- Cabeçalho: "first ad Jun 17, 2025 · walked Sep 22–30, 2026", "8 steps · 6 seen".
- Etapas numeradas: anúncio → opt-in → página pós-botão → vídeo → emails → aulas → oferta → checkout.
  - Cada etapa tem screenshot, uma legenda curta ("Only the form") e a jogada.
  - Etapas que eles ainda não viram aparecem como "Not seen yet".
- Linha do tempo dos emails: "11 emails in 7 days", eixo Dia 0–7, papel de cada email ("The paid program rides in the P.S.").
- Exemplo de jogada da página pós-botão: *"Never a bare thank-you: confirm, give the start day, say who it's for, and hand over one thing to watch or do now, so the wait starts selling."*

### 4.3 Biblioteca [C]
- **Três níveis:** páginas, seções e funis inteiros.
- Cada **seção** é anotada com o que o comprador precisa acreditar naquele ponto e a jogada que o leva até lá.
- **Tipos de negócio:**
  - Local service (Roto-Rooter, Choice Home Warranty, LeafFilter)
  - Software & AI (Granola, Synthesia)
  - Product (Jones Road, AG1, Vuori)
  - Course/coaching (Marie Forleo, Jenna Kutcher, PTYA, IXL)
- **Formatos:** Free check, Instant price, Priced first step, Quiz, Explainer video/VSL, Follow-up machine, Seasonal offer, Live class, Free guide, Software trial.
- **Metadados de cada item:** "N ads running / N ads to this page", "captured {data}", "Just added", "Added this week".
- **Jogadas em uma linha**, exemplos:
  - Roto-Rooter: *"Makes the call the spine: the local number, huge, in the first screen."*
  - AG1: *"A per-day price in the headline, and the first order under it as a receipt."*
  - IXL: *"A checkout with the ad's plan already picked and 20% off."*
- **Tamanho declarado:** "40 local service businesses taken apart" (09/10/2026).

### 4.4 Curadoria (o fosso) [C]
1. Acham anunciantes pelos **anúncios que continuam rodando**. Longevidade do anúncio = sinal de lucro.
2. Capturam as páginas no celular e no desktop.
3. Dão nota em **12 pontos**. Só entram páginas com nota 11 ou 12.
4. Os **emails são capturados com caixas próprias**: eles se cadastram de verdade.
5. Termos de uso: *"Use the moves, never their words, brands, logos, photos, testimonials or likeness."*
6. O agente do usuário pode **pedir uma página que falta** ou **dar nota a uma página que usou**. Isso realimenta a curadoria.

O checklist de 12 pontos não é público. Pelos teardowns, inferi estes critérios [I]:
- promessa do anúncio na 1ª tela
- CTA ou ligação na 1ª tela, fixo
- nota e reviews visíveis
- primeiro passo ou preço claro
- captura de email
- agendamento curto
- página pós-botão que vende
- follow-up
- linguagem do cliente
- prova específica
- garantia
- funciona no celular

### 4.5 "Copy for your agent" [C]
- Gera um prompt em texto puro, buscado no servidor com sessão ativa, e copia via ClipboardItem. Se a cópia falhar, mostra uma textarea.
- **4 trabalhos:**
  - Build something new (padrão)
  - Improve my page
  - Rewrite my copy
  - Audit my site
- Os três últimos pedem a URL.
- A auditoria *"lists up to eight things costing them customers, worst first, each with the fix, and changes nothing on their site."*

### 4.6 Pro: MCP + kit + board local [C]
- **Setup:** um comando e depois "set up boringfunnels". O agente baixa o kit versionado, autentica o MCP por OAuth e abre um **board local no navegador**.
- Escopo do kit: *"strategy, copy, the offer, design, the build and the checks."* Gera todas as páginas, emails e o anúncio.
- **O board** tem cabeçalho "boringfunnels / build", o projeto e o menu Library:
  1. **Entradas:** build a funnel, improve one page, audit your site, rewrite your copy. O agente recomenda uma.
  2. **Cards de funil:**
     - um RECOMMENDED e de 2 a 3 ANOTHER WAY;
     - cada um com promessa, sequência de etapas e **custo estimado por venda** ("At about $2 a click, 30% leaving an email… a sale costs about $220 on a $997 program");
     - botões "See it below" e "Choose this one".
  3. **Diagrama em post-its:** anúncio → páginas → checkout → "You're in" → emails, com uma tag de fricção em cada etapa ("Asks a few questions", "Asks nothing", "Takes payment", "Not written yet"). Ao lado, uma coluna **LEVERS**: the free thing, quando pedir o email, a promessa.
  4. **Decisões do plano**, cada uma com 3 a 6 opções, uma recomendada e um "Why:":
     - **YOUR HEADLINE**, com refinadores: *Louder / Plainer words / More like the recommended / Lead with the money*
     - **THE FREE THING**
     - **THE PAID NEXT STEP**
     - **THE PROOF YOU'LL MAKE THIS WEEK**
  5. **"What this plan is based on":** cards da biblioteca ("10 sources").
  6. **Aprovação:** *"Approved. Your agent has your plan and moves on to the look next."*
  7. **Estilo:**
     - o usuário escolhe até 3 páginas reais e descreve o que gostou;
     - o sistema devolve **YOUR STYLE**: paleta, tipografia, direção de imagem e "Based on 4", com botão "Change";
     - são "nine looks in three lanes", e uma das trilhas é "your site made better".
  8. **Imagens:** comps reais a cerca de US$0,10 cada. Antes era com a chave do usuário; hoje são **100 por mês incluídas**.
  9. **Build:** preview desktop e celular de `site/index.html`.
  10. **Inspeção antes de entregar:**
      - testado em 4 tamanhos de tela;
      - **segundo revisor**;
      - **toda afirmação rastreada até a fonte**;
      - formulários testados "until a test lead arrives";
      - pronto para Netlify, Vercel ou o site do próprio usuário.
  11. **Lançamento:** 3 perguntas no chat. Um preview pode ser compartilhado sem elas.
- **Estado do agente visível no board:** "Your agent is listening: a click here reaches it at once" / "Your agent is working. Anything you click here is saved for it." O board e o chat do agente são um único canal bidirecional.
- **Arquivos do projeto:** `scorecard.md`, `offers.md`, `what-failed.md`, `site/index.html`.
- **Caso público:** um produto inexistente virou funil em 80 minutos, com 1 prompt, 15 follow-ups e US$0,96 em imagens.

### 4.7 Client Finder, incluído no Pro [C]
1. **Busca:** "find me plumbers in Dallas worth pitching". O sistema olha 100 empresas e mostra o funil de contagem: *100 no Maps → 83 com site → 24 recebendo reviews novas → 10 rodando Google Ads → 11 parecem ter $2M+*.
2. **Card do prospect:**
   - nota e nº de reviews
   - "N Google ads nos últimos 30 dias"
   - reviews por mês
   - horário de funcionamento
   - porte estimado ("by our estimate")
   - link da ficha no Google
   - vazamento principal
3. **See what's leaking:** abre no celular a página onde o anúncio deles cai e lista os vazamentos do pior para o menor, cada um com o custo explicado. Exemplos: "No call button on the first screen", "Their rating isn't on the page", "The ad's promise isn't on the first screen", "Booking is buried".
4. **Pitch with the fix built** (cerca de 15 min):
   - página na marca do prospect com o selo "CONCEPT PREVIEW" e comparação Hoje vs Nova página;
   - proposta de uma página;
   - primeiro email.
   - O envio sai da caixa do próprio usuário.
5. **Reach the owner:** dono provável e email de trabalho "Checked: it takes mail", com **a fonte de cada dado**. Nunca usa email pessoal nem celular.
6. **Oferta padrão gerada:** "Your page live in 7 days, and every call counted".
   - Entregáveis: página em 7 dias, número de rastreio + agendamentos, *missed-call text-back*, relatório semanal de uma página.
   - **30 dias grátis**, $0 para construir, depois "agreed together/mo".
7. **Pipeline:** Found → Leaks found → Pitched → Sent → Replied → Won.
   - Os três últimos estágios são marcados à mão.
   - O agente sugere o próximo passo: "find the leaks on the next 5… Nothing is sent to anyone".
8. **Cotas:**
   - **Pro:** 20 buscas e 40 emails de dono por mês.
   - **Agency:** 150 buscas, 300 emails e 300 imagens por mês.
   - Renovam no dia 1º.
   - Só fatos públicos, ninguém é contatado automaticamente.

**Ferramentas auxiliares públicas [C]**
- **Score de nicho:** 6 itens de 1 a 5 (ticket, urgência, valor do lead vs custo, concorrência online fraca, dono que opera com equipe de 2–20, consegue alcançá-los). Abaixo de 18 descarta; acima de 24 monta lista.
- **Prompt de sourcing:** "50+ reviews, 4.2+, owner-run, crew 2–20… Mark every inference as an inference."
- **Prompt "homeowner walk":** "how long does it take you to find the phone number and a way to book?… What happens after the form?"

## 5. Monetização [C]

| Plano | Preço | Inclui |
|---|---|---|
| Free | US$0 | Estudo da semana, 1º passo de cada funil, Copy for your agent |
| Pro | **US$299/ano** ("save 68%", "under $6 a week") ou **US$79/mês** | Biblioteca inteira + MCP + kit + 100 imagens/mês + Client Finder (20/40) + estudo semanal + updates |
| Agency | **US$149/mês** | Cotas maiores (150/300/300) |

- **Regras:** sem reembolso, exceto cobrança errada. Licença para 1 pessoa ou empresa, trabalho para clientes permitido, revenda da biblioteca proibida. Ao cancelar, o usuário fica com o que já construiu.
- **Gatilhos de upgrade:**
  - conteúdo travado depois do 1º passo;
  - oferta logo após o cadastro;
  - `/upgrade` aponta para o Client Finder (é ele que vende o Pro);
  - comparação com ClickFunnels ("$97–297/mês") e com agência;
  - workshops grátis no Luma;
  - cotas.
- **Afiliados** via Rewardful.

## 6. Modelo de dados inferido [C/I]

| Entidade | Campos |
|---|---|
| User | id, emails[], plan, hashed_id |
| Purchase | stripe_checkout_id, plano, preço, data |
| KitRelease / Download | versão, IP, user-agent, data |
| McpCall | tool, latência, sucesso, app do agente, rótulos (tipo de negócio, o que vende, etapa, estudo). Não guarda o texto livre |
| AgentRequest / Rating | frase, usuário, item |
| StudyOpen | usuário, estudo, semana |
| Funnel / Study | slug, anunciante, tipo, first_ad_date, walked_from/to, days_running, ads_running, steps_total/seen |
| Step | ordem, tipo, seen, screenshot, legenda, move |
| Email | posição, dia, assunto, corpo, papel |
| Page | slug, marca, tipo, url, captured_at, ads_to_page, screenshots, selling_move, score 0–12, descritor de estilo, sections[] |
| Section | página, crença, move |
| Project (local) | negócio, números, plano aprovado, estilo, páginas, emails, anúncio, checagens |
| Prospect | nome, cidade, rating, reviews, reviews/mês, ads_30d, horário, site, landing do anúncio, porte estimado, leaks[], contato com fonte e verificação, status, artefatos do pitch |
| Quota | buscas, emails, imagens / mês |

## 7. Lacunas (não públicas)

- Os critérios exatos dos 12 pontos.
- O texto do prompt gerado.
- Os nomes e esquemas das tools do MCP.
- O comando de instalação.
- A estrutura de arquivos do kit.
- As fontes de dados do Client Finder. Candidatos citados por ele: Apify/Outscraper, Google Ads Transparency, Meta Ad Library.
- O método de estimativa de receita.

**Conclusão:** essas lacunas são justamente o que **desenhamos do zero** no plano v2.

## Fontes

**Site (boringfunnels.com):**
- Páginas: `/`, `/start`, `/clients`, `/access`, `/terms`, `/privacy`, `/refunds`, `/removal`
- Bundle JS: `/_next/static/immutable/chunks/0--0q59ozpa37.js`
- Metadados OAuth do MCP: `/.well-known/oauth-protected-resource/mcp`
- Vídeos do board: `/film/loop-{board,style,build}.mp4`

**YouTube:**
- `HKNpCwG3nlc`: demo em ~4:47 e ~35:00
- `-JienW-k_1o`: ~19:16–20:44, ~28:39–31:20 e ~32:52

**X:**
- `x.com/boringmarketer/status/2108588421992071334` (artigo)
- `…/2112317152522854490` (Client Finder)
- `x.com/boringfunnels/status/2112222638462451963`
- `…/2116140993003106335` (funil em 80 min)

**Newsletters:**
- getscuttlebutt.substack.com/p/diesel-dudes-owner-main-street-plumbers
- bopyoletters.com (com paywall; lido só o resumo)
