# How the AI translation was produced and reviewed

The English text was written by an AI translator and checked by a second AI and by automatic validators, under the
project owner's direction. This page describes the whole procedure so it can be audited, repeated or adapted (for
example for another language). The original, more detailed notes are in Portuguese in `docs/ESTUDO_ACE2.md`
(section 8) and `work/translation/agent/PLANO.md`.

## Roles

| Role | Who | Allowed to |
|---|---|---|
| Translator | an external **Google AI agent** | read `work/translation/agent/batches/<BATCH>.json` and the reference files; write **only** `work/translation/agent/returns/<BATCH>.json` |
| Reviewer, toolsmith, builder | **Claude (Anthropic)** in Claude Code | everything else: tools, glossary, batches, validation, meaning review, corrections, application, fonts, builds, audits, changelog |
| Owner | the project maintainer | decisions (names, terms, style), in-game testing, releases |

The separation is strict. In one incident the translator applied its own work, edited a tool, generated an ISO and
rewrote the changelog; all of it was moved to a quarantine folder (not published) and redone by the pipeline. Since
then every return is checked for changes outside `returns/`, and each file in `returns/` is treated as an
independent delivery.

## 1. Extraction and preparation

1. `tools/ace2/export_text.py` finds every text table on the Special Vocal disc (no hard-coded list) and writes
   `work/translation/en/<table>.json`. Earlier fan extractions were **not** reused: an audit showed misnumbered
   resources and lines applied to the wrong missions.
2. `tools/ace2/operations.py` maps all 168 briefing tables and the mission tables to the **28 operations**, in play
   order: strategic briefing → for each phase, the tactical briefing and the mission dialogue → debriefing → reports
   (`work/translation/operations.json`). An operation is always translated as a whole, so the translator never sees a
   mission without its briefings.
3. Glossary: `tools/ace2/glossary.py` merges owner decisions (`work/glossary/decisions.json`) > the ACE3 English
   patch glossary > researched entries (`work/glossary/research/*.json`, each with its source: series wikis, MAHQ,
   official materials). Characters of series not in ACE2 are excluded. Name matching respects katakana word
   boundaries and ignores a name inside a longer one (レイ inside アムロ・レイ).
4. Reference files for the translator (`tools/ace2/agent_docs.py` and hand-written):
   - `INDICE.md`: premise, factions, the plot of each operation (with `table#row` references), tone and voice per
     series and character, sensitive points (spoilers, characters whose gender the text has not revealed yet);
   - `GLOSSARIO.md`: the 450 names and terms that occur in the game text, with short form, gender, role and voice;
   - `examples/op01.json`: Operation 01, translated by hand and tested in game, as the model for tone, length and
     control codes;
   - `PLANO.md` (rules) and `PROMPT_AGENTE.md` (the prompt given to the agent).

## 2. Batches

`tools/ace2/batches.py make` (operations) and `make --extras` (text outside the operations) write 150 batches of up
to **80 consecutive rows** in play order: `op02_01` … `op28_04`, `xa_*` (extra missions), `xb_*` (tutorial),
`xc_*` (flashbacks), `xd_*` (short missions), `xm_menuNNNN_*` (menus, encyclopedia, messages).

Each row carries what the translator needs and what the validator will check:

```json
{
 "ref": "brief63001#1",
 "layer": "strategic briefing",
 "phase": null,
 "tokens": [],
 "jp_lines": 1, "max_lines": 1, "max_line_px": 430, "max_line_chars_approx": 43,
 "jp": "ガンダム２号機 追撃",
 "en": "",
 "notes": ""
}
```

A batch also has `context_before` / `context_after` (read-only neighbouring rows), the glossary entries that occur in
it, a `do_not_touch_names` list, and a `report` block the translator must fill (summary, rows examined,
uncertainties, glossary proposals).

Rows already translated elsewhere (identical Japanese, codes included) are not sent (`tm`), and a row repeated
inside the pending text is sent once (`repeat`); both are filled automatically (`work/translation/auto/`). Once a
batch is handed over (`batches.py hand <BATCH>`), its group is frozen: later `make` runs never move its boundaries.

## 3. Validation (automatic)

`tools/ace2/validate_return.py <BATCH>` (or `--all`) writes `agent/validation/<BATCH>.md`, APPROVED or REJECTED.

