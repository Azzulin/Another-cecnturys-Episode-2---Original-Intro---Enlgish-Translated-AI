# Retomada em outra máquina

Guia para continuar o projeto num computador novo. Escrito em 2026-10-09, com a build 0.0.10 pronta e ainda não
testada. Depois de montar o ambiente (seções 1 a 3), o trabalho continua em `docs/ESTUDO_ACE2.md` seção 8 e no topo
de `docs/CHANGELOG.md`.

## 1. O que copiar

A pasta não é um repositório git. Copie a pasta `Ace 2` inteira, com estas exceções:

| Item | Tamanho | Copiar? |
|---|---|---|
| `Another Century's Episode 2 - Special Vocal Version (Japan).iso` | 3.677.028.352 bytes | **Sim.** Base de todo build. |
| `Another Century's Episode 2 (Japan).iso` (2006) | 4.332.388.352 bytes | **Sim.** Fonte do `MOVIE001.PSS`. |
| `AGENTS.md`, `requirements.txt`, `docs/`, `tools/` | < 1 MB | Sim. |
| `work/` sem `work/output/*.iso` | ~3 GB | Sim (traduções, lotes, glossário, relatórios JSON das builds, capturas). |
| `work/output/ACE2-EN-0.0.10.iso` | 3,6 GB | Só se for testar antes de montar o ambiente. Dá para gerar de novo (seção 3). |
| `work/output/ACE2-EN-0.0.7/0.0.8/0.0.9.iso` | 3,6 GB cada | Não. Substituídas pela 0.0.10. |
| `.venv/` | 87 MB | **Não.** Recriar (seção 2); o venv guarda caminhos desta máquina. |
| `tools/ace2/__pycache__/` | — | Não. |

SHA-256 de referência:

| Arquivo | SHA-256 |
|---|---|
| Special Vocal Version (SLPS-25829) | `efd791e7c50af2ec476f4026c6bda57fcf6d64babf20c12174db642b54941741` |
| Original 2006 (SLPS-25623) | `c9dcaeda5e466120c777d771639e4b247a787c84f3cc7131322f8e6dd390eef5` |
| `ACE2-EN-0.0.10.iso` | `3e8c61433aab58bafa3fb0ff6c0f55d95c63d8eefde1be441d8737be5d578c12` |

Os dois ISOs base ficam na raiz do projeto, com estes nomes exatos: `tools/ace2/ace2lib.py` os procura ali.

## 2. Ambiente

- **Windows.** O `tools/ace2/fonts.py` lê as fontes de `C:\Windows\Fonts`.
- **Python 3.14** (aqui: 3.14.7). Na raiz do projeto:

  ```
  py -3.14 -m venv .venv
  .venv\Scripts\python.exe -m pip install -r requirements.txt
  ```

  São três pacotes: numpy 2.5.3, pillow 12.3.0 e pycdlib 1.21.0. Nesta máquina o comando `python` solto abre a
  Microsoft Store; use sempre `.venv\Scripts\python.exe`.
- **`PYTHONIOENCODING=utf-8`** para tudo que imprime texto do jogo (`merge_fill.py`, `build.py`,
  `validate_return.py`, scripts de pesquisa). Sem isso o console do Windows quebra no "①" e o `merge_fill` para no
  meio, deixando tabelas sem mesclar. No PowerShell: `$env:PYTHONIOENCODING='utf-8'`; no Git Bash:
  `export PYTHONIOENCODING=utf-8`.
