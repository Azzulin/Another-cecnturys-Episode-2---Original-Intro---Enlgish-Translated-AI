# Changelog

## Repositório público — 2026-10-15 (sem build nova)

- Documentação em inglês para o GitHub: `README.md`, `CHANGELOG.md` (raiz, em inglês) e `docs/INSTALL_PATCH.md`,
  `GLORIOUS_OPENING.md`, `BUILD_FROM_SOURCE.md`, `MAKE_YOUR_OWN_TRANSLATION.md`, `AI_TRANSLATION_WORKFLOW.md`,
  `TECHNICAL_REFERENCE.md`, `RELEASING.md`, `STATUS.md`. `.gitignore` exclui ISOs, `.PSS`, `.xdelta`, `.venv` e as
  quarentenas (uma tem uma ISO de 3,5 GB).
- `tools/ace2/swap_movie.py`: troca o `MOVIE001.PSS` de uma imagem pelo de outra, no mesmo lugar (os dois têm
  275.251.204 bytes), e confere o resultado. Só biblioteca padrão, para o jogador rodar sem o ambiente. Testado com
  as ISOs reais: SVV japonesa + Glorious, 0.0.10 `--svv-opening` + Glorious = SHA da 0.0.10, e a volta.
- `tools/ace2/make_patch.py`: xdelta da SVV intacta para a build **com a abertura da SVV recolocada** (o patch não
  carrega o filme de 2006), decodificação de conferência, SHA da versão Glorious recalculado e
  `work/release/ACE2-EN-<v>-SHA256.txt`. Rodado com o xdelta3 3.0.11 oficial (jmacd/xdelta-gpl): patch da 0.0.10 com
  454.701 bytes; saída com a abertura da SVV `60227c82…a2aa` (igual à build `--svv-opening` feita à parte); com o
  `swap_movie.py` e o disco de 2006, `3e8c6143…8c12` (a 0.0.10 auditada). Publicado como pre-release `v0.0.10` no
  GitHub.
- `build.py --svv-opening` e `audit_iso.py --svv-opening`: build sem o disco de 2006 (para usuários). O padrão
  continua sendo a abertura "Glorious".
- `fonts.py`: pasta das TTF configurável por `ACE2_FONTS` (padrão `C:\Windows\Fonts`).
- Ambiente desta máquina conferido: `build.py --version 0.0.10 --write` reproduziu o SHA-256
  `3e8c6143…8c12`.

## 0.0.10 — 2026-10-09 (teste interno)

- Primeiro teste no PCSX2 desde a 0.0.1 (feito com a 0.0.9). Achados:
  - **Rótulos de menu somem por inteiro acima de ~141 px** (fonte de menu): tudo até 141 px aparece ("Flight
    Reverse", "Invert Y-Axis", "Encyclopedia"); tudo a partir de 154 px fica em branco ("Return to Menu",
    "Controller Type", "Camera Priority", "Reset to Defaults", "Auto Altitude Adjustment"). Não é limite de bytes
    ("Flight Reverse" e "Return to Menu" têm 14). Os lotes de menu tinham saído com `max_line_px` 350.
  - **Crash ao pausar no meio da missão** (o log do PCSX2 não registra nada). Suspeita: o mesmo tipo de limite, sem a
    proteção que os menus têm. Não confirmado.
- Menus (correção em `reviewer_fixes.json`; as cópias herdam pela repetição automática):
  - `menu3004#15` "Back to Menu" (também `menu3040#11`, `menu3054#7`);
  - `menu3070#8` "Defaults" (também `menu3071#10`, `3072#8`, `3073#5`, `3076#7`);
  - Target: "Camera" / "Facing" / "Distance" / "Damage" (`menu3070#14-17`);
  - Controller: "Control Type", "Camera", "Auto Altitude" (`menu3071#3/5/8`).
