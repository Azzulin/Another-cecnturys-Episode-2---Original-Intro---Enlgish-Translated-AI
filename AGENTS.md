** Organização das pastas (mesmo padrão do ACE1/ACE3) **
work
    output         ISOs de teste (ACE2-EN-<versão>.iso) + relatório JSON de cada build
    glossary       glossário em JSON
    ui             capturas de tela com medidas de caixas/widgets
    translation/en tabelas exportadas (<tabela>.json) e _fill/ (entrada das traduções)
    proof          provas visuais (fontes, textos)
docs               estudo (ESTUDO_ACE2.md; seção 8 = estado e próximos passos), CHANGELOG.md, REVISAO_PARALELA.md,
                   RETOMADA.md (montar o ambiente noutra máquina: o que copiar, Python/fontes, SHA de referência)
tools/ace2         ferramentas do pipeline; tools/research = scripts de pesquisa (não usados no build)

** Regras **
- Seguir as regras de tradução de D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\BASE_RULES.md (glossário, lotes de 80 linhas,
  gênero neutro quando não se sabe, não encurtar frases, reportar incertezas).
- Todo build parte da Special Vocal Version intacta e usa o MOVIE001.PSS da edição original (abertura "Glorious").
- Executável SLPS_258.29: a única mudança permitida são os patches de tools/ace2/exe.py (fronteira pilha/heap 256 KB
  acima; capacidade da janela de mensagem 60 → 128 letras; decisão do usuário em 2026-10-10). audit_iso.py confere
  que não há outra diferença.
- Texto nunca pode passar da capacidade do widget onde aparece (o jogo não confere e trava depois): janela de
  mensagem ≤ 127 bytes visíveis por linha; objetivos, contadores e textos do HUD/pausa ≤ 32 letras (ambos no
  validate.py); outros widgets conforme ESTUDO 8.5.
- Memória: o jogo carrega cada cena numa arena sem folga (pedido que não cabe volta NULL e trava). Recurso de missão
  não carrega bytes mortos (tabela velha deixada para trás); todo crescimento de recurso de missão vai no CHANGELOG.
- Nunca gravar texto in-place nem espremer em orçamento de bytes: tabelas crescem e são realocadas (textdb.py).
- Nunca alterar glifos originais das fontes; letras novas só em espaço livre (fonts.py verifica).
- Texto em ASCII de 1 byte, nunca fullwidth. Códigos de controle na mesma ordem do japonês (validate.py).
- Não reaproveitar textos, extrações ou injetores do projeto anterior (D:\Projeto Crise de Meia Idade 2) nem da ISO
  "English Patched": a auditoria mostrou linhas trocadas e estruturas corrompidas. O glossário dele só como fonte a
  verificar.
- Toda ISO passa por tools/ace2/audit_iso.py antes de ir para o emulador.
- Versões 0.x.y; builds de teste 0.0.x. Sempre atualizar docs/CHANGELOG.md.
- Se o usuário pedir para lembrar algo, anotar aqui (perguntar se conflitar com uma regra existente).
- Tradutor externo (agente do Google), mesmo procedimento do ACE1: ele **só traduz**, lendo
  work/translation/agent/batches/<LOTE>.json e gravando apenas returns/<LOTE>.json (regras em agent/PLANO.md e
  agent/PROMPT_AGENTE.md). Validação (validate_return.py → validation/<LOTE>.md), revisão de sentido
  (review_returns.py; correções em agent/reviewer_fixes.json, nunca editando a entrega), aplicação em _fill/, build,
  auditoria e ISO são exclusivamente do Claude. Qualquer coisa que o agente aplicar fora de returns/ vai para
  quarentena e é refeita pelo pipeline.
- Repositório público (GitHub): documentação em inglês em README.md, CHANGELOG.md (raiz) e docs/*.md com nome em
  inglês; manter docs/STATUS.md e o CHANGELOG.md da raiz em dia junto com o docs/CHANGELOG.md. Nunca versionar ISO,
  .PSS, .xdelta nem capturas do PCSX2 (work/crash/, .p2s) (.gitignore). Release = tools/ace2/make_patch.py (o patch
  nunca leva o filme de 2006; o jogador aplica o "Glorious" com tools/ace2/swap_movie.py), passos em
  docs/RELEASING.md. Esta pasta não é git: para publicar, copiar sobre um clone (docs/RELEASING.md, "Updating the
  repository from the working folder"); nada que só exista no clone pode se perder.
