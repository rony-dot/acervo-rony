# Brief de pesquisa: semana de 12 a 18/10/2026 (Social OS, @rony)

Gerado em 11/10/2026 em modo somente leitura (nada foi criado nem editado no Notion). Toda métrica abaixo vem da fonte citada ao lado, com link. Onde a fonte não trouxe número, está escrito "sem número".

## 0. Fontes: o que funcionou e o que falhou

| Fonte | Status | Observação |
|---|---|---|
| Notion, Padrões: Hooks e Formatos | Parcial | 13 padrões lidos. Os rollups `Outlier médio`, `Views médias`, `Nº de posts` e `Leads gerados` voltam como referência opaca (`rollupResult://...`) no MCP e não são consultáveis por SQL. Nenhum padrão tem `Posts publicados` vinculado, então mesmo no Notion esses rollups estariam vazios. **Ranking por outlier médio impossível**; ordenei por Confiança e Versão Rony. |
| Notion, Formatos Trending | OK | 7 formatos com Score ≥ 65 e não Saturando. |
| Notion, Pautas | OK, com ressalva | 9 pautas Aprovada (todas com nota ≥ 7). **Todas já têm Produção vinculada** e todas foram criadas em 24/08/2026. Nenhuma pauta aprovada "livre". |
| Notion, Roteiros BigVu Escolhidos Semanal | OK | Existem semanas cadastradas até 02/11/2026. Usei a semana de gravação **12/10/2026** (a do brief). Todas as 220 linhas da base estão "A gravar"; nenhuma "Gravado". |
| Notion, Produção | OK, resultado vazio | **Zero peças em Edição ou Agendado.** Listei as de Gravação e Aprovação Rony como contexto. |
| Sandcastles `top_hooks` (watchlist, 7 dias) | OK | 30 vídeos analisados. Retorna madlib e título, **não a frase falada literal** dos vídeos de terceiros. |
| Sandcastles `top_topics` (watchlist, 7 dias) | OK | Mesmo conjunto de vídeos do `top_hooks`. |
| Sandcastles `get_channel_recap` @rony (14 dias) | OK | 27 vídeos de 27/09 a 10/10/2026. Média do período: outlier 1,93x, 74.656 views, engajamento 1,04%. |
| Notion, Acervo BIGVU: Base de exclusão | OK | Página lida inteira (última atualização da página: 20/08/2026). |
| Notion, Prompt Mestre (A3, A6, A7) | OK | Página de ~91 mil caracteres salva em arquivo; seções extraídas por python. |
| Fila de Aprovação (linhas "Ajustar") | Não consultada | Fora do escopo deste pedido. A rotina 01 manda tratar isso como prioridade 1; precisa ser lido na etapa de geração. |

---

## 1. Padrões mais fortes (Notion: Padrões, Hooks e Formatos)

