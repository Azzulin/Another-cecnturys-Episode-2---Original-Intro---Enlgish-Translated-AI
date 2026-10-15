# Changelog

All builds so far are internal test builds (0.0.x). The detailed working log, in Portuguese, is
[docs/CHANGELOG.md](docs/CHANGELOG.md). SHA-256 values are of the full image with the "Glorious" opening, as written
by `tools/ace2/build.py`.

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