- Menu de pausa (`hud3013`): cada item ficou dentro da largura do japonês. "Resume", "Commands", "To Intermission",
  "To Free Mission", "To Versus Menu", "1P/2P Commands"; barra "Select:㊤㊦　Exit:⑪　OK:○" (241 px, JP 245); ajuda
  "Restart the mission from the start.", "Review 1P's/2P's abilities and commands."; faixa "Mission Complete"
  (168 px, JP de faixa até 191).
- `merge_fill.py` quebrava no console do Windows ao imprimir "①" (`UnicodeEncodeError`) e deixava parte das tabelas
  sem mesclar. Rodar com `PYTHONIOENCODING=utf-8`.
- 389 recursos alterados; `audit_iso.py` passou (SHA-256
  `3e8c61433aab58bafa3fb0ff6c0f55d95c63d8eefde1be441d8737be5d578c12`).
- Para continuar em outra máquina: `docs/RETOMADA.md` (o que copiar, `requirements.txt`, fontes, SHA de referência,
  o que estava só na memória do Claude). Nova ferramenta de pesquisa: `tools/research/label_widths.py`.

## 0.0.9 — 2026-10-08 (teste interno)

- **Todo o texto das tabelas do jogo em inglês**: campanha 6.822/6.822, menus 2.171/2.171, missões extras 457,
  tutorial 628, flashbacks 122, missões curtas 142, HUD, nomes e janelas do sistema. Os 150 lotes do agente estão
  aplicados.
- Extras revisados (mesmo ciclo das operações; cada proposta lida aqui antes de entrar): `xa` 76 correções,
  `xb`+`xd` 107, `xc` + menus 3000–3018 92, enciclopédia e menus 3019–3029 121, menus 3032–3057 110, menus
  3061–3077 121.
  - Enciclopédia (`menu3019`, 69 verbetes) e mensagens privadas (`menu3029`, 19 cartas) **retraduzidas por inteiro**:
    o agente resumiu, cortou parágrafos e inventou conteúdo (carta de Nina virou autoapresentação, Barkholz
    "fundador" do Design Bureau, Poseidal "com mão de ferro").
  - Linhas deslocadas (`m6006#23-25`, `m6302#140/141`), condições de falha traduzidas como ordem
    ("Destroy allied Aries"), falante errado nos flashbacks (`m6322#13`, `m6324#20`).
  - Botões: `決定` = "OK" (como `common`/`hud3013`), separadores com o espaço largo do japonês; `対戦` = Versus.
- Pipeline:
  - `validate_return.py --auto` reaplica as linhas automáticas de todos os grupos (172 linhas que ficavam de fora:
    `menu3023` e `menu3074` não têm lote, e cópias de linhas preenchidas depois do próprio grupo);
  - `agent/width_waivers.json`: dispensa registrada de largura provisória de menu (só `menu3077#54`, onde os dois
    nomes do glossário já ocupam o limite);
  - overrides novos em `auto/overrides.json`: `menu3002#3` "Recovery Dev.", `menu3013#5` "Player Unit".
- `merge_fill` lista 142 linhas WIDE (mais largas que a maior linha japonesa da tabela), quase todas nos objetivos
  copiados para `menu3055`/`menu3056`: `work/ui/wide_0.0.9.txt`. Conferir no jogo.
- 389 recursos alterados; `audit_iso.py` passou (SHA-256
  `3ec584ee6a6490687cf3671a144f20b48ef67dba7b88e7708cd14e65d8076da0`).

## 0.0.8 — 2026-10-08 (teste interno)

- **Campanha completa: Ops 01–28, 6.822 de 6.822 linhas de enredo.** Novas nesta build: Ops 22–28.
- O agente devolveu os 150 lotes. A única coisa fora de `returns/` foi um script dele (`apply_op23_02.ps1`), movido
  para `agent/_quarentena_google_0.0.8/`.
- Op 22: o agente "consertou" a linha extra de `op22_04` copiando o japonês e a tradução de `m6223#38` para a
  `m6223#37`. A linha foi retraduzida pelo revisor (`reviewer_fixes.json`) em vez de voltar ao agente.