Fonte: [base Padrões](https://app.notion.com/p/bb3243fe515682d9b932016ed0312747). A base tem só 13 padrões. Nenhum tem número próprio (ver seção 0). Ordem: primeiro os "Testado e funcionou", depois os hooks não testados que já têm Versão Rony.

| # | Padrão | Tipo / gatilho | Confiança | Definição | Exemplo verbatim | Versão Rony |
|---|---|---|---|---|---|---|
| 1 | [Número específico e improvável](https://app.notion.com/p/e66243fe515683b0b4e501e510063bef) | Hook / Curiosidade | Testado e funcionou | Abre com um número exato e estranho que obriga o cérebro a pedir contexto. | "Cinco mil reais. Era isso que a gente tinha." | "Cinco mil reais. Era tudo que eu e meus sócios tínhamos juntado. Pensa comigo." |
| 2 | [História, virada, princípio](https://app.notion.com/p/b61243fe515682b1826a0131241eb893) | Estrutura narrativa | Testado e funcionou | Conta um caso concreto, revela a virada inesperada, extrai um princípio generalizável no fim. | (vazio) | (vazio) |
| 3 | [Inimigo comum, depois solução](https://app.notion.com/p/047243fe51568225a2ee81554cf74d8d) | Estrutura narrativa | Testado e funcionou | Nomeia um vilão que o público já sente, valida a raiva, e só então apresenta o caminho. | (vazio) | (vazio) |
| 4 | [Talking head com corte seco](https://app.notion.com/p/313243fe51568240820d01a6fe83eca4) | Formato | Testado e funcionou | Câmera fixa, close, sem b-roll, cortes secos a cada respiração. | (vazio) | (vazio) |
| 5 | [Objeto como prova](https://app.notion.com/p/97f243fe5156829086b4014eed593ed3) | Formato | Testado e funcionou | Um objeto físico entra em cena e carrega o argumento no lugar do texto. | (vazio) | (vazio) |
| 6 | [Transformação visual em cena](https://app.notion.com/p/e77243fe515682aeaed101f8b9253d8c) | Formato | Testado e funcionou | O apresentador muda algo em si mesmo ou no cenário enquanto fala, e a mudança é o argumento. | (vazio) | (vazio) |
| 7 | [Contradição de autoridade](https://app.notion.com/p/e71243fe5156827598d2817491090b21) | Hook / Contradição | Não testado | Alguém com credencial no assunto diz o oposto do que se espera dele dizer. | "Eu construí uma empresa de dois bilhões e vou te dizer por que plano de negócio é perda de tempo." | "Eu passei dezoito anos construindo uma marca e vou te falar a coisa que ninguém fala. A verdade verdadeira é que." |
| 8 | [Confissão de custo](https://app.notion.com/p/729243fe51568347b3ab019568181d15) | Hook / Identificação | Não testado | Abre admitindo algo que custou caro, financeiro ou emocional, antes de qualquer lição. | "Essa decisão me custou dois anos." | "Essa decisão me custou dois anos e quase o negócio inteiro. Calma, valente, calma, que eu vou te contar." |
| 9 | [Erro que você provavelmente está cometendo](https://app.notion.com/p/5b2243fe5156825ca2da816ba2fce1f4) | Hook / Perda | Não testado | Nomeia um erro comum e sugere que quem assiste está dentro dele agora. | "Se você faz isso na sua empresa, você está queimando dinheiro sem perceber." | "Se liga. Se você faz isso no seu negócio, você tá queimando caixa e nem percebeu ainda." |
| 10 | [Pergunta que só o público-alvo responde](https://app.notion.com/p/b04243fe5156839eb9c5017123d0a324) | Hook / Pertencimento | Não testado | Uma pergunta que filtra quem assiste e faz o público certo se identificar em segundos. | "Você já demitiu alguém que gostava?" | "Você já teve que demitir alguém que você gostava de verdade? Então esse aqui é pra você." |
| 11 | [Promessa de tempo curto](https://app.notion.com/p/f63243fe51568261a8cb81cd842ed319) | Hook / Ganho | Não testado | Entrega uma promessa concreta com prazo explícito logo na primeira frase. | "Em quarenta segundos eu te mostro como resolver isso." | "Em quarenta segundos eu te mostro um problema de negócio resolvido com IA. Um só." |

Não listados (sem exemplo nem prova): Entrevista de um lado só, Estáticos.

Notas de uso:
- O padrão 1 tem uma nota interna: "Funciona porque número redondo soa inventado e número específico soa vivido. O R$5 mil e o R$2 bi são os dois ativos mais fortes dessa categoria." **Conflito:** a Base de exclusão padroniza o capital inicial em **R$3 mil**, não R$5 mil. A Versão Rony do padrão 1 precisa ser corrigida antes de ir ao ar.
- Padrão 7, Versão Rony: "dezoito anos" bate com o padrão oficial (18 anos).
- Padrão 8 é a porta de entrada para a lacuna "fracasso próprio com nome, número e consequência" (seção 7).

---

## 2. Formatos Trending (Score ≥ 65, não Saturando)

Fonte: [base Formatos Trending](https://app.notion.com/p/882243fe5156826690c801f4a9483783). Números exatamente como estão na base.

| Formato | Score | Status | Outlier | Views | Gate | Esforço |
|---|---|---|---|---|---|---|
| [Gate Isolado com Entregável Nomeado](https://app.notion.com/3e2243fe51568197b34fdf2401f477fe) | 95 | Testar esta semana | 89,9 | 156.269 | Nativo | Grava sozinho em 20min |
| [Regra Que Eu Não Tenho](https://app.notion.com/3ed243fe5156816e8a00cda71a00188c) | 85 | Novo | 468,6 | 4.812.296 | Com ajuste | Grava sozinho em 20min |
| [Enciclopédia Falada de Conceitos com Corte por Card](https://app.notion.com/3e3243fe515681288aade3eb6682e47d) | 81 | Novo | 1211,2 | 12.393.109 | Nativo | Precisa edição |
| [Troca de Hábito com Conta de Chegada](https://app.notion.com/3e3243fe515681f1856ec7aabf648131) | 79 | Novo | 2928,7 | 2.610.929 | Com ajuste | Grava sozinho em 20min |
| [Dois mundos, mesmo padrão](https://app.notion.com/85e243fe515682cda17c0119a6d650be) | 78 | No banco | 15,2 | 2.812.950 | Nativo | Precisa edição |
| [Alerta de Perfil Contrariante](https://app.notion.com/3f1243fe5156812ab4bdc929373be59e) | 77 | Novo | 274,2 | 2.668.731 | Com ajuste | Grava sozinho em 20min |
| [A gente fazia X, agora só faz Y](https://app.notion.com/26c243fe5156831da06c013584b4ce63) | 76 | No banco | 19,6 | 2.278.811 | Com ajuste | Grava sozinho em 20min |

### 2.1 Mecânica e onde entra o CTA

**A. Gate Isolado com Entregável Nomeado (95).** Referência: [reel](https://www.instagram.com/reel/DdKinc8hjAq/) (@billycoxcoaching, @liamfromvulcan). Reforço registrado na base em 25/09/2026: @smartleadai "Comment WORKFLOW", 75.684 views, 2.021 comentários, outlier 152,9 ([reel](https://www.instagram.com/reel/Dcq0nmpyEUR/)).
- Mecânica: hook nomeia uma dor específica (0 a 3s); 15 a 40s de contexto ou exemplo real; últimos 3 a 5s com ação visual cortada e o pedido sozinho, com o nome do entregável dito.
- CTA: "Isolado no último segundo, sozinho na tela, sem CTA falado competindo: 'Comenta [palavra] que eu mando o [entregável nomeado]'".
- Hook da base: "Cliente sumiu depois do orçamento. Isso não é falta de sorte, é falha de processo."
- Atenção: `Semanas na lista` = 3. A regra da própria base diz "3 semanas sem uso vira Saturando e cai". Se não for usado nesta semana, sai.

**B. Regra Que Eu Não Tenho (85).** Referência: [reel](https://www.instagram.com/reel/Dc3jIMSDzKj/) (@zerodollarcoach, fora da watchlist).
- Mecânica: 0 a 3s, regra que o dono "deveria" ter e deliberadamente não tem, com a reação do público embutida; 3 a 35s, o porquê; fecha reformulando o modelo mental. Talking head sem corte de cena.
- CTA: original sem gate. Ajuste: pedido único e isolado nos últimos 5s, sem "siga" nem "salve".
- Hook da base na voz do Rony: "Eu não tenho regra de horário pra ninguém aqui. Metade dos donos que tão me vendo vai achar que eu tô errado."

**C. Enciclopédia Falada de Conceitos com Corte por Card (81).** Referência: [reel](https://www.instagram.com/reel/DdfC9HHiEUm/) (@davidepstein).
- Mecânica: cada conceito vira card nomeado na tela, 1 a 2 frases de explicação, corte seco, repete 4 a 6 vezes, fecho reflexivo.
- CTA: nativo, no último card: "comenta [PALAVRA] que eu te mando a lista completa".
- Hook da base: "Primeiro conceito: Chief Vassoura Officer." **Cuidado:** Chief Vassoura Officer está `[REPETIDO 10+]` no acervo. Trocar o conceito de abertura.

**D. Troca de Hábito com Conta de Chegada (79).** Referência: [reel](https://www.instagram.com/reel/DctNitOt5wa/) (@growithquentin).
- Mecânica: 0 a 1s, hook de custo de oportunidade; 1 a 7s, 4 passos concretos; fecho com conta de chegada em R$; legenda com os 4 passos.
- CTA: original empilhado (siga + comente + salve). Ajuste obrigatório: um pedido só, no fim.
- Hook da base: "Enquanto você tá aí vendo série, seu concorrente tá fazendo isso."

**E. Dois mundos, mesmo padrão (78, No banco).** Referência: [reel](https://instagram.com/reel/DbLe9wspP-s) (@codiesanchez). Mecânica: dois contextos que ninguém compara, mesmo sinal de fracasso. CTA: fim, com promessa de conteúdo estendido.

**F. Alerta de Perfil Contrariante (77).** Referência: [reel](https://www.instagram.com/reel/DdmRJMEN6eJ/) (@drgavingcook); segundo caso [reel](https://www.instagram.com/reel/DdmwcbVxiEX/) com 2.220.153 views, outlier 226,5. CTA: últimos 5s isolado (original sem gate). Hook da base: "O dono mais perigoso do seu mercado é o que não faz questão de parecer esperto."

**G. A gente fazia X, agora só faz Y (76, No banco).** Referência: [reel](https://instagram.com/reel/Db7Xr2GtImb) (@orenmeetsworld). CTA: "Precisa ser forçado no fim. O formato não pede naturalmente, e esse é o ponto fraco dele."

---

## 3. Pautas aprovadas

Fonte: [base Pautas](https://app.notion.com/p/40f243fe515682b6bb6501891c2c2505). Filtro: Status Aprovada ou nota ≥ 7. Todas as 9 têm Status Aprovada, Tenho prova própria = sim, criadas em 24/08/2026, e **todas já têm linha em Produção** (relação preenchida). Pela regra da rotina ("Aprovada, ainda sem Produção") nenhuma está livre; servem como material para peças já existentes.

| Pauta | Nota | Ângulo | CTA | Linha |
|---|---|---|---|---|
| [Trabalho Ao Redor do Trabalho (carrossel)](https://app.notion.com/bad243fe51568360bbf301b3930119f4) | 9 | 30 a 40% do dia do time é trabalho ao redor do trabalho, e essa é a fatia mais barata e rápida de delegar pra IA. | comenta QUERO | MDD AI |
| [Sociedade: a briga que quase acabou com a Reserva](https://app.notion.com/09b243fe5156838a8bac811763cf22eb) | 8 | Sociedade nenhuma quebra numa discussão, quebra num silêncio. A gente trata sócio como casamento e gerencia sócio como emprego. | palavra-chave do e-mail | Marca pessoal, MDD Negócios |
| [Não existe sair do operacional (reel)](https://app.notion.com/541243fe5156832d948181aaff8cbbde) | 8 | O dono não precisa sair do operacional, precisa escolher os poucos processos-chave em que só ele deve entrar. | comenta VENDAS | MDD Negócios |
| [Processos-Chave e Zona de Potência (carrossel)](https://app.notion.com/433243fe515682ef9ba481e0a2bb76d9) | 8 | Cruzar processo-chave com zona de potência numa matriz 2x2 diz onde o dono deve entrar fundo e de onde deve sair. | comenta VENDAS | MDD Negócios |
| [Os 9 Blocos do Vendedor Automático: SPIN e BANT (carrossel)](https://app.notion.com/6c7243fe51568381a693815dbdecd4e1) | 8 | Responder o WhatsApp em 5 minutos multiplica por 21 a chance de fechar, e um agente com SPIN e BANT faz isso 24 horas. | comenta QUERO | MDD AI |
| [Radar de Mercado com Sol, Terra e Luna (Manuais Práticos de IA Ep.2)](https://app.notion.com/27e243fe515683aabea1011f5c56044d) | 8 | Um analista de mercado automático dentro de um agente é a versão prática do radar competitivo que toda PME precisa. | palavra-chave do e-mail | MDD AI |
| [Grupo Estrela: plano de recuperação judicial de R$109,1 milhões](https://app.notion.com/4b6243fe5156836b80a98171141ece7c) | 7 | Marca não paga dívida. Marca forte sem operação saudável por trás é decoração. | comenta VENDAS | MDD Negócios |
| [Os PDFs de um bilhão de dólares que ninguém tá lendo](https://app.notion.com/fc9243fe51568345b29001cd670e8526) | 7 | A próxima ideia mais valiosa do seu negócio já existe, escrita e ignorada, num documento interno. | comenta VENDAS | MDD Negócios |
| [Receber antes de entregar: o modelo de caixa que ninguém usa](https://app.notion.com/fe3243fe51568253a2280125ad57790f) | 7 | Negociar prazo de fornecedor e de cliente na mesma direção transforma o negócio em banco de si mesmo. | comenta VENDAS | MDD Negócios |

Notas:
- "Sociedade: a briga..." cai exatamente na lacuna nº 2 do acervo (conflito real entre sócios). É a pauta de maior valor estratégico da lista. O ângulo no Notion usa travessão; tirar antes de usar (A3).
- "Grupo Estrela" encosta na lacuna "Recuperação judicial por porte de empresa" (zero ocorrências) e no tema Brasil/macro "recuperação judicial crescendo" (11/05, 25/05). O número R$109,1 mi precisa de duas fontes (A7). "R$" força risco Alto no config.
- "Receber antes de entregar" encosta em "varejo quebra no caixa e não no DRE" (24/05/2026) e no recém-publicado "atacado antes do varejo" (06/10, ver seção 6). Precisa de ângulo novo.

---

## 4. Roteiros BigVu da semana de gravação 12/10/2026

Fonte: [base Roteiros BigVu](https://app.notion.com/p/f2e243fe515682278e6d01ec5657713a), filtro Semana = 2026-10-12. 20 roteiros, todos "A gravar", nenhum gravado. Outlier de referência é o que está registrado na linha (o maior outlier do padrão na watchlist naquela semana, segundo a própria base).

| # | Roteiro | Tema | Padrão de referência | Outlier ref. | Hook (1 a 2 linhas do roteiro) | Alerta |
|---|---|---|---|---|---|---|
| 1 | [A Reserva e o sonho de Natal que virou campanha](https://app.notion.com/p/3e6243fe5156811a983ef61034d0ad4f) | Histórias de marcas | Case de marca em storytelling pessoal | 40,6 (@ritu_david) | "Fala galera, eu to muito muito muito muito feliz. A Reserva, como em tantas outras ocasiões, me permitiu realizar um sonho de muitos anos." | Campanha Natal 2023; precisa reposicionar como retrospectiva. |
| 2 | [Por que nasceu a Oficina Reserva](https://app.notion.com/p/3e6243fe5156816ca4d3ce7a1550a2a6) | Histórias de marcas | Origem de marca com motivo real | 40,6 (@ritu_david) | "A Oficina Reserva, marca que só cresce e aparece no mercado, nasceu por dois principais motivos:" | Cita cupom "ronyrsv" e 3ª edição da Limonada: datado; "cupom" força risco Alto. |
| 3 | [Toda empresa nasce de uma revolução e morre numa reunião](https://app.notion.com/p/3e6243fe51568116aca8e9296dbb2b1f) | Histórias de marcas | Crítica analítica contrarian | 62 (@elliottspeaks) | "Toda empresa nasce de uma revolução — mas, com o tempo, tende a virar uma reunião." (o travessão do original fere A3) | Acervo já tem "fundador x executivo". Números de Galló/Renner precisam de 2 fontes. |
| 4 | [De executiva em Dubai a fundadora de marca global de cílios](https://app.notion.com/p/3e6243fe515681938b05f9a9bb349a6b) | Histórias de marcas | Case de fundadora | 40,6 (@ritu_david) | "Essa mulher largou pra trás sua carreira de executiva financeira em Dubai pra abrir um blog de beleza e ser maquiadora na terra dos anjos." | Zona de saturação 3 (case estrangeiro em 3 pilares). |
| 5 | [Alo Yoga: a marca que vendeu um mundo, não uma legging](https://app.notion.com/p/3e6243fe5156814bb2defe22f8c081ab) | Histórias de marcas | Case com virada cultural | 62 (@elliottspeaks) | "Você já reparou que tem marcas que não precisam te convencer a comprar nada? Elas criam um mundo que você quer pertencer." | Zona 3; "escassez planejada / drop" é `[REPETIDO]`; tem "me segue" no meio (fere gate isolado). |
| 6 | [O paradoxo do tempo: a escassez de US$63 bilhões](https://app.notion.com/p/3e6243fe5156814494eded446b96f1c6) | Modelo de negócios | Revelação de mercado oculto | 300,5 (@vaibhavsisinty) | "Existe um relógio que custa US$ 35.000 no varejo. Você não pode comprá-lo." | Roteiro truncado no Notion (íntegra em arquivo externo). Escassez planejada `[REPETIDO]`. |
| 7 | [Ele fatura US$10 milhões por ano com apps de IA sem programar](https://app.notion.com/p/3e6243fe515681f492dfcea31e8271df) | Modelo de negócios | Mecanismo replicável | 30,3 (@alexhormozi) | "Esse é o Blake Anderson, ele tem só 23 anos e fatura mais que 10 milhões de dólares por ano com aplicativos saas feito usando inteligencia artificial." | "micro-SaaS em 48h" `[REPETIDO]`; Bubble/V0/Framer já cobertos. |
| 8 | [Três irmãos, uma janela de café em Curitiba](https://app.notion.com/p/3e6243fe5156811fb01cddd3b4be08f9) | Modelo de negócios | Origem humilde, escala global | 32,9 (@danmartell) | "Tres irmaos largaram tudo pra vender cafe numa janela em Curitiba. Hoje tem loja em Paris, Dubai, Miami e mais 25 paises." | Case fresco. Toca juros como argumento (lacuna "Selic como janela"). Base pede trocar CTA com data 14/04. |
| 9 | [Sua empresa vende todo mês e não sai do lugar?](https://app.notion.com/p/3e6243fe515681568b17f2307d15920c) | Modelo de negócios | Mecanismo em números simples | 30,3 (@alexhormozi) | "Tem empresa que vende mais todo mês… e mesmo assim não sai do lugar." | Retenção x aquisição `[REPETIDO]`; @rony publicou retenção em 02/10. |
| 10 | ['Tempo é dinheiro' é a frase mais perigosa dos negócios](https://app.notion.com/p/3e6243fe515681d88915e1db1b1aa780) | Modelo comportamental | Contrarian sobre crença popular | 1011,9 (@davidepstein) | "Hoje, numa reunião, pela milionésima vez, eu escutei a velha e péssima frase: 'Tempo é dinheiro.'" | Próximo de "extrato do tempo" `[REPETIDO]`. Estudo DeVoe e House 2011 precisa de 2 fontes. |
| 11 | [O Gap de Responsabilidade](https://app.notion.com/p/3e6243fe5156819282bcf62c8d77508d) | Modelo comportamental | Framework binário | 1011,9 (@davidepstein) | "Então hoje eu vou falar sobre o que eu chamo de Gap de responsabilidade." | Hook fraco na abertura; tese fresca. |
| 12 | [O método de decisão que construiu uma empresa de R$2 bilhões](https://app.notion.com/p/3e6243fe515681f988fdd50bcdac9d03) | Modelo comportamental | Framework com prova própria | 1011,9 (@davidepstein) | "Hoje de manhã eu tava fazendo um exercício de tomada de decisão que sempre repito e me dei conta que nunca contei pra vocês." | Fresco e com prova própria. Usar "~R$2 bi de faturamento" conforme padrão oficial. |
| 13 | [O italiano que apostou no bem-estar corporativo](https://app.notion.com/p/3e6243fe515681ffba98d48b228049d9) | Modelo comportamental | Tese antes da tendência | 24,4 (@drgavingcook) | "Esse maluco aqui se chama Nerio Alessandri." | Wellness `[REPETIDO 12+]`. |
| 14 | [O botão de pânico que Sam Altman apertou](https://app.notion.com/p/3e6243fe51568107b896f0af9e3625c6) | AI | Bastidor de IA com números | 300,5 (@vaibhavsisinty) | "A empresa que criou o ChatGPT acabou de apertar o botão do pânico." | Notícia de 01/12/2025: velha em out/2026. |
| 15 | [Anthropic gastou US$10 milhões pra dizer que nunca vai ter anúncio](https://app.notion.com/p/3e6243fe5156814abe72ed1c2d9600dc) | AI | Rivalidade com número chamativo | 300,5 (@vaibhavsisinty) | "A Anthropic gastou 10 milhões de dólares em anúncios no Super Bowl pra dizer que nunca vai colocar anúncios dentro da sua inteligência artificial." | Super Bowl de fev/2026: velho. Crítica nominal a Sam Altman (A7). CTA cita "Business of Brands", não é dele. |
| 16 | [Você está tratando a IA como subordinado](https://app.notion.com/p/3e6243fe515681ff9b6ce5755f5efb31) | AI | Contrarian de uso de ferramenta | 1011,9 (@davidepstein) | "A maioria das pessoas ainda fala com a IA como se estivesse dando ordens." | Próximo de "IA como funcionário recém-contratado" (acervo). |
| 17 | [O Claude reduziu 10 semanas de burocracia médica pra 10 minutos](https://app.notion.com/p/3e6243fe5156812fa469c33dba6b37ea) | AI | Aplicação surpreendente de IA | 300,5 (@vaibhavsisinty) | "O maior rival do ChatGPT acabou de criar uma parada que pode revolucionar a medicina mundial!" | Dados Novo Nordisk/Sanofi precisam de 2 fontes. |
| 18 | [300 empresas reposicionadas revelaram o mesmo erro](https://app.notion.com/p/3e6243fe5156812087cdf17e06bb861e) | Posicionamento | Autoridade + estatística | 13,2 (@douggrindstaff) | "Uma mulher ajudou 300 empresas a se reposicionar. E descobriu que na maioria delas o time de marketing, o time de vendas e o time de produto discordam sobre quem é o próprio concorrente." | Fresco; tem prova própria (camiseta a R$140). CTA no roteiro usa "quero" com texto do CTA 3 (misturado). |
| 19 | [Você não precisa de um nicho, você já é o nicho](https://app.notion.com/p/3e6243fe515681b79926da5cde80b35e) | Posicionamento | Contrarian sobre convenção | 13,2 (@douggrindstaff) | "E se eu te dissesse que você não precisa escolher um nicho de mercado, porque você mesmo já é o nicho?" | "4 horas por dia" encosta na zona 2; tom de guru de internet. |
| 20 | [13 lições de quem construiu uma empresa de R$2 bilhões do zero](https://app.notion.com/p/3e6243fe515681f1a2e0d134fe7ab374) | Posicionamento | Lista de aprendizados | 13,2 (@douggrindstaff) | "Ao longo da minha jornada empreendendo uma empresa do zero quase R$2 BILHÕES DE REIAS de faturamento anual, aprendi muitas lições importantes." | Numeração quebrada (pula a 8ª; chega a 14). Dado "5 x 16 pessoas" sem fonte. |

Leitura rápida: os mais limpos para gravar já são **#12 (método de decisão)**, **#18 (300 empresas)**, **#8 (The Coffee)** e **#11 (gap de responsabilidade)**. Os mais arriscados: #14 e #15 (notícia velha), #4, #5, #13 (zonas saturadas).

---

## 5. Produção: peças já gravadas disponíveis

Fonte: [base Produção](https://app.notion.com/p/cb2243fe515683f4a80d012b0c2ca5d3).

**Etapa Edição ou Agendado: nenhuma peça.** Não há vídeo gravado pronto para entrar na semana pela origem preferida da rotina (Produção > Corte > BigVu).

Contexto (não estão em Edição/Agendado, mas existem):

| Peça | Etapa | Plataformas | CTA | Data de gravação | Observação |
|---|---|---|---|---|---|
| [Por Trás das Marcas #3: Comfrt](https://app.notion.com/3d0243fe51568127a57dc792df48425d) | Aprovação Rony | IG Reels, TikTok, Shorts | sem CTA | 18/09/2026 | Tem data de gravação; etapa possivelmente desatualizada. Confirmar se foi gravado. |
| [Manuais Práticos de IA #3: o coach de 15 mil dólares](https://app.notion.com/3cd243fe5156812ab086f793ddc7946d) | Aprovação Rony | IG Reels, TikTok, Shorts | palavra-chave do e-mail | 18/09/2026 | Idem. |
| [Por Trás das Marcas Ep.3: Birkenstock](https://app.notion.com/3cd243fe5156816292f5e968b28b408b) | Aprovação Rony | IG Reels, TikTok, Shorts | sem CTA | 09/09/2026 | **Já publicado** em 05/10 (ver seção 6). Etapa desatualizada. |
| [Por Trás das Marcas #5: Como 1907](https://app.notion.com/3e9243fe515681b58937f912af2bd5bb) | Aprovação Rony | IG Reels, TikTok, Shorts | sem CTA | (vazio) | **Já publicado** em 30/09. |
| [Nike chutada do S&P 100](https://app.notion.com/3e9243fe5156812d99c5f60282ad28ba) | Aprovação Rony | IG Reels, TikTok, Shorts | comenta VENDAS | (vazio) | **Já publicado** em 01/10. |
| [Por Trás das Marcas: Patagonia (Ep. 7)](https://app.notion.com/3cb243fe51568131924dc984f5c3c777) | Gravação | IG Reels, TikTok, Shorts | (vazio) | (vazio) | Teleprompter pronto. |
| [Por Trás das Marcas: Whoop](https://app.notion.com/3ca243fe51568142a608c54ba54f18a9) | Gravação | IG Reels, TikTok, Shorts | (vazio) | (vazio) | Teleprompter pronto. Existe duplicata "WHOOP" em Aprovação Rony. |
| [Por Trás das Marcas #6: Sam Zemurray](https://app.notion.com/3ea243fe51568126a261f06670a93deb) | Aprovação Rony | IG Reels, TikTok, Shorts | (vazio) | (vazio) | Teleprompter pronto. |
| [5 mil que tatuariam o logo](https://app.notion.com/3ec243fe5156813cb569e904066e52a2) | Aprovação Rony | IG Reels, TikTok, Shorts | sem CTA | (vazio) | Criada em 01/10, a mais recente. |
| [O tabuleiro foi montado antes de você sentar](https://app.notion.com/3d2243fe5156818b84b0ca879f38b3ab) | Aprovação Rony | IG Reels, TikTok, Shorts | palavra-chave do e-mail | (vazio) | Estado x dono: checar veto A7 (política). |

Outras em Aprovação Rony: Rick Rubin (Ep.10), Pokémon (Ep.9), Steven Bartlett, WHOOP, Tamara Klink x Project Panama, MANUAL ABERTO #01 Rodrigo Noll.

---

## 6. O que JÁ saiu no @rony (Sandcastles, 27/09 a 10/10/2026)

Fonte: Sandcastles `get_channel_recap`, canal da2d77da-1d5d-472a-ac64-96af5e2e3caf, lookback 14 dias. Média do período: 27 vídeos, outlier 1,93x, 74.656 views médias, engajamento 1,04%.

Top 8 por views:

| Data | Título / assunto | Views | Outlier | Link |
|---|---|---|---|---|
| 07/10 | Pesquisas eleitorais erram (opinião política) | 337.786 | 8,9x | [reel](https://www.instagram.com/reel/DeMb8w7I9l0/) |
| 05/10 | Manual de negócios EP10: Birkenstock | 297.787 | 7,5x | [reel](https://www.instagram.com/reel/DeIXlMMJ9fq/) |
| 29/09 | Comenta "IA" (tier list de ferramentas de IA) | 255.883 | 6,7x | [reel](https://www.instagram.com/reel/Dd4_ADHQsAs/) |
| 30/09 | Manual de negócios EP8: Como 1907 | 144.165 | 3,6x | [reel](https://www.instagram.com/reel/Dd7hb-ipFHe/) |
| 03/10 | Manual de negócios EP9: Caio Amato (Oakley) | 104.588 | 2,6x | [reel](https://www.instagram.com/reel/DeDOZzThMHa/) |
| 08/10 | Comenta KIT (presente na DM) | 100.350 | 2,6x | [reel](https://www.instagram.com/reel/DeOtpXQPcBo/) |
| 01/10 | Nike fora do índice (falta de humildade) | 99.951 | 2,5x | [reel](https://www.instagram.com/reel/Dd-FuZDJCUs/) |
| 08/10 | Manual de negócios EP11: Edward Bernays | 91.310 | 2,4x | [reel](https://www.instagram.com/reel/DeQHkVdpHy_/) |

Também saíram (não repetir tema sem ângulo novo): Zara (10/10, 50.597), editor de vídeo 24h com IA (09/10, 73.256), As 6 Leis para destravar vendas (10/10, 19.123), Falácia do Porteiro (08/10, 10.758, 0,3x), AMN Aprovado/Melhorado/Novo (07/10, 27.359), Manual de IA EP4 Perplexity Computer (06/10, 18.174), atacado antes do varejo (06/10, 17.841), o que diferencia um bom empreendedor (05/10, 10.001), hidroponia em supermercado de Berlim (04/10, 42.568), Manual de IA EP3 NotebookLM (02/10, 44.476), retenção x primeira venda em e-commerce (02/10, 18.816), OpenAI Dots (30/09, 49.815), produto com promessa única (28/09, 48.412), mãe com 5 agentes de IA (28/09, 500), tier list de IA mais duas vezes (27/09, 58.959; 28/09, 50.686), consumismo como vazio (27/09, 22.403), Stone/Embaixadores (09/10, 14.030), futuro do varejo (09/10, 6.116).

Leituras:
- A série **Manual de negócios** (EP8 a EP11) é o que segura o canal: 4 dos 8 primeiros. Todos usam o molde "case + 3 princípios + comenta PALAVRA", que o acervo chama de **zona de saturação 3**. Funciona hoje, mas está no limite.
- O maior outlier do período (8,9x) é **político**. É veto permanente A7. Não replicar, não usar como referência.
- Tier list de IA saiu 3 vezes em 3 dias; o acervo já marca "listas de ferramentas de IA" como `[REPETIDO 6×]`. Fora desta semana.
- Pior desempenho: hooks em forma de pergunta genérica ("Tu já ouviu falar na falácia do porteiro?" 0,3x; "O que diferencia um bom empreendedor dos demais?" 0,3x).

---

## 7. Base de exclusão (Acervo BIGVU): resumo operacional

Fonte: [Acervo BIGVU: Base de exclusão](https://app.notion.com/p/36a243fe515682f8a87b815d3651dc6a) (1.170 roteiros, out/2023 a ago/2026).

### 7.1 Três zonas de saturação (corte automático salvo fato novo)
1. Funil ACP + comunidade antes do produto + founder botando a cara (12+ ocorrências).
2. Doing Nothing Club / agenda vazia / método 10-20-30 / trabalhar menos e melhor (12+).
3. Case de marca estrangeira dissecado em 3 pilares + "Ctrl C Ctrl V nessa ideia" + CTA de newsletter (formato mais usado do acervo).
Bônus: guru de internet (dezenas) e listas de "melhores ferramentas de IA" (6× entre abril e agosto de 2026).

### 7.2 Lacunas (onde está o ouro)
1. Fracasso próprio com nome, número e consequência. Já gravados: Pistol Birds/NFT (28/02/2026) e quebra do primeiro negócio na bolha pontocom (24/05/2026).
2. Conflito real entre sócios ou dentro da família (nunca uma cena de atrito).
Zero ocorrências: fraude/golpe/segurança da informação/continuidade; precificação dinâmica/capacidade ociosa; formação e sucessão de gente; Selic como janela de ação; recuperação judicial por porte de empresa.

### 7.3 Temas marcados repetidos (resumo)
- **IA ferramentas:** Jack Dorsey/Block, Claude para Pequenas Empresas, Claude Cowork/SaaSpocalypse, Obsidian + Claude, Perplexity Computer, Sandcastles, Medvi, Arcads, OpenClaw, Vekta, listas de ferramentas (6×).
- **IA teses:** "AI first fake", mapear processo antes da ferramenta, IA não gera desemprego/Jevons (último 05/08), dívida cognitiva, GEO e AEO, moat de ferramenta evapora (4×, prazos contraditórios), internet morta, bolha de IA ≠ pontocom.
- **Marca:** KitKat/limonada, Blank Street, P.T. Barnum/ModaFoque, cliente herói, colabs, Ralph Lauren, Track & Field/Dior, CazéTV, Kith, Represent (4×), Lululemon, Nike, Stanley/Liquid Death/RXBAR, nostalgia, escassez planejada/drop, ragebait (3×), Head of Storytelling (3×), Toguro/Cimed, 3% x 97%.
- **Negócios:** Funil ACP (12+), "não procure cliente pro produto", 4 formas de crescer, Oakberry, Naval e as 4 alavancas, Reserva Mini, wellness (12+), psicologia de vendas, MVI e CMV, micro-SaaS em 48h, cobrança a cada 4 semanas, Black Friday, retenção x aquisição, bootstrapping vs VC, TikTok Shop, newsletter como mídia própria, 1P=5P (6×).
- **Gestão:** redução de reportes, "vai pra rua vender" (4×), Sully/"foguete não dá ré", negócio na cabeça do dono, contratar no feeling (4×), faturar ≠ ganhar dinheiro, ritual dos 5 números, Chief Vassoura Officer (10+), 5 motivos de não entregar, Via Negativa/Munger, planejamento anual (3×), cliente furioso (3×).
- **Filosofia:** "faça o que é bom, não o que ama", Bandura, Herbert Simon, escrever 30min/dia (último 08/07), superestímulo/tempo de tela, extrato do tempo, Napoleon Hill farsante, solidão do dono, ostentação como medo, grama do vizinho, sorte é estatística (4×), Doing Nothing Club (12+), "rico é quem tem agenda vazia" (5+), 10/20/30 (10+), Hábitos Atômicos, detox de dopamina.
- **Brasil/macro:** taxa das blusinhas, fim da escala 6x1 (3×), complexo de vira-lata (3×), torcida japonesa. Eleição, candidato, partido e polarização: veto permanente.
- **Institucional:** guru de internet (dezenas), Banco Stone. Cuidado com a contradição Dia de Donos (imersão vs encontro de aplicação).

### 7.4 Números oficiais (padronizar)
18 anos à frente da Reserva · capital inicial R$3 mil · R$715 mi na venda em 2020; ~R$2 bi de faturamento em 2024 · Reserva Mini "centenas de milhões" · Reserva Ink 50 mil · aprendiz → mestre 500 anos · newsletter e 1P=5P: **a definir** (não citar número).

### 7.5 Bordões
**São dele:** "Fui!" (~85% dos roteiros) · "Calma, valente, calma" (~21%, **não passar disso numa mesma semana**) · "Pensa comigo" · "A verdade verdadeira é que" (~10%) · "Se liga nessa" · "Dito isso" · "Deixa eu desenhar pra você" · "E aqui tá o que eu prometi lá no começo" · "Resumão da ópera" · "Nasceu perfeito, nasceu tarde" · "Vendendo almoço pra pagar jantar" · "Foguete não dá ré" · "Prefiro segurar louco a empurrar burro" · "Confia no pai" · "Anota".
**Vocativos:** galera, turma, rapaziada, valente, irmão, meu caro, filhão.
**NÃO são dele (nunca usar):** "Sacou o jogo?" · "O óbvio tem que ser dito e desenhado" · "tarefa de casa" · "maré volta" · "D'us" (ele escreve Deus) · "alçada" como conceito central · "programa de gente" · "arbitragem" fora de contexto financeiro.
**Ritmo:** frase média de 12 palavras (mediana 10); 30% das frases com 6 palavras ou menos; um argumento por linha; sem emoji no roteiro.

---

## 8. Prompt Mestre: A3, A6, A7

Fonte: [Estrategista Digital: Prompt Mestre](https://app.notion.com/p/871243fe515683298af881fcbd703ca5) (v15.0, agosto 2026).

### 8.1 A3. Voz
- Marcadores verbais (usar naturalmente, não empilhar): "Pensa comigo," · "A verdade verdadeira é que" · "Se liga" · "Calma, valente, calma" · fecha com "Fui."
- Regras rígidas: português do Brasil; **sem travessão, nunca**; sem aspas na narração; prosa corrida pronta para teleprompter (só o hook pode ser fragmentado); frase curta, verbo forte, zero adjetivo de palestra motivacional; número concreto sempre que existir ("R$ 380 mil em três meses" existe, "muito dinheiro" não).
- Nunca: falar de riqueza como estilo de vida; posar de quem sabe tudo (erro próprio é ativo); atacar guru nominalmente (ataca o modelo); jargão corporativo importado sem tradução.

### 8.2 A6. Tese do comment-gate
Fato da página: o volume de comentários é determinado exclusivamente por CTA de comment-gate falado dentro do vídeo, com entregável concreto fora do vídeo. Provas: @forseth.ai (6,97%) e um Reel do @liamjohnston.ai (2,02%); demais sem gate falado: 0,02% a 0,49%. A variável real é o **isolamento do pedido**: carrossel da @manifestlikemom com 0,59 de razão comentário/curtida com gate só de texto no card final. Todo formato recomendado precisa de gate isolado, palavra-gatilho de uma palavra e entregável concreto.

**Os três CTAs (verbatim, nunca reescrever, nunca adaptar):**

**(1) MDD Negócios**

> A minha vida toda eu estudei pra antecipar tendência nos meus negócios, e isso me fez estar sempre um passo à frente e vender muito mais. Pra te ajudar a fazer a mesma coisa, toda semana eu mando um e-mail com um estudo como esse pra você ler e aplicar imediatamente no seu negócio e vender mais. Ao longo do ano são 52 ideias pra ler e aplicar na hora. Se você tiver interesse, comenta vendas que eu te mando o link. Fui.

**(2) MDD AI**

> Como eu sei que você tá afogado em opção de IA, toda semana eu mando um e-mail com um problema de negócio comum, um só, resolvido com IA. Um por semana, 52 por ano, pra aplicar na hora sem se entupir de informação que rouba sua atenção. Comenta quero que eu te mando o link. Fui!

**(3) Email do Rony**

> Toda semana eu mando um email pra uma lista de amigos com as minhas ideias e opiniões sobre os negócios e pessoas mais interessantes que encontro no mundo. Escreve [palavra do vídeo] nos comentários que eu te mando o link. Ah! E se botar de pé alguma dessas ideias, procura o papai que tenho interesse.

Mapeamento por território: T1 → CTA 1 · T2 → CTA 1 · T3 → CTA 2 · T4 → CTA 3.

(Nota de cópia: no Notion, o "[palavra do vídeo]" do CTA 3 aparece com colchetes escapados em Markdown; o texto acima é o mesmo sem os caracteres de escape.)

### 8.3 A7. Vetos permanentes
Nunca sugerir pauta com: política partidária, eleição, candidato, polarização · tragédia, morte, acidente ou crise humanitária como gancho · crítica nominal a pessoa física, concorrente ou ex-sócio · guru específico com nome e sobrenome · número, case ou dado sem confirmação em **duas fontes independentes** · setor financeiro concorrente da Stone · conselho jurídico, tributário ou de investimento como recomendação · fofoca, boato, "fontes dizem".
- Antialucinação: nunca inventar link, número, data ou nome de empresa; se não achou, escrever "não confirmado".
- Antirrepetição: consulta obrigatória à Base de exclusão; tema já gravado só com ângulo comprovadamente novo escrito na ficha.
- Voz: nunca inventar bordão (lista na seção 7.5).

---

## 9. Sandcastles: watchlist, últimos 7 dias

Fonte: `top_hooks` e `top_topics`, watchlist, lookback 7 dias, filtros padrão (≥ 25 mil views, ≥ 2% engajamento, ≥ 1,0x outlier). 30 vídeos.

### 9.1 Clusters de tema (top_topics)
1. **Autovalor, ferida e identidade (storytelling pessoal).** @garyvee "Define your self-worth..." 5.809.456 views, 306,7x ([link](https://www.instagram.com/reel/DeKUwIhjX0m/)); @charlie "Inside your deepest wound is your greatest gift" 2.005.563, 211,9x ([link](https://www.instagram.com/reel/DeNXvrNxowu/)); @rich_somers "Your Life Is Shorter Than You Think" 381.633, 242,9x ([link](https://www.instagram.com/reel/DeNU4sNJTZf/)).
2. **IA com caso real e erro sistêmico.** @vaibhavsisinty "A guitar just got a traffic fine" 546.006, 248,2x ([link](https://www.instagram.com/reel/DeKKJAbgqhS/)); @sebastien "Comment RED for the prompt" 442.784, 166,7x ([link](https://www.instagram.com/reel/DeMwEMQvxFE/)); @justyn.ai "Drop EDIT below" 354.987, 31,4x ([link](https://www.instagram.com/reel/DeUUFJQu8cw/)); @thevarunmayya Ben Affleck e Python 1.731.242, 8,7x ([link](https://www.instagram.com/reel/DePZYzRzsoh/)).
3. **Vendas x marketing e valor do tempo do dono.** @garyvee "Sales is [negative] when you can't [market]" 615.262, 31,6x ([link](https://www.instagram.com/reel/DeHP5XuuTI8/)); @leilahormozi "making money vs duplicating money" 1.302.568, 16,9x ([link](https://www.instagram.com/reel/DePMTk0jCjk/)); @rich_somers "Real Sales People Thrive Under Pressure" 28.628, 18,3x ([link](https://www.instagram.com/reel/DeIgg9xgF_F/)).
4. **Comunicação e marketing decodificado.** @jen_gottlieb sound bites 998.947, 27,4x ([link](https://www.instagram.com/reel/DeMT3_ZhWBZ/)); @itssavannahjordan breakdown de marketing 62.500, 50,8x ([link](https://tiktok.com/@itssavannahjordan/video/7693311164561771790)); @danielpink reuniões 197.104, 14,0x ([link](https://www.instagram.com/reel/DeHj9EmM8Gz/)).

### 9.2 Padrões de hook (top_hooks, categorias e madlibs)
- **Contrarian** é a categoria mais frequente (8 dos 30). Madlibs: "Sales is [negative activity] when you can't [core business function]." (31,6x) · "Your life is [adjective] than you think. [Number/Percentage] of my life is already [state]." (242,9x) · "[Topic] are the most underrated [medium/category]..." (24,7x).
- **Personal experience** lidera em outlier: "I come back to this [type of content] when I [state of mind]." (306,7x) · "There was [noun] I liked..." (211,9x).
- **Problem com caso absurdo**: "[Location]'s [System] [Action] [Subject] for [Outlier event]." (248,2x) · "You're probably [common professional action] wrong." (14,0x).
- **Secret reveal com gate de palavra**: "I didn't do [painful, common task] in this [content type]. [Tool/Entity] did." (31,4x, com "Drop EDIT below").
- Observação: o Sandcastles não devolve a frase falada literal dos vídeos de terceiros, só o madlib. Por isso a tabela da seção 10 usa os hooks literais dos vídeos do próprio @rony, onde a frase está disponível.

---

## 10. Hooks vencedores lado a lado

Frase literal dos 3 primeiros segundos quando a fonte a fornece. Quando a fonte só traz madlib ou exemplo adaptado, está indicado.

| Frase dos 3 primeiros segundos | Por que funcionou | Número / fonte |
|---|---|---|
| "A sandália mais feia do mundo tem os donos mais cabeça-duras do mundo!" (literal, @rony) | Contradição dupla (feio + teimoso) sobre marca famosa; promete explicar um paradoxo. | 297.787 views, 7,5x · Sandcastles recap · [reel](https://www.instagram.com/reel/DeIXlMMJ9fq/) |
| "Tá pra usar, bom, ou perda de tempo?" (literal, @rony) | Formato tier list com veredito; gate "IA". **Tema saturado (listas de IA 6×)**: não repetir. | 255.883 views, 6,7x · [reel](https://www.instagram.com/reel/Dd4_ADHQsAs/) |
| "Esse time de futebol anunciou para o mundo inteiro que não tem meta de ganhar campeonatos." (literal, @rony) | Contradição de expectativa sobre um objeto com atenção própria (futebol). | 144.165 views, 3,6x · [reel](https://www.instagram.com/reel/Dd7hb-ipFHe/) |
| "Esse moleque se tornou um sucesso, porque pesava 150 kg aos 12 anos e viu a empresa da família falir." (literal, @rony) | Número específico e improvável + confissão de custo (padrões 1 e 8). | 104.588 views, 2,6x · [reel](https://www.instagram.com/reel/DeDOZzThMHa/) |
| "A Nike está valendo 77% a menos do que valia há poucos anos atrás e acabou de ser retirada da lista das 100 maiores empresas da bolsa americana." (literal, @rony) | Número de perda + marca gigante + notícia fresca. | 99.951 views, 2,5x · [reel](https://www.instagram.com/reel/Dd-FuZDJCUs/) |
| "O café da manhã mais famoso do mundo, bacon com ovos, virou um hábito nos Estados Unidos por causa de uma carta enviada pra cinco mil médicos." (literal, @rony) | Hábito familiar com causa oculta e número específico. | 91.310 views, 2,4x · [reel](https://www.instagram.com/reel/DeQHkVdpHy_/) |
| "Cinco mil reais. Era isso que a gente tinha." (exemplo verbatim do padrão) | Número exato soa vivido. Padrão "Testado e funcionou". **Corrigir para R$3 mil** (padrão oficial). | sem número · [Padrão](https://app.notion.com/p/e66243fe515683b0b4e501e510063bef) |
| "Cliente sumiu depois do orçamento. Isso não é falta de sorte, é falha de processo." (exemplo da base, voz Rony) | Dor nomeada em 3s + virada; casa com gate isolado. | Formato: outlier 89,9, 156.269 views, score 95 · [ficha](https://app.notion.com/3e2243fe51568197b34fdf2401f477fe) |
| "Eu não tenho regra de horário pra ninguém aqui. Metade dos donos que tão me vendo vai achar que eu tô errado." (exemplo da base, voz Rony) | Regra impopular em primeira pessoa com reação do público embutida. | Formato: outlier 468,6, 4.812.296 views, score 85 · [ficha](https://app.notion.com/3ed243fe5156816e8a00cda71a00188c) |
| "Your life is [adjective] than you think. [Number/Percentage] of my life is already [state]." (madlib, @rich_somers) | Urgência pessoal com número; contrarian. | 381.633 views, 242,9x · [Sandcastles](https://app.sandcastles.ai/video/59a50354-707a-4a4d-ac77-257b94ed2449?from=mcp) |
| "[Location]'s [System] [Action] [Subject] for [Outlier event]." (madlib; título: "A guitar just got a traffic fine") | Caso absurdo e concreto de IA errando; curiosidade imediata. | 546.006 views, 248,2x · [reel](https://www.instagram.com/reel/DeKKJAbgqhS/) |
| "Sales is [negative activity] when you can't [core business function]." (madlib, @garyvee) | Contrarian curto sobre vendas x marketing; gate "Podcast". | 615.262 views, 31,6x · [reel](https://www.instagram.com/reel/DeHP5XuuTI8/) |

Contraexemplos do próprio canal (não repetir o molde): "Tu já ouviu falar na falácia do porteiro?" 10.758 views, 0,3x · "O que diferencia um bom empreendedor dos demais?" 10.001 views, 0,3x · "Organizar isso custaria 100k mas me custou apenas R$100 com essa IA." 18.174 views, 0,5x · "Eu sempre parti de uma cópia para inovar nos meus negócios. Calma, valente, calma." 27.359 views, 0,7x.

Proibido como referência: "Pessoal, tenho lido nos jornais, né, uma discussão gigantesca sobre o porquê as pesquisas eleitorais erram tanto, tá?" (337.786 views, 8,9x). Veto A7.

---

## 11. Síntese para a geração da semana

1. **Formato prioritário:** Gate Isolado com Entregável Nomeado (score 95, 3ª semana na lista, sai se não for usado).
2. **Formato de maior teto:** Regra Que Eu Não Tenho (outlier 468,6, 4,8 mi de views) com ajuste de gate.
3. **Hook próprio mais forte recente:** contradição sobre marca famosa (Birkenstock 7,5x), mas o molde "case estrangeiro + 3 princípios" é zona 3. Usar a contradição com case brasileiro ou prova própria.
4. **Pautas de maior valor:** Sociedade (lacuna nº 2) e Grupo Estrela (lacuna recuperação judicial), ambas já ligadas a Produção.
5. **BigVu mais limpos:** #12 método de decisão, #18 300 empresas, #8 The Coffee, #11 gap de responsabilidade.
6. **Evitar:** listas/tier list de IA, wellness, case estrangeiro em 3 pilares, Chief Vassoura Officer, retenção x aquisição, notícias velhas de IA (#14, #15), qualquer coisa eleitoral.
7. **Gargalo:** não há peça em Edição ou Agendado. Toda saída de vídeo da semana depende de gravação nova ou de corte de podcast. Vale checar com o Michel se Comfrt e Manuais de IA #3 (data de gravação 18/09) já estão gravados.
