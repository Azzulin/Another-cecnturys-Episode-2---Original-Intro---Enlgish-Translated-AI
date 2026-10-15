# Plano de trabalho: tradução das operações de Another Century's Episode 2 (PS2) para o inglês

Este documento é para o **agente tradutor**. Seu único trabalho é traduzir: preencher os campos `"en"`, `"notes"` e
`report` dos lotes, um lote por vez, seguindo estas regras.

Um revisor valida cada entrega com um programa, revisa o sentido e é o único que insere o texto no jogo. Entregas fora
das regras voltam com um relatório.

## 0. O que você NÃO faz (proibido)

- Não roda nenhum script nem ferramenta do projeto (`tools/`, `.venv`, `python`...).
- Não gera, altera nem testa ISO, e não mexe em `work/output/`.
- Não edita nada fora de `work/translation/agent/returns/`. Isso inclui:
  - `work/translation/en/` e `_fill/`;
  - o glossário e os `docs/` (CHANGELOG incluído);
  - os próprios lotes em `batches/`;
  - este plano.
- Não "aplica", "mescla", "integra" nem "valida" a tradução. Isso é trabalho do revisor.

Uma entrega que mexa em qualquer coisa além de `returns/<LOTE>.json` é descartada inteira.

Antes de começar, leia nesta ordem:

1. Este arquivo.
2. [INDICE.md](INDICE.md): enredo de cada operação, facções, tom e voz de cada série e personagem, pistas de
   contexto e pontos sensíveis (spoilers, gênero ambíguo).
3. [GLOSSARIO.md](GLOSSARIO.md): nomes de personagens, mechas, naves, facções e termos de cada série, com gênero e
   papel. O bloco `glossary` de cada lote traz os itens daquele lote.
4. [examples/op01.json](examples/op01.json): a Operação 01, já traduzida e testada no jogo. É o padrão de tom, de
   tamanho e de uso dos códigos.
5. [LOTES.md](LOTES.md): a lista de lotes, na ordem de trabalho.

---

## 1. Escopo e ordem

- **Lotes:** `op02_01` … `op28_04`. Cada um tem até 80 linhas seguidas de uma operação, na ordem em que o jogador as
  vê:
  1. briefing estratégico;
  2. para cada fase, o briefing tático e o diálogo da missão;
  3. debriefing;
  4. relatórios.

  Os campos `layer` e `phase` de cada linha dizem onde você está.
- **Um lote por entrega**, em ordem. Antes de traduzir o lote N, releia os lotes anteriores já entregues da mesma
  operação, para manter a continuidade: quem está presente, o que aconteceu e como cada personagem fala.
- **Contexto:** `context_before` e `context_after` trazem as linhas vizinhas, só para leitura. Você também pode abrir
  o lote anterior e o seguinte em `batches/` (`previous_batch` / `next_batch`).

## 2. Formato de entrada e de saída

1. Copie `batches/<LOTE>.json` para `returns/<LOTE>.json`.
2. Em `returns/<LOTE>.json`, preencha **apenas**:
   - `"en"` de cada linha;
   - `"notes"` (opcional, por linha): dúvida, falante inferido, desempate que você teve de fazer;
   - o bloco `report`:
     - `translator_summary`: 2 a 5 frases sobre o lote, os falantes que você identificou e as dúvidas;
     - `rows_examined` e `rows_examined_count`: o que você de fato leu, incluindo contexto e lotes vizinhos;
     - `uncertainties`: toda decisão incerta, **mesmo quando a linha parece correta**;
     - `glossary_proposals`: nome ou termo que aparece nas suas linhas e falta em `glossary`, no formato
       `{"ja", "en", "kind", "gender" (só personagens), "sources": [URL], "note"}`. Use a grafia do título da página na
       wiki da série;
     - `portrait_speakers`: para cada número em `unknown_portraits`, quem fala e a evidência.
3. Não altere `ref`, `layer`, `phase`, `portrait`, `opens_new_window`, `tokens`, `jp_lines`, `max_lines`,
   `max_line_px`, `max_line_chars_approx`, `jp`, nem os blocos do topo. Não acrescente, remova ou reordene linhas.
4. O arquivo final precisa ser JSON válido em UTF-8, com quebras de linha escritas como `\n` dentro das strings.

## 3. Regras técnicas (bloqueantes: o validador rejeita a linha)

