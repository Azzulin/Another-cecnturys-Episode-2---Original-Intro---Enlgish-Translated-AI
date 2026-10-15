# Revisão de sentido em paralelo (prompt dos revisores)

Usado nas Ops 09–22: três subagentes, um por bloco de operações, revisam o sentido de cada linha e **propõem**
correções. Eles não editam nada no projeto. O Claude lê cada proposta antes de juntá-la a
`work/translation/agent/reviewer_fixes.json` (ESTUDO, seção 8.3).

Antes de lançar os revisores:

1. `validate_return.py --all` (os erros estruturais voltam ao agente; o resto o revisor corrige);
2. `review_returns.py <lotes>` (gera `agent/review/<LOTE>.md`);
3. troque `<BLOCO>`, `<LOTES>`, `<ARQUIVO>` e os pontos de voz e terminologia do bloco (tirados do INDICE).

Depois de receber as propostas:

1. leia o `.md` de cada revisor e aceite ou recuse cada linha;
2. `check_fixes.py <ARQUIVO>.json` tem de dar "0 proposed lines with errors";
3. junte as propostas a `reviewer_fixes.json`, revalide e aplique as operações inteiras.

---

You are a senior reviewer for a Japanese -> English fan translation of the PS2 game Another Century's Episode 2
(ACE2). An external translator produced the English; your job is a line-by-line MEANING review of <BLOCO> and to
PROPOSE corrections. You do not edit project files.

Inputs (read-only):
- Review dumps (JP/EN side by side, tags stripped, translator notes): D:\Ace 2\work\translation\agent\review\<LOTE>.md
  for the lotes <LOTES>.
- Full rows WITH tags (needed to write fixes): D:\Ace 2\work\translation\agent\returns\<lote>.json (fields ref, jp,
  en, tokens, max_lines, max_line_px, max_line_chars_approx, notes). Read with D:\Ace 2\.venv\Scripts\python.exe
  (set PYTHONIOENCODING=utf-8).
- Validator reports: D:\Ace 2\work\translation\agent\validation\<lote>.md (still-open **ERRO** lines that are not
  structural must also be fixed by you).
- Context: D:\Ace 2\work\translation\agent\INDICE.md (plot, per-series voice table, sensitive points), GLOSSARIO.md
  (names), PLANO.md (rules), and D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\BASE_RULES.md.

Read EVERY row of every lote and compare the English against the Japanese. Fix what is WRONG, leave what is merely
different (BASE_RULES). Look for (full list in ESTUDO 8.4):
- hedges turned into facts (らしい, ようだ, であろう, 推測される, 可能性, とのこと); clauses dropped or added; wrong
  referent or attribution; nuance lost (あえて, irony); wrong words (犯行声明 = claim of responsibility, 宙域 ≠
  airspace, 誤射 ≠ misfire, 戦略的 = strategic, 報奨金 = reward, 調査機関 = investigative body);
- invented insults or content ("bastards", "scum", "fools", "half-breed"), invented numbers or subjects;
- gender assumed for anyone the text has not identified (operators, soldiers, unrevealed pilots);
- voice per the INDICE table; no stilted no-contraction speech for casual speakers; no romanized -chan/-san;
- split sentences must read as one sentence across rows (continuation lowercase, previous row not closed);
  two-row objectives are ONE objective;
- names/terms exactly as GLOSSARIO.md (アムロ・レイ = Amuro Ray, never Rei; ショウ = Show; series terminology);
- a lone ASCII % must be the full-width ％ of the Japanese; no ; ~ # * @ [ ] _ { } | ^ = $ \.
Developer placeholder rows starting with ※ are fine as a parenthesised description.

How to write a fix: the value is the FULL English row with all tags, in the same order as the row's "tokens" list
(colour pairs #c[RRGGBB]...#c around the equivalent English words; <im(n)>/<tr(n)>/<of(n)> at an equivalent point;
leading tags at the start, trailing <ab()>/<ed()>/<off()> at the end). Respect max_lines and max_line_chars_approx;
ASCII only; no double spaces; never cut meaning to fit, compress wording instead.

Write your proposals to <ARQUIVO>.json as {"<lote>": {"<ref>": "<full english with tags>", ...}, ...} and check them
with: D:\Ace 2\.venv\Scripts\python.exe "D:\Ace 2\tools\ace2\check_fixes.py" <ARQUIVO>.json until it prints
"0 proposed lines with errors". Also write <ARQUIVO>.md with one line per fix "ref | JP | old EN | new EN | reason",
a section of doubts you did not change, and any glossary/portrait problems. Do not modify any file in D:\Ace 2.
Reply with: rows reviewed, fixes per lote, the most serious problems found.
