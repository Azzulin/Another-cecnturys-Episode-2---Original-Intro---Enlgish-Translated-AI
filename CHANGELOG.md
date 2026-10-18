# Changelog

All builds so far are internal test builds (0.0.x). The detailed working log, in Portuguese, is
[docs/CHANGELOG.md](docs/CHANGELOG.md). SHA-256 values are of the full image with the "Glorious" opening, as written
by `tools/ace2/build.py`.

## Patch 0.0.16 published — 2026-10-17 (no new build)

- **0.0.16 patch (pre-release `v0.0.16`):** `ACE2-EN-0.0.16.xdelta` (38,906,005 bytes, xdelta3 3.0.11) turns the
  untouched Special Vocal Version into the English disc with the Special Vocal opening
  (`1608ce46831834437f53d427c8441b6c7ad9aeff0f4ebb5ae8b5caf9f8f40890`, the same image as `build.py --svv-opening`);
  `swap_movie.py` with the 2006 disc then gives exactly the audited 0.0.16 build (`888f11d1…4ac79e`). It is larger
  than the 0.0.10 patch (454,701 bytes) because builds since 0.0.14 rewrite the 108 compressed partner packages.
- New guide [docs/MAKE_YOUR_OWN_PATCH.md](docs/MAKE_YOUR_OWN_PATCH.md): build from this repository, make an xdelta
  patch with `make_patch.py`, check it, and share it (a release on your own fork, anywhere else, or fixes sent back
  to the project).