1. **Códigos de controle.** A lista `tokens` de cada linha é a sequência exata de códigos do japonês. A tradução
   precisa conter **a mesma sequência, na mesma ordem e escrita igual**. Não invente códigos.

   | Código | Função |
   |---|---|
   | `<op()>` … `<ed()>` | Abre e fecha a fala rápida da missão. Uma linha sem `<op()>` continua a fala anterior. |
   | `<on()>` … `<off()>` | Abre e fecha a janela de comunicação. |
   | `<op(N,1)>` | Retrato N no briefing. `known_portraits` diz quem é. |
   | `<sp(N)>` | Velocidade do texto. Fica no início. |
   | `<ab(N)>` | Pausa no fim da fala. `<ab(0)>` significa que a frase continua na próxima linha. |
   | `<im(N)>`, `<tr(N)>`, `<of(N)>`, `<ac(N)>` | Imagem e efeitos do briefing. Ficam num ponto equivalente da frase. |
   | `#c[RRGGBB]` … `#c` | Cor. Fica em volta das palavras em inglês que correspondem às palavras coloridas no japonês. |
   | `%d`, `%s` | Valores inseridos pelo jogo. |
   | `％` depois de `%d` | Sinal de porcentagem literal de largura total. Mantenha `%d％`, nunca `%d%%`. |
   | `○ × △ □ ① … ⑳ ㊤ ㊦ ㊧ ㊨` | Ícones de botão. Mantenha o símbolo ("Press the △ button"). |

   Exemplo (Op 01): `#c[BE5050]ジオン残党<im(2)>#cは、` virou `The #c[BE5050]Zeon remnants<im(2)>#c took...`.
2. **Linhas.**
   - `\n` é uma quebra manual.
   - O número de linhas não pode passar de `max_lines`: 2 na fala de missão e 3 no briefing, que é o máximo que as
     janelas do jogo mostram.
   - Nenhuma linha pode passar de `max_line_px`, que é medido com a fonte real. Guia prático: `max_line_chars_approx`
     caracteres por linha (cerca de 38 na missão e 43 no briefing).
   - Se a frase não couber, reescreva de forma mais compacta. Abreviações são bem-vindas (Lt., Capt., HQ, MS).
     **Nunca corte o fim da frase nem uma parte do sentido.** Se não houver jeito, traduza inteira e explique em
     `notes`.
3. **Caracteres.**
   - Use só ASCII imprimível, mais os ícones e o `％` que já existirem no japonês.
   - Proibidos:
     - aspas curvas;
     - travessão;
     - o caractere `…` (escreva `...`);
     - acentos;
     - japonês;
     - letras e dígitos de largura total (`０２` vira `02`; `ＵＣＥ` vira `UCE`);
     - `# $ @ [ \ ] ^ _ { | } ~ ; * =`, que faltam em algumas fontes (o `#` é o marcador de cor).
   - `「」` e `『』` viram `"`.
   - Sem espaço duplo e sem espaço no começo ou no fim da linha.
   - A única exceção são os espaços largos que alinham a assinatura dos relatórios: copie o layout dos relatórios de
     `examples/op01.json`.
4. **Glossário.** Todo nome do bloco `glossary` que aparece no japonês da linha tem de aparecer em inglês exatamente
   como no glossário (`en`, ou `en_short` na fala). Os nomes em `do_not_touch_names` são fixados por script: escreva
   exatamente assim.
5. **Linhas repetidas.** As linhas que já foram traduzidas ou que se repetem não vêm nos lotes. Não é preciso
   procurá-las.

## 4. Estilo

- **Fidelidade dramática.** É um crossover de várias séries de robôs:
  - Gundam 0083, Wing e G Gundam;
  - Macross DYRL;
  - Dragonar;
  - Dunbine;
  - L-Gaim;
  - Layzner;
  - Brain Powerd;
  - Nadesico;
  - os pilotos originais Tak Kepford e Marina Carson (Gun Ark).

  Cada personagem mantém a voz da obra: siga a tabela "Tom e voz por série" do INDICE e os campos `gender`,
  `role` e `personality` do glossário. Não simplifique e não deixe o texto genérico.
- **Terminologia de cada série.** Use os termos próprios de cada obra como estão no GLOSSARIO: Aura Battler,
  Valkyrie, Heavy Metal, SPT, Metal Armor, Aestivalis, Antibody, Protoculture... Não os troque por palavras
  genéricas ("robot", "mech").
