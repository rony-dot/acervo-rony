# site/ — o que vai pro ar

Pasta publicada na Netlify (projeto `acervo-posts-rony`, mesma conta do `digest-rebels`).
Só o que está aqui fica público — o resto do repositório (transcrições, skill) não sobe.

| Arquivo | O quê |
|---|---|
| `index.html` | Relatório: lista geral, Top 50, calendário e o catálogo com as artes |
| `acervo.html` | Acervo visual: os 73 blocos abertos, texto ao lado das artes |
| `robots.txt` + `_headers` | `noindex, nofollow` — o link funciona para quem tem, mas não é indexado |

## Como republicar depois de mudar o conteúdo

Os HTMLs são gerados a partir de `posts-estaticos/CATALOGO.md` e `posts-estaticos/TOP50.md`.
A versão do site é a mesma das páginas do Claude, com duas diferenças: links relativos
entre as duas páginas e um documento HTML completo (`<!doctype>`, `charset`, `viewport`) —
nos artifacts esse invólucro é injetado pelo serviço, num host estático não.

```bash
STANDALONE=1 SIBLING_VISUAL=acervo.html OUT_REPORT=site/index.html  python3 gen.py
STANDALONE=1 SIBLING_REPORT=index.html  OUT_VISUAL=site/acervo.html python3 gen2.py
npx -y @netlify/mcp@latest --site-id 6ba76b0b-26d4-4033-917b-0f140ff13aa3
```

O deploy tem que rodar de um diretório que contenha **apenas** `netlify.toml` e `site/` —
o comando sobe o diretório inteiro para o build system da Netlify.