- **Structural errors go back to the translator:** rows added, removed or reordered, frozen fields edited
  (`jp`, `ref`, `phase`…), invalid JSON, Japanese that no longer matches the table.
- **Content errors** can be fixed by the reviewer: control codes missing or out of order; non-ASCII or forbidden
  characters (curly quotes, em dash, `;`, `~`, a lone `%`); double or trailing spaces; too many lines; a line too
  wide for the box that an automatic re-wrap cannot fix; a glossary name missing; an old spelling.
- Warnings: lines re-wrapped automatically, glossary terms (ranks, titles) missing, translator notes, empty report.

## 4. Meaning review (every line)

`tools/ace2/review_returns.py <BATCH>` writes `agent/review/<BATCH>.md`: Japanese and English side by side, codes
stripped, with the translator's notes and suspicion flags. The reviewer reads **every row** against the Japanese.

- For large deliveries, three reviewer sub-agents worked in parallel (one block of operations each) with the prompt
  in `docs/REVISAO_PARALELA.md`. They only **proposed** fixes in a separate file; `tools/ace2/check_fixes.py <file>`
  tests proposals with the validator's rules without writing anything, and each proposal was read and accepted or
  refused before being merged.
- Corrections are stored in `work/translation/agent/reviewer_fixes.json` as `{batch: {"<table>#<id>": "English"}}`
  and applied on top of the return. **The translator's file is never edited**, so every change is traceable.
- Total: **1,486 corrections** in 144 batches. The Encyclopedia (69 entries) and the private messages (19 letters)
  were retranslated entirely, because the translator summarized them and invented content.

Typical translator errors the review looked for:

- hedges turned into facts (らしい, ようだ, であろう, 推測される, 可能性, とのこと);
- invented insults or flourishes ("bastards", "scum", "fools", "noble sacrifice");
- dropped clauses (すでに, 少しずつ, 人質をとって…) and wrong terms (犯行声明 = claim of responsibility; 宙域 is
  space, not airspace; 誤射 is a mistaken shot, not a misfire);
- "he" for characters the text has not identified yet; stiff speech without contractions for casual characters;
  "-chan"/"-san" left in romaji;
- sentences split over two rows closed too early; a two-line objective translated as two objectives; shifted lines;
- names: "Amuro Rei" (Ray), "Sho" (Show), partial names that pass a word-based check ("Will Wips", "Golaon").

## 5. Application and build

1. `validate_return.py <BATCH> --apply`, always for a **whole operation**, writes the rows into
   `work/translation/en/_fill/<table>.json`; `validate_return.py --auto` then refills the automatic rows of every
   group.
2. `tools/ace2/fix_names.py --write` applies project-wide spelling fixes (`work/glossary/name_fixes.json`).
3. `tools/ace2/merge_fill.py` validates every fill again and measures widths with the real font.
4. `tools/ace2/build.py --version 0.0.N --write`, then `tools/ace2/audit_iso.py`, a changelog entry and a test in
   PCSX2.

Glossary proposals from the translator that cite a source go to `work/glossary/research/agent_proposals.json` and
enter through `glossary.py --write`.

## What is in the repository

| Path | Content |
|---|---|
| `work/translation/agent/batches/` | the 150 batches as handed over |
| `work/translation/agent/returns/` | the translator's deliveries, unedited |
| `work/translation/agent/validation/`, `review/` | validator report and review page of every batch; reviewer notes and doubts in `review/revisores_*` |
| `work/translation/agent/reviewer_fixes.json` | every correction |
| `work/translation/agent/handed.json`, `applied.json` | what was handed over and applied |
| `work/translation/agent/width_waivers.json` | the few width exceptions, with the reason |
| `work/translation/auto/` | automatic rows and their per-row overrides |

The quarantine folders (`_quarentena_google_*`) are kept only on the maintainer's machine.

## Repeating it

The agent instructions are in Portuguese (`PLANO.md`, `PROMPT_AGENTE.md`); the rest of the procedure is tool-driven.
For a new language or a full retranslation: regenerate the batches for your text (`batches.py make --force`
rewrites frozen groups, so start from a clean `handed.json`/`applied.json`), translate the prompt and rules, adapt the
English-specific checks in `validate_return.py`, and keep the two principles that made this work: the translator
only writes its own folder, and nothing reaches the game without validation and a line-by-line review.
