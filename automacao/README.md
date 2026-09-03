# Automações

## Referências do Instagram → Sandcastles → Notion

Salvou um reel, a máquina transcreve e escreve a página. Você só classifica depois.

```
você salva o post  →  rotina de hora em hora  →  Sandcastles transcreve/analisa
                                              →  página completa em Referências — Vídeos
                                              →  Status "pendente" (esperando sua classificação)
```

### Como salvar um post

**Caminho principal — pasta no Sandcastles.**
No Sandcastles, jogue o vídeo na pasta **📥 Referências Rony — auto**
(`f053f61a-d2c3-4221-b587-2681c409a501`). É a pasta-inbox: tudo que cair ali entra na fila.

**Caminho alternativo — link direto no Notion.**
No celular: Instagram → Compartilhar → Notion → base **Referências Conteúdo Rony**.
A linha nasce com a URL crua no título; a rotina reconhece, analisa e reescreve com título de gente.

Os dois caminhos terminam no mesmo lugar. Use o que for mais rápido no momento.

### O que não dá para fazer (e por quê)

Não existe jeito de ler a pasta de **Salvos do próprio Instagram**. A API do Instagram não expõe
os itens salvos nem as coleções — nem pela Graph API, nem pelo IFTTT (os gatilhos de Instagram lá
são só "novo post *seu*"). Só sobraria raspar a sessão logada, que quebra os termos do Instagram e
para de funcionar a cada mudança de layout. Por isso o gatilho é a pasta do Sandcastles ou o
compartilhamento para o Notion — duas ações com o mesmo número de toques que o "salvar".

### O que sai no Notion

Página na base **Referências — Vídeos**, dentro da Central de Conteúdo, com:

- ficha rápida (views, likes, comentários, engajamento, outlier, formato, layout, categoria de hook);
- transcrição completa em PT-BR no corpo da página, em blocos com faixa de tempo — e o original,
  quando o vídeo não é em português;
- leitura de estrutura: mad lib do hook, arco narrativo, crença atacada, realidade contrária;
- a leitura editorial para o pipeline do Rony (o que dá pra roubar, onde o vídeo deixa dinheiro na
  mesa no CTA, etapa ACP, linha de conteúdo);
- propriedades preenchidas, canal relacionado em Canais monitorados (criado se ainda não existir).

O Status final é **pendente** de propósito: `pronto` é decisão editorial do Rony no ritual de
segunda, não da máquina.

### Estados do Status

| Status | Significa |
|---|---|
| `analisando` | linha reservada, análise pedida ao Sandcastles, corpo ainda não escrito. A próxima rodada termina. |
| `pendente` | página pronta, esperando a classificação de padrões (ritual de segunda) |
| `pronto` | você já classificou |
| `sem crédito` | acabaram os créditos do Sandcastles no ciclo |
| `não suportado` | link de plataforma que o Sandcastles não analisa |
| `erro` | falhou; o motivo está no corpo da página |

### Estado: falta ligar pela UI

A rotina existe (`trig_01Dbeu3Qn3oCEkYHbZkRUcs7`) mas está **pausada**, porque uma rotina criada
pela API do Claude Code não recebe os conectores: a sessão que ela dispara sobe sem as ferramentas
do Notion e do Sandcastles, e a rodada morre em 13 segundos sem fazer nada. Testado três vezes.

**Para ligar:** claude.ai → Routines → nova rotina, de hora em hora, colando o prompt de
`referencias-instagram/ROTINA.md` (o texto entre `--- PROMPT ---` e `--- FIM DO PROMPT ---`) e
marcando os conectores **Notion** e **Sandcastles**. Depois é só apagar a rotina pausada.
As rotinas que já funcionam — Radar Diário, Digest semanal, Painel de Vendas — foram criadas assim.

Enquanto não estiver ligada, o caminho é pedir no chat: "transcreve esses e joga no Notion", com os
links. A rodada manual usa exatamente o mesmo prompt.

### Coordenadas

| O quê | Id |
|---|---|
| Rotina (Routine), pausada | `trig_01Dbeu3Qn3oCEkYHbZkRUcs7` — cron `1 * * * *` (de hora em hora, no minuto 1 UTC) |
| Pasta-inbox no Sandcastles | `f053f61a-d2c3-4221-b587-2681c409a501` |
| Base Referências — Vídeos | `df3243fe-5156-8375-b0ca-81867311eaf0` · data source `a6d243fe-5156-83ee-8e15-87615b519cc8` |
| Canais monitorados | data source `d4d243fe-5156-82db-9eb7-073ae562dae2` |

### Custo e limites

Cada vídeo novo custa **1 crédito** do Sandcastles (vídeo já analisado na base não custa nada).
No máximo **10 vídeos por rodada** — o que sobrar entra na próxima hora.
Se os créditos acabarem, a rotina marca `sem crédito` e não insiste.

### Latência

De hora em hora — o mínimo permitido para rotinas agendadas. Na prática, um post salvo às 14h10
vira página até as 15h05. Para não esperar, é só pedir no chat: "transcreve esse aqui e joga no
Notion" com o link.

### Mexer na rotina

- **Pausar:** desligue a rotina em claude.ai → Routines, ou peça no chat.
- **Criar pela API não serve:** a rotina sobe sem conectores e a rodada não escreve nada. Tem que
  ser pela UI de Routines, que é onde se anexam Notion e Sandcastles.
- **Mudar o comportamento:** edite `referencias-instagram/ROTINA.md` — é a fonte da verdade — e
  peça para atualizar a rotina com o texto novo. O que roda é uma cópia do prompt, então os dois
  precisam andar juntos.
- **Digest:** esta rotina não notifica ninguém. Quem avisa é a rotina "Radar Diário — PDF de
  referências no Telegram", às 6h de São Paulo, com tudo que foi transcrito no dia anterior.
