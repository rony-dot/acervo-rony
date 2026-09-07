# snippets/

## `aba-digest.html`

Bloco pronto para dar ao digest semanal uma barra de abas apontando para o acervo
de estáticos — o outro lado da consolidação.

**Onde colar:** no gerador do digest, dentro de `<header class="site-header">`,
logo depois do `<h1>`. Não em `digest-rebels.netlify.app` pela mão: o site é
regerado toda semana e a edição seria perdida no próximo build.

O bloco reaproveita as variáveis do `:root` do digest (`--accent`, `--border`,
`--muted`, `--sans`), então acompanha o tema dele sem ajuste.

**O outro lado já está feito:** as duas páginas do acervo têm a aba
"Digest semanal ↗" apontando de volta.