- **Registro militar natural.** Ordens curtas e imperativas, relatórios objetivos. Use contrações na fala e evite-as
  em relatórios formais.
- **Gênero.** Não deduza pelo nome. Se o texto não estabelece quem é a pessoa, use forma neutra ("they", "that pilot").
- **Falante e destinatário.** Leia as linhas dos dois lados antes de decidir. A linha sozinha muitas vezes permite
  leituras opostas, e a resposta duas linhas depois costuma resolver. Pistas de fala: 俺/僕/私/あたし, わ/よ/のよ,
  だ/です.
- **Não invente o que o japonês omite.** Quando a cena não diz quem age, prefira uma construção que mantenha a
  ambiguidade (passiva, imperativo) a inventar "I" ou "we".
- **Frase dividida em duas linhas continua dividida.** Duas linhas em inglês que se leem como uma frase, cada uma com
  seus códigos.
- **Sem notas no texto.** Nada de parênteses explicativos, gírias atuais ou memes. A única exceção são as linhas de
  rascunho do desenvolvedor marcadas com `※`, que podem ficar descritas entre parênteses.
- **Tratamentos.**
  - 少尉 = Ensign;
  - 中尉 = Lieutenant (Lt.);
  - 大尉 = Captain (Capt.);
  - 少佐 = Major;
  - 准将 = Commodore;
  - 艦長 = Captain;
  - ちゃん/さん não viram "-chan"/"-san": use o nome ou um tratamento em inglês.
- **Use os exemplos como referência, não como cópia.** Leia em `examples/op01.json` como uma forma parecida foi
  resolvida e então traduza a sua linha.

## 5. Checklist antes de entregar

- [ ] Todas as linhas têm `en` preenchido.
- [ ] Em cada linha, a sequência de códigos é igual à lista `tokens`.
- [ ] Nenhuma linha passa de `max_lines`, e todas cabem na regra prática de `max_line_chars_approx`.
- [ ] Não há caracteres proibidos, espaço duplo nem espaço no começo ou no fim da linha.
- [ ] Os nomes seguem o glossário.
- [ ] O `report` está preenchido, com `translator_summary` e as incertezas.
- [ ] Você alterou **somente** `returns/<LOTE>.json`.

## 6. Depois da entrega

O revisor roda o validador e grava `validation/<LOTE>.md`.

- **APROVADO:** o revisor revisa o sentido, aplica e libera o próximo lote. As correções do revisor ficam registradas
  à parte (`reviewer_fixes.json`). Sua entrega não é editada.
- **REJEITADO:** corrija só as linhas citadas, no próprio `returns/<LOTE>.json`, e entregue de novo.

## 7. Lotes fora das operações (`xa`, `xb`, `xc`, `xd`, `xm_*`)

Mesmo formato, mesmas regras técnicas e mesmo checklist. O campo `group_label` diz o que é cada grupo.

| Grupo | Conteúdo | Atenção |
|---|---|---|
| `xa` | Missões extras (Nadesico B, Ra Cailum/Bright, White Fang...) | Diálogo de missão comum: vozes conforme o INDICE. |
| `xb` | Tutorial / manual em jogo | Tom instrutivo e claro. Vocabulário de sistema conforme o GLOSSARIO (Ace Points, Module, Free Mission, Combo, Sub Combo, Lock-on, Dash, vernier...). Ícones de botão com "button" ("Press the △ button"). |
| `xc` | Flashbacks Tak × Marina (054–057) | Spoiler: traduza exatamente o que o texto diz. Tak e Marina mais jovens, ainda em treinamento. |
| `xd` | Missões curtas e de sistema | Muitas são linhas soltas; leia o contexto antes. |
| `xm_menuNNNN` | Uma tela de menu cada (inclui a enciclopédia, `menu3019`, e as mensagens privadas, `menu3029`) | Rótulos curtos e consistentes entre telas. Textos de enciclopédia em tom enciclopédico, terceira pessoa, sem contrações. As mensagens privadas são cartas pessoais (Barkholz, Nina, Inez...): tom de cada um, e spoilers como no texto. |

**Largura nos menus:** as caixas dos menus ainda não foram medidas. `max_line_px` é provisório (a maior linha
japonesa da tela). Traduza sempre o sentido completo dentro de `max_lines`; se não couber na largura, compacte o que
for possível e explique em `notes`. O revisor ajusta o layout quando as telas forem medidas. Nunca corte o sentido
para caber.