- `make_patch.py --svv-opening`: makes the patch from a build made with `--svv-opening`, on a machine without the
  2006 disc (checked against the build's own SHA-256; the "Glorious" checksum is added when the 2006 disc is there).
- README, INSTALL_PATCH, STATUS and BUILD_FROM_SOURCE now point players to the 0.0.16 patch.

## Repository update — 2026-10-17 (no new build)

- The repository now holds the 0.0.16 state: tools, all translations (including the partner chatter), working notes
  and build reports 0.0.15/0.0.16. Building from this repository reproduces the audited 0.0.16 image byte for byte
  (`888f11d1…4ac79e`); the `--svv-opening` build (`1608ce46…f40890`) plus `swap_movie.py` gives the same image.
- `swap_movie.py`, `make_patch.py`, `build.py --svv-opening`, `audit_iso.py --svv-opening` and `ACE2_FONTS` carried
  over to the new tools; the executable patch is now part of every build, with either opening.
- Guides rewritten for 0.0.16: status and freezes, widget limits for translators, partner tables, PCSX2 notes (save
  states and CRC), `crash_watch.py`, Python 3.12 or newer.
- `.gitignore`: PCSX2 captures (`work/crash/`, `*.p2s`) and archives (`*.7z`) are never committed.

## 0.0.16 — 2026-10-16

- 0.0.15 froze at the same point of Op 11-1 (destroying the first solar facility). This time `crash_watch.py`
  caught it: the HUD counter draws **label + "：" + value in one 32-character widget**, and
  "Solar Facilities Destroyed：1 facilities" has 39 characters.
- Counters shortened: Op 11-1 "Solar Facilities Destroyed：12"; Op 21-1 "Heavy Attackers Passed：7 units"; Op 22-2
  "Resistance Facility：HP 100％".
- `menu3056` (objectives on the mission data screens and Free Mission) uses the same 32-character widget: its 12
  automatic copies now take the new objective text.
- Validator: `check_counters` (label + 1 + value within 32, in the build and in `merge_fill.py`); the `widget` rule
  also covers `menu3056`.
- Mission files at most +800 bytes (6010), −12,176 bytes in total; partner packages at most +512.
- 605 resources changed; audit PASS. SHA-256 `888f11d1e518cd45a7b71002cd041ee087e537e592d8e6d68cb8825f5b4ac79e`.

## 0.0.15 — 2026-10-16

- 0.0.14 froze in Op 11-1. Text widgets whose owner sets no capacity hold **32 characters** (both widget
  classes): objectives, counters, labels, names, the conditions of MISSION INFORMATION and the pause help line.
  The Op 11-1 objective "Destroy 12 or more solar facilities" had 35.
- 27 lines rewritten within 32 characters ("Destroy 12+ solar facilities", "View abilities and commands."…): 20 in
  `reviewer_fixes.json`, one automatic row in `auto/overrides.json`, the pause help in `_fill/hud3013.json`.
- Validator rule `widget`: a plain one-line row of a mission or HUD table whose Japanese fits in 32 characters has at
  most 32 in English (spaces count; `%d` counts as 3).
- `crash_watch.py` lists both widget classes (79 widgets in the Op 12-1 capture).
- 605 resources changed; audit PASS. SHA-256 `4281f242ee08eafeeeeded3aec95cff1482b53994e7cb11dec370fdeab9f5d1e`.

## Public repository and first patch — 2026-10-15

- English documentation for players, builders, translators and maintainers (`README.md`, `docs/*.md`).
- `tools/ace2/swap_movie.py`: standalone tool (Python standard library only) that puts the original 2006
  "Glorious" opening on any Special Vocal Version image, Japanese or English, and verifies the result. Tested on the
  real discs: Japanese + Glorious, English + Glorious (identical to the 0.0.10 build), and back.
- `tools/ace2/make_patch.py`: release patch (xdelta from the untouched Special Vocal Version, without the 2006 movie)
  and checksum file, with decode and Glorious checks.
- `build.py --svv-opening` / `audit_iso.py --svv-opening`: build and audit without the 2006 disc.
- `ACE2_FONTS` environment variable: folder of the TrueType candidates for the font generator (default
  `C:\Windows\Fonts`).
- Build 0.0.10 reproduced on a second machine with the same SHA-256.
- **First public patch: 0.0.10 (pre-release).** `ACE2-EN-0.0.10.xdelta` (454,701 bytes, xdelta3 3.0.11) turns the
  untouched Special Vocal Version into the English disc with the Special Vocal opening
  (`60227c82247a6954b2003cbbe142c7fc0e318604862f0f9984340213a9cec2aa`); `swap_movie.py` with the 2006 disc then gives
  exactly the audited 0.0.10 build (`3e8c6143…8c12`).
- Note: the repository was published from the 0.0.10 state; builds 0.0.11–0.0.14 below were made before that date
  and reached the repository on 2026-10-17.

## 0.0.14 — 2026-10-10

- Test of 0.0.13: cutscenes no longer freeze and gameplay was stable.
- **Partners' battle chatter in English:** 107 partners, 6,138 lines (2,657 unique), 34 batches `xp_01`–`xp_34`
  translated by Claude at the owner's request and validated like the other batches. One voice per character
  (Gato and Zechs formal, Duo and Kaine loose, Rei in short machine phrases); Izumi's puns turned into English puns.
- Partner packages stay in memory during a mission: they grow at most +512 bytes (2022, Gato).
- 605 resources changed; audit PASS. SHA-256 `ee93ee69969950b22f1e076e9913cda6530b0c815a554a79591e7dce0ae9e74d`.

## 0.0.13 — 2026-10-10

- **Real cause of the Op 12-1 freeze: text longer than its widget.** Each text widget reserves a buffer for a fixed
  number of characters, and the glyph builder never checks it. The message window asked for 60; the Japanese never
  goes past 60, the English did in about 1,960 lines. Lines of 65–67 characters before the cutscene overwrote a HUD
  sprite that is only drawn in the boss phase.
- **Executable patch:** message window capacity 60 → 128 (`exe.py`). Validator: a message line shows at most 127
  bytes. Seven briefing lines rewritten to fit.
- Probably also the cause of the 0.0.9 pause freeze (pause confirmations of 89–96 characters).
- **Partner chatter found:** it lives in the `PMS` chunk of each partner's model package (`VMD` format), which the
  extractor did not read. 1,394 text locations now (was 934); new tables `partnerNNN` and `partner_names`
  (pilot names, filled from the glossary). Lines not yet translated in this build.
- `tools/research/crash_watch.py` lists every text widget in RAM (capacity, characters, text) and dumps the moment
  one overflows.

## 0.0.12 — 2026-10-10

- **Game memory +256 KB** (owner's decision): `exe.py` moves the stack/heap boundary up, so the arena where every
  mission is loaded grows from 0x1950100 to 0x1990100 bytes. The stack keeps 768 KB (161 KB used at most).
- The executable change makes PCSX2 see a different CRC: save states of older builds do not load; memory card saves
  are fine.
- `audit_iso.py` requires the executable to be the original plus exactly these patches.
- SHA-256 `feada09f94d4275077415193b9d3c7d7da0b7fe75d599084b37ba655e461f14b`.

## 0.0.11 — 2026-10-10

- 0.0.10 froze in Op 12-1 after the cutscene before the fight with Kaine. First diagnosis: memory. Mission files
  kept their Japanese table as dead weight when the English one was appended.
- `ace2lib.mission_relayout` rebuilds each table where the Japanese one was and moves the sections after it: the
  largest mission file now grows +800 bytes (was +24,800), −12 KB in total (was +920 KB).
- `audit_iso.py` fails a mission file that carries dead bytes ("mission memory").
- Not the cause of the freeze (0.0.12 froze the same way), but kept.
- 389 resources changed; audit PASS. SHA-256 `374a798d8c6bd0877cb648b77f319f991fc2f4f9423807aeec9d0952f7025a77`.

## 0.0.10 — 2026-10-09

- First PCSX2 test since 0.0.1 (done with 0.0.9): menu labels wider than ~141 px are not drawn at all; the game
  crashed when pausing during a mission.
- Menu labels shortened ("Back to Menu", "Defaults", "Control Type", "Auto Altitude"…); every pause-menu item kept
  within the Japanese width ("Resume", "Commands", "To Intermission"…).
- `merge_fill.py` must run with `PYTHONIOENCODING=utf-8` on Windows (it stopped half-way on "①").
- 389 resources changed; audit PASS. SHA-256 `3e8c61433aab58bafa3fb0ff6c0f55d95c63d8eefde1be441d8737be5d578c12`.

## 0.0.9 — 2026-10-08

- **Every text table of the game in English:** campaign 6,822/6,822, menus 2,171/2,171, extra missions 457,
  tutorial 628, flashbacks 122, short missions 142, HUD, names and system windows. All 150 translator batches applied.
- Extras reviewed like the operations (627 corrections). The Encyclopedia (69 entries) and the private messages
  (19 letters) were retranslated entirely: the translator had summarized them and invented content.
- Buttons: `決定` = "OK"; fullwidth separators kept; `対戦` = Versus.
- 389 resources changed; audit PASS. SHA-256 `3ec584ee6a6490687cf3671a144f20b48ef67dba7b88e7708cd14e65d8076da0`.

## 0.0.8 — 2026-10-08

- **Full campaign: Operations 01–28**, 6,822 story lines (new: Ops 22–28).
- Meaning review with three parallel reviewers: 367 corrections in Ops 22–28 (inverted meanings, hedges turned into
  facts, partial names, truncated report sentences).
- Ending credits: 1,436 mojibake spaces fixed; roles in English, names in Hepburn.
- 339 resources changed; audit PASS. SHA-256 `8326913d37c982445b9e0b3fe6ac73ef69cc4cb1145950dc49cd0ad215626401`.

## 0.0.7 — 2026-10-08

- **Operations 09–21** (3,164 lines); 4,832 of 6,822 story lines applied.
- 348 review corrections (hedges, invented insults, dropped clauses, wrong terms, voice, gender of unidentified
  pilots).
- The validator now rejects a lone ASCII `%` (the game's printf reads it as a conversion; use `％`).
- 286 resources changed; audit PASS. SHA-256 `a1853fe7ceec93aeaecdfb1ae21c654573239df5875955bfca7003247b94c366`.

## 0.0.6 — 2026-10-07

- **Operations 03–08** (1,221 lines), 56 review corrections ("Operation Stardust", "Amuro Ray"…).
- Glossary fix: a name inside a longer name no longer matches (レイ inside アムロ・レイ caused "Amuro Rei").
- 195 resources changed; audit PASS. SHA-256 `874de9a95ad6bd03412e618e584f8a2da3a82d28ecb7823c6ac77466d6c99bff`.

## 0.0.5 — 2026-10-07

- HUD complete (second copy of the command list, `hud3024`).
- Translator batches frozen once handed over.
- 144 resources changed; audit PASS. SHA-256 `54017e959c6412564c46ec974cf59daa3b99f172213cb25c72cb71a290411319`.

## 0.0.4 — 2026-10-06

- Translator reference package: plot index of the 28 operations, voice per series and character, glossary of the 450
  names and terms in the game.
- 89 series terms researched with sources. Characters from series not in ACE2 removed from the glossary (the speaker
  label レイ is now "Rei", Layzner's computer).
- 144 resources changed; audit PASS. SHA-256 `1db3c02d1182c0ab16ff8d58916f5d3dc0ef35d289dc23b954a30ada0341af34`.

## 0.0.3 — 2026-10-06

- **Operation 02** (190 lines) by the external translator, validated and reviewed (30 corrections).
- The translator applied its own work, edited a tool and built an ISO on its own: everything quarantined and redone.
  The rule "the translator only writes its returns folder" dates from here.
- Window line limits from the game itself: mission 2 lines, briefing 3.
- 144 resources changed; audit PASS. SHA-256 `c1cd08f6676e289b8bd068ebcbd456efe40a72b6910e5c1ab4e2cacfae1774c7`.

## 0.0.2 — 2026-10-02

- **Operation 01** complete in every layer (strategic and tactical briefings, missions, debriefing, reports).
- Speaker names, all 89 lock-on names, pause menu, results, command list.
- Glossary of 319 researched entries merged with the ACE3 glossary; ranks 少尉 Ensign, 中尉 Lieutenant, 大尉 Captain.
- Measured limits: briefing 430 px; mission 380 px (provisional).

## 0.0.1 — 2026-10-02

- Proof of concept on the untouched Special Vocal Version, with the 2006 `MOVIE001.PSS` ("Glorious").
- Printable ASCII completed in the 4 fonts (13 bundles) without changing any original glyph.
- System windows, Operation 01 briefing and Operation 01-1 in English. `DATA.BIN` +47 KB, files moved, ISO9660 and
  UDF rewritten. Tested in PCSX2: fonts, dialogue and scenes OK.