- Revisão de sentido em paralelo (3 revisores para as Ops 23–28), com cada proposta lida aqui antes de entrar:
  Op 22 2, Ops 23–24 67, Op 25 204, Ops 26–28 94 correções. Problemas típicos: sentido invertido
  (`brief63300#3` "zero damage confirmed", `m6252#13`, `m6272#15`), hipóteses viradas em fato, nomes que passavam
  pelo validador só por um pedaço (Golaon, Baron Zu, Will Wips, Quincy Isser), "戦域" = airspace, frases de
  relatório truncadas, falas sem contração.
- Créditos (`m6285`): mojibake `ã€€` (espaço largo gravado como cp1252) consertado em 1.436 lugares; cargos em
  inglês, nomes em Hepburn com vogais longas, BANPRESTO/FromSoftware/Sunrise; "五十音順" = Japanese kana order.
- Pipeline:
  - `validate_return.py --all` e `review_returns.py` agora pegam todos os lotes (antes só `op*`, os extras ficavam
    de fora);
  - `merge_fill.widths` não quebra mais com caractere fora do cp932 (o validador o reporta como erro);
  - `#i…#i` (nomes de patente em `menu3001`) é código de controle (`textdb.TOKEN` e os `STRIP`);
  - uma linha reescrita pelo revisor ignora campos congelados alterados na entrega (vira aviso), como na `op22_04`.
- 339 recursos alterados; `audit_iso.py` passou (SHA-256
  `8326913d37c982445b9e0b3fe6ac73ef69cc4cb1145950dc49cd0ad215626401`).

### Preparação (sessão anterior)

- Lotes para o texto fora das 28 operações (`batches.py make --extras`), no mesmo formato, com o mesmo validador e
  as mesmas regras. São 57 lotes e 4.108 linhas:
  - `xa`: missões extras (6 lotes);
  - `xb`: tutorial (4);
  - `xc`: flashbacks Tak × Marina (2);
  - `xd`: missões curtas e de sistema (2);
  - `xm_menuNNNN`: telas de menu, enciclopédia e mensagens (43).
- Os grupos extras ganharam linhas automáticas próprias (`auto/<grupo>.json`) e congelamento por `hand`. O
  validador acha as linhas automáticas pelo nome do grupo do lote.
- Entregues ao agente: Ops 23–28 (22 lotes) e os 57 lotes extras. A Op 22 aguarda 2 consertos estruturais.
- Documentação para continuar em outra sessão: ESTUDO, seção 8 (reescrita) e `docs/REVISAO_PARALELA.md` (prompt
  dos revisores).

## 0.0.7 — 2026-10-08 (teste interno)

- **Operações 09 a 21 completas** (3.164 linhas). Com as Ops 01–08, são 4.832 de 6.822 linhas de enredo aplicadas.
- Revisão de sentido feita por três revisores em paralelo (Ops 09–13, 14–18, 19–22). Cada proposta foi lida e
  aceita aqui antes de entrar em `agent/reviewer_fixes.json`, e conferida por `tools/ace2/check_fixes.py`
  (novo: testa propostas sem gravar nada).
  - 348 correções: 95 nas Ops 09–13, 130 nas Ops 14–18 e 123 nas Ops 19–22.
  - Problemas típicos:
    - hipóteses (らしい, ようだ, であろう, 推測される) viradas em fato;
    - insultos inventados ("bastards", "scum", "half-breed", "fools", "runts");
    - orações perdidas (軍務に復帰, 軍属, 建造中, 人質をとって);
    - termos errados (犯行声明 = claim of responsibility; 戦略的 = strategic; 誤射 ≠ misfire);
    - frases divididas quebradas;
    - falas sem contração;
    - "-chan"/"-san" em romaji;
    - "he" para pilotos ainda não identificados.
