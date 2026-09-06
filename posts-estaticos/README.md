# Posts Estáticos — catálogo do acervo de referências

Extração completa do deck **"Posts Estáticos"** (Google Slides, 108 slides, 228 MB), lido print a print.

| Arquivo | O quê |
|---|---|
| `CATALOGO.md` | Lista geral: 73 blocos de referência, slide a slide, com o texto de cada página de carrossel transcrito |
| `TOP50.md` | Os 50 selecionados para adaptar ao padrão visual, com ranking, justificativa, pilar, estágio de funil e esforço |
| `posts-estaticos.html` | As duas coisas em uma página navegável, com busca no catálogo |
| `acervo-visual.html` | Catálogo visual: o texto de cada post ao lado das 388 artes extraídas, com lightbox |

## Como a extração foi feita

O texto nativo dos slides só traz as anotações — os posts em si são imagens. O pipeline foi:

1. Exportar a apresentação como PDF (61 MB).
2. `pymupdf` para extrair as 412 imagens embutidas com a posição de cada uma na página (a posição é o que permite saber quais prints formam um mesmo carrossel).
3. Recortes otimizados por tipo: imagem inteira para cards de story, corte do corpo para screenshots de celular, e *tiles* da página em alta resolução (300–420 dpi) para as páginas com dezenas de prints sobrepostos.
4. Leitura visual de cada peça e transcrição para `cat/pNNN.md`, depois consolidada.

Slides 1–26 são a parte de estratégia e governança do departamento de conteúdo, não referências de post. As referências vão do slide 27 ao 105.

## Idioma

Todo o conteúdo transcrito está em **português do Brasil**, inclusive quando a arte original está em inglês — a ideia é ler o texto em português e olhar a arte ao lado. Ficam no original: perfis (@), nomes de marcas, nomes próprios e títulos de livros.

## Páginas publicadas

- Relatório (lista geral + Top 50 + calendário): https://claude.ai/code/artifact/df6aaeb3-b12e-4bab-84b2-f29143296448
- Acervo visual (texto + arte lado a lado): https://claude.ai/code/artifact/36569e4d-ca4a-41cf-9e0f-8f461baa30e9

## Como usar

Para escolher a pauta da semana: abra o `TOP50.md` e pegue o próximo item do tier corrente.
Para achar uma referência específica: use a busca do `posts-estaticos.html` (por tema, por @perfil ou por número de slide).
Para ver a arte junto do texto: `acervo-visual.html` — 388 artes em grade, filtro "só top 50", clique para ampliar. As artes são WebP embutidos como data URI (orçamento de ~260 mil pixels por imagem, para a página caber no limite de 16 MB de um Artifact).
