# Voz da marca e adaptação por plataforma

Este arquivo **não substitui** as fontes da voz, ele aponta para elas e acrescenta só o que é específico de redes. Ordem de leitura obrigatória para qualquer rotina que escreva em nome do Rony:

1. `skill/references/voz-e-estilo.md` (neste repositório): como ele fala, frases de assinatura e o que nunca fazer.
2. **Estrategista Digital — Prompt Mestre** (Notion, `config.json > notion.prompt_mestre_page`), seções **A3 Voz**, **A6 Comment-gate** (os três CTAs *verbatim*) e **A7 Vetos**.
3. **Acervo BIGVU — Base de exclusão** (Notion): o que já foi gravado e os bordões que **não** são dele.
4. **Gabarito das Duas Séries**, quando a peça for Por Trás das Marcas ou Manuais Práticos de IA.

Se um destes conflitar com este arquivo, a fonte vence.

## Regras que o gate checa em código

- Sem travessão (— ou –). O gate bloqueia.
- Limite de caracteres por plataforma (`config.json > plataformas`).
- Vídeo, carrossel e story exigem arquivo em `Mídia`.

## Regras que o redator segue (o gate não consegue checar)

- Português do Brasil. Frase curta, verbo forte, número concreto ("R$ 715 milhões", nunca "muito dinheiro").
- Só número que está em `skill/references/trajetoria-e-numeros.md` ou com duas fontes. Senão, não usa.
- Bordão só da lista dele. Bordão inventado é falha grave.
- CTA de comment-gate: um pedido isolado, uma palavra, um entregável. O texto dos três CTAs é **copiado**, nunca reescrito.
- Hook inspirado no que está performando (Padrões, Formatos Trending, Sandcastles), **nunca copiado**. Registrar na página qual padrão inspirou.

## Uma peça, oito saídas

A unidade de trabalho é a **Peça** (base Produção). Cada peça vira até uma linha por plataforma na Fila de Aprovação, adaptada, não colada.

| Plataforma | O que muda | Legenda | CTA |
|---|---|---|---|
| Instagram Reels | Vídeo 9:16 até 90s. Hook falado nos 3 primeiros segundos e escrito na tela. | Até 2.200. Primeira linha = hook. 3 a 5 hashtags no fim, no máximo. | Comment-gate falado no vídeo + repetido na legenda (`comenta VENDAS` / `QUERO`). |
| Instagram Carrossel | Slide 1 = hook (é a "copy do slide 1" das Referências Estáticas). 6 a 10 slides. Último slide = pedido isolado. | Curta, reforça o pedido. | Comment-gate em texto, sozinho no último card. |
| Instagram Stories | Bastidor, enquete, link. Sem roteiro longo. | Nenhuma. | Sticker de link com UTM. |
| LinkedIn | Texto nativo, não legenda de Reel. Abre com a história (Reserva, AR&Co, Rebels), fecha com o passo a passo. Pode levar o vídeo, mas o texto tem que funcionar sozinho. | 900 a 1.800 caracteres, parágrafos de 1 a 2 linhas, sem hashtag no meio. | Link com UTM **no primeiro comentário**, não no post. Palavra-chave do e-mail quando couber. |
| TikTok | Mesmo vídeo do Reels, hook ainda mais cedo (0 a 1s). | Curta, 1 linha + 3 hashtags. | Comment-gate falado. |
| YouTube Shorts | Mesmo vídeo. Título = hook em até 100 caracteres. | Descrição com link UTM. | Link na descrição. |
| X | Uma ideia, uma frase forte. Thread só para passo a passo (até 6 posts). | 280 por post. | Link UTM no último post da thread. |
| Threads | Tom de conversa, pergunta aberta no fim. | Até 500. | Sem link (alcance cai); puxa para o perfil. |

## Fontes de conteúdo e risco padrão

| Origem | De onde vem | Risco mínimo |
|---|---|---|
| Corte de podcast | `transcricoes/texto/` deste repo: trecho de 30 a 75s com timestamp | Baixo (Michel pode aprovar) |
| Repost/adaptação | Peça já aprovada e publicada em outra rede | Baixo |
| Roteiro gravado | Base Produção, Etapa ≥ Edição | Alto |
| Banco BIGVU | Roteiros BigVu Escolhidos Semanal | Alto |
| Acervo Notion | Pautas aprovadas, Referências, Padrões | Alto |
| Texto nativo | Escrito do zero pela IA (LinkedIn, X, Threads) | Alto |

Qualquer menção a Stone, preço, oferta, política, tragédia ou investimento sobe para **Alto** automaticamente (lista completa em `config.json > risco`).