- Pipeline:
  - `％` largo: um `%` ASCII solto vira início de conversão de printf. 7 linhas corrigidas, uma delas já na 0.0.6
    (6082#29). O validador agora barra `%` solto.
  - Objetivos divididos em duas linhas (…を / 掃討する) recebiam a cópia automática de outra operação ("military
    units"). Novo `work/translation/auto/overrides.json` dá inglês próprio a essas linhas (Ops 14, 18 e 22).
- Decisão provisória: 地上人 = "Upper Earthling" (Dunbine).
- Op 22 fica para a próxima build: o agente acrescentou uma linha a `op22_04` e alterou um campo `phase` em
  `op22_02`; a correção já foi pedida.
- 286 recursos alterados; `audit_iso.py` passou (SHA-256
  `a1853fe7ceec93aeaecdfb1ae21c654573239df5875955bfca7003247b94c366`).

## 0.0.6 — 2026-10-07 (teste interno)

- **Operações 03 a 08 completas**, em todas as camadas (1.221 linhas):
  - Op03 Novis Noah;
  - Op04 Kimbareid;
  - Op05 Guardian;
  - Op06 Konpei Island;
  - Op07 La Vie en Rose;
  - Op08 Interception Limit.
  Junto com as Ops 01 e 02, são 1.668 linhas de enredo aplicadas.
- Tradução do agente externo, validada (`validate_return.py`) e revisada linha a linha aqui: 56 correções em
  `agent/reviewer_fixes.json`.
  - Op03: 7. Op04: 7. Op05: 10. Op06: 10. Op07: 5. Op08: 17.
  - Erros de sentido corrigidos, entre outros:
    - objetivo dividido em duas linhas traduzido como dois objetivos soltos (63005#2/#3);
    - 星の屑 = Operation Stardust;
    - hipótese que virou afirmação (63216#4);
    - "Amuro Rei" (6082#36);
    - "that guy" para a piloto ainda não revelada (6032#31);
    - frases de relatório truncadas (63205#1, 63212#3/#5, 63213#6);
    - insultos acrescentados ("scum", "bastard", "fools");
    - Kou e Nina sem contrações.
- Bug do glossário corrigido:
  - レイ (Rei, o computador da Layzner) casava dentro de アムロ・レイ e ia para o glossário do lote. Foi isso que
    levou o agente a escrever "Amuro Rei".
  - Agora um nome do glossário dentro de um nome mais longo não conta (`validate_return.longer_keys`), tanto na
    validação quanto na geração dos lotes.
  - Nova regra em `name_fixes.json`: "Amuro Rei" → "Amuro Ray".
- 195 recursos alterados; `audit_iso.py` passou (SHA-256
  `874de9a95ad6bd03412e618e584f8a2da3a82d28ecb7823c6ac77466d6c99bff`).

## 0.0.5 — 2026-10-07 (teste interno)

- HUD completo: `hud3024` (38 linhas) traduzido. É a segunda cópia, em 38004, da lista de comandos `hud3020`; usa
  exatamente as mesmas traduções aprovadas na 0.0.2 (Ability, Weapon, Combo, Sub Combo, Purge, Pursuit Combo,
  "Hold ① + □"...).
  - A linha "Hold ① + □□□□□" tem 198 px num limite de 197, igual à da `hud3020`; conferir no jogo.
- 144 recursos alterados; `audit_iso.py` passou (SHA-256
  `54017e959c6412564c46ec974cf59daa3b99f172213cb25c72cb71a290411319`).

- O agente externo entregou 16 lotes (`op03_01` … `op08_01`) sem parar entre eles. Nada foi aplicado ainda.
  - Validador: 9 aprovados e 7 rejeitados (29 erros).
  - A partir da Op 05 as notas e a leitura de contexto caíram; essas entregas precisam de revisão mais minuciosa
    (ESTUDO, seção 8.1).
- `batches.py hand <LOTE>` registra o lote entregue ao agente (`agent/handed.json`). Uma operação entregue ou
  devolvida fica congelada: o `make` não reescreve mais os lotes nem as linhas automáticas dela, porque os limites
  dos lotes mudam quando a memória de tradução cresce.
- ESTUDO, seção 8: estado atual, receita do ciclo de um lote, regras aprendidas, fila de trabalho, decisões
  pendentes e escopo restante fora das operações.

## 0.0.4 — 2026-10-06 (teste interno)

- Material de contexto para o tradutor, como no ACE1:
  - `work/translation/agent/INDICE.md`: premissa, facções, enredo das 28 operações (lido do texto japonês, com
    referências `tabela#linha`), tom e voz por série e por personagem, pistas de contexto dos lotes, pontos sensíveis
    (spoilers, gênero ambíguo) e exemplos aprovados;
  - `work/translation/agent/GLOSSARIO.md` (`tools/ace2/agent_docs.py`): os 450 nomes e termos que existem no texto do
    jogo, por categoria e série, com forma curta, gênero, papel e voz;
  - PLANO e PROMPT agora mandam ler INDICE e GLOSSARIO antes de cada lote.
- Terminologia das séries: 89 termos pesquisados com fonte (`research/series_terms.json`), entre eles Aura Battler,
  Aura Power, Protoculture, GERWALK, Chulip, Distortion Field, Kimbareid, Hyper Mode e Antibody, além do vocabulário de
  sistema do ACE3 (Ace Points, Module, Free Mission...). As formas sem ponto que o jogo usa (グラビティブラスト,
  アンチボディ) agora são reconhecidas.
- Correção no glossário: entravam personagens do ACE3 de séries que não estão no ACE2 (Eureka Seven, Gundam X, King
  Gainer, Getter, Turn A, SEED, Macross Plus). Saíram 50 nomes e 34 formas curtas.
  - Bug visível: o rótulo de quem fala レイ (hud3021) estava "Ray" (Ray Beams, Eureka Seven) desde a 0.0.2. Agora é
    **"Rei"**, o computador da Layzner (como no ACE1).
  - O glossário de cada lote passou a respeitar o limite da palavra em katakana (レイ não casa mais dentro de
    リクレイマー ou ドレイク).
- Retratos de briefing: os 19 identificados (36 Noin, 41 Global, 43 Tak, 46 Amuro, 49 Nina, 55 operador da ponte).
- Lotes 03–28 regenerados com o glossário novo. A Op 02 aprovada foi conferida contra a terminologia nova, sem
  divergências.
- Decisões provisórias, pendentes do dono do projeto: ナナフシ = Nanafushi; トランスユニット = Trans Unit;
  Ｄ兵器 = D-weapons; ダンコフ = Dankova (só a MAHQ); 聖戦士 = Holy Warrior na fala; ボドル基艦 = Boddole Flagship.
- 144 recursos alterados; `audit_iso.py` passou (SHA-256
  `1db3c02d1182c0ab16ff8d58916f5d3dc0ef35d289dc23b954a30ada0341af34`).

## 0.0.3 — 2026-10-06 (teste interno)

- Operação 02 completa, em todas as camadas (190 linhas):
  - briefing estratégico 63001;
  - táticos 63033 e 63034;
  - missões 6021 e 6022;
  - debriefing 63169;
  - relatório 63200.
- Tradução feita pelo agente externo (lotes `op02_01` a `op02_03`), validada e revisada aqui:
  - 187 linhas entregues, 3 lotes APROVADOS (`work/translation/agent/validation/`);
  - 30 correções do revisor (`agent/reviewer_fixes.json`):
    - 14 de sentido, entre elas: Zeon e Giganos "ambos" defendendo a autonomia (63200#4); "Severing" inventado
      (6022#35); 報奨金 = reward, não bounty (6021#48); あえて omitido (63200#6); frases truncadas (63001#10,
      6021#12, 6022#57);
    - 16 compactações para caber no limite de linhas.
  - 6 propostas de glossário aceitas (`work/glossary/research/agent_proposals.json`).
- Incidente: o agente aplicou a própria tradução, alterou `merge_fill.py`, gerou uma ISO 0.0.3 e reescreveu este
  CHANGELOG.
  - Tudo isso foi para `work/translation/agent/_quarentena_google_0.0.3/`, e a árvore voltou ao estado da 0.0.2.
  - A Op 01 e as tabelas compartilhadas foram conferidas e estavam intactas.
  - Esta 0.0.3 foi refeita pelo pipeline.
- Procedimento do ACE1 adotado (regra em `AGENTS.md`):
  - `work/translation/agent/` com `batches/`, `returns/`, `validation/`, `review/`, `PLANO.md`, `PROMPT_AGENTE.md`,
    `LOTES.md` e `examples/op01.json`;
  - o agente só grava em `returns/`;
  - `tools/ace2/validate_return.py` (validação + `--apply`) e `tools/ace2/review_returns.py` (revisão) substituem o
    antigo `batches.py apply`.
- Limite de linhas por janela, tirado do próprio jogo:
  - fala de missão: 2 linhas;
  - briefing: 3 linhas (nenhuma das 1.281 falas de briefing em japonês passa disso; a Op 01 também não);
  - a regra antiga "japonês + 1" permitia 4 linhas no briefing.
- Lotes regenerados para as Ops 03–28:
  - `<on()>` agora conta como janela nova;
  - cada linha traz a lista `tokens`;
  - 5.957 linhas a traduzir; 248 já traduzidas e 360 repetições são preenchidas automaticamente
    (`work/translation/auto/`).
- 144 recursos alterados; `audit_iso.py` passou (SHA-256
  `c1cd08f6676e289b8bd068ebcbd456efe40a72b6910e5c1ab4e2cacfae1774c7`).


## 0.0.2 — 2026-10-02 (teste interno)

- Operação 01 completa, em todas as camadas:
  - briefing estratégico 63000;
  - **briefings táticos de cada fase** 63028 e 63029;
  - missões 6011 e 6012 (e as gêmeas 42011 e 42012);
  - debriefing 63168;
  - relatórios da Preventer 63196 e 63197, com a assinatura alinhada à direita.
- Nomes:
  - de quem fala, nas missões (hud3021, 118) e nos briefings (menu3014, 83);
  - todas as 89 unidades da mira (unit_names), em todos os contêineres de missão.
- Interface:
  - menu de pausa, resultados e legenda do mapa (hud3013);
  - lista de comandos (hud3020);
  - títulos, rodapé e locais do briefing (menu3010).
- Glossário: 319 entradas pesquisadas, com fonte, em `work/glossary/research/`, fundidas com o glossário do ACE3 em
  `work/glossary/names.json`. Nos conflitos vale a grafia do ACE3.
- Patentes: 少尉 Ensign, 中尉 Lieutenant, 大尉 Captain (Gundam Wiki); Gato = Major; Cowen = Commodore (o jogo diz
  准将).
- Grafias da wiki aplicadas por script e reversíveis (`work/glossary/name_fixes.json`):
  - Tak (antes Tack);
  - Sinapus;
  - Barkholz;
  - Giganos.
- Limites de largura medidos: briefing 430 px (pela captura da 0.0.1); falas 380 px (provisório).
- 139 recursos alterados; `audit_iso.py` passou.

## 0.0.1 — 2026-10-02 (teste interno, não testado no jogo)

- Base: Special Vocal Version (SLPS-25829) intacta; `MOVIE001.PSS` da edição original de 2006 (abertura "Glorious").
- Fontes: ASCII imprimível completado nas 4 fontes (2500 gameplay 19 px e 21 px, 2500 menus, 2501 HUD), em todos os
  13 pacotes. Nenhum glifo original alterado. Na fonte de 21 px, `@` ficou de fora por falta de espaço.
- Texto: janelas do sistema (`common`, 3 cópias), briefing da Operação 01 (`brief63000`), Operação 01-1 completa
  (`m6011` → contêineres 6011 e 42011) e o nome "Gun Ark".
- Briefing com linhas propositalmente largas, para medir a caixa no jogo.
- `DATA.BIN` +47 KB; os arquivos seguintes foram deslocados; ISO9660 e UDF reescritos. A auditoria (`audit_iso.py`)
  passou.