- **Fontes usadas nas letras novas.** O `fonts.py` escolhe, entre as candidatas instaladas, a que mais se parece com
  a fonte do jogo. A escolha da 0.0.10 está no relatório `work/output/ACE2-EN-0.0.10.json` (chave `fonts`):

  | Fonte do jogo | TTF escolhida | SHA-256 da TTF nesta máquina |
  |---|---|---|
  | 38000/2500, 38002/2500 | `times.ttf` 18 e 21 | `931c5de5c70401d9324d5014c123802b4fb753000360ceb2f56c589403cd58c5` |
  | 38000/2501 | `YuGothR.ttc` 13 | `cd24b5617c1e26572b0a7fe7e558f7121ca42c36f7b50e8d9216ac222a1c0a93` |
  | 62050/2500 | `georgia.ttf` 17 | `38dffcaf1fac89492f7c56c600a14daf36ae42f7c21985cd4134ae113124a58f` |
  | `\` (reserva) | `segoeui.ttf` | `704eada12961a27fd271f7d3b09e2066520e758390c1776744eff430fee30f6e` |

  Outra versão dessas fontes, ou uma candidata a mais instalada (`CENTURY.TTF` vem com o Office), pode mudar os
  glifos e as larguras medidas. A seção 3 detecta isso.

## 3. Conferir que o ambiente reproduz a build

```
$env:PYTHONIOENCODING='utf-8'
.venv\Scripts\python.exe tools\ace2\build.py --version 0.0.10 --write
.venv\Scripts\python.exe tools\ace2\audit_iso.py work\output\ACE2-EN-0.0.10.iso
```

O build leva uns 2 minutos para planejar e grava 3,6 GB. Ele termina com
`PASS ... SHA-256 3e8c6143...8c12`. **O SHA tem de ser igual ao da tabela da seção 1.** Se não for, compare a chave
`fonts` do novo `work/output/ACE2-EN-0.0.10.json` com a da cópia trazida desta máquina: a causa quase certa é a
fonte (seção 2). Não continue com um ambiente que gera outra ISO sem entender a diferença.

Os testes do pipeline (`tools/ace2/test_*.py`) também servem de verificação rápida.

## 4. Emulador (PCSX2)

Nesta máquina: PCSX2 v2.6.3 em `C:\PCSX2` (modo portátil), BIOS USA v01.60, renderizador Vulkan. O GameDB aplica
sozinho um patch para SLPS-25829 (`nativeScaling`), e não há cheats.

- Log: `C:\PCSX2\logs\emulog.txt`. Cada abertura do PCSX2 sobrescreve o log. O PCSX2 **não registra** quando o jogo
  trava (o crash da pausa não deixou rastro); anote a missão e o que foi feito.
- Saves: `C:\PCSX2\memcards\Mcd001.ps2`. Leve esse arquivo junto para não refazer a campanha até as missões que
  precisam de teste.

## 5. Onde paramos (2026-10-09)

- **0.0.9 testada no PCSX2** (primeiro teste desde a 0.0.1):
  - Rótulos de menu acima de ~141 px não são desenhados (Intermission, Options > Game, Options > Controller). A
    medida está em `work/ui/limits.json` (`menu_label`).
  - O jogo travou ao pausar no meio de uma missão. A causa não foi confirmada.
- **0.0.10 gerada e auditada, não testada:** rótulos encurtados e menu de pausa (`hud3013`) dentro da largura do
  japonês. Detalhes no CHANGELOG.
- **Próximo passo:** `ESTUDO_ACE2.md` 8.6, item 0 (testar a pausa e anotar a missão; conferir as três telas).
  - Se a pausa ainda travar, a causa não é largura de texto. Próximos suspeitos: os contêineres de missão que
    cresceram e o atlas da fonte 38000/2501.
  - Depois disso, os cerca de 305 rótulos de menu que ainda passam de 141 px:
    `tools/research/label_widths.py over`.

### Ferramenta nova

`tools/research/label_widths.py` (somente leitura) tem quatro modos:

- `table <tabela>...`: largura em px de cada linha, JP e EN;
- `over [px]`: rótulos de uma linha que cabem em japonês e passam do limite em inglês;
- `try menu|game "<texto>"...`: mede textos candidatos;
- `source <ref>...`: diz se a linha vem de lote do agente, de linha automática ou de preenchimento à mão, e se já tem
  correção em `reviewer_fixes.json`.

### Como corrigir uma linha já aplicada

| Origem da linha (`label_widths.py source`) | Onde corrigir | Depois |
|---|---|---|
| Lote do agente (`xm_menu…_01`, `opNN_KK`) | `work/translation/agent/reviewer_fixes.json` (`{lote: {ref: inglês}}`) | `validate_return.py <lote> --apply` |
| Linha automática (`repeat`/`tm`) | Corrija a linha de origem (o `value`); se só esta cópia precisa de outro inglês, use `auto/overrides.json` | `validate_return.py --auto` |
| Preenchida à mão (`hud*`, `common`, `unit_names`) | `work/translation/en/_fill/<tabela>.json` | — |

Em todos os casos, termine com `merge_fill.py` → `build.py --version 0.0.N --write` → `audit_iso.py` → CHANGELOG.
Uma build nova recebe o número seguinte (a próxima é 0.0.11).

## 6. O que estava só na memória do Claude desta máquina

As notas do Claude Code ficam em `~\.claude\projects\` e **não vão junto com a pasta**. O essencial delas:

- **Comece toda sessão** lendo `docs/ESTUDO_ACE2.md` seção 8 e o topo de `docs/CHANGELOG.md`.
- **O tradutor externo (agente do Google) só traduz.** Ele lê `work/translation/agent/batches/<LOTE>.json` e grava
  apenas `returns/<LOTE>.json`. O Claude faz todo o resto: validação (`validate_return.py`), revisão de sentido de
  cada linha (`review_returns.py`), correções em `reviewer_fixes.json` (nunca editando a entrega), aplicação, build,
  auditoria e ISO.
  - Em 06/10 o agente aplicou, editou ferramentas, gerou ISO e reescreveu o CHANGELOG. Tudo foi para quarentena.
  - Ele não obedece "pare depois deste lote": valide cada arquivo de `returns/` por conta própria e revise com mais
    cuidado os que vieram rápido.
  - Registre os lotes entregues com `batches.py hand <LOTE>`.
- **Toda operação tem várias camadas de briefing:** estratégico (63000+op-1), táticos por fase (antes de cada fase),
  debriefing e relatórios. Planeje sempre pela operação inteira (`work/translation/operations.json`), nunca só pela
  tabela da missão. O agente do projeto anterior esquecia os táticos.
- **Resposta ao usuário que pergunta sobre a abertura no PS3:** já foi dada (09/10). A build troca o
  `MOVIE001.PSS` inteiro (vídeo e áudio) pelo da edição de 2006. Não houve remux de áudio.

## 7. Dependências externas que faltam

- **`D:\Ace 1` não existe mais** (já não existia nesta máquina). O `AGENTS.md` aponta para o `BASE_RULES.md` de lá,
  e `tools/ace2/glossary.py` e `tools/ace2/agent_docs.py` leem o glossário do ACE3 em
  `D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\work\glossary`.
  - Sem essa pasta, esses dois scripts não rodam.
  - O build, a validação e a revisão **não** dependem deles: `work/glossary/names.json` já está gerado.
  - Se a pasta do ACE1/ACE3 for recuperada, ponha-a no mesmo caminho ou ajuste a constante `ACE3` nos dois scripts.
- Os scripts de `tools/research/` (exceto `label_widths.py`) têm `D:\Ace 2` fixo no código. Funcionam se o projeto
  ficar em `D:\Ace 2`; em outro caminho, troque a constante no topo de cada um. O pipeline (`tools/ace2/`) usa
  caminhos relativos e roda em qualquer lugar.
- O projeto anterior (`D:\Projeto Crise de Meia Idade 2`) e a ISO "English Patched" **não** são necessários (e não
  devem ser usados).
