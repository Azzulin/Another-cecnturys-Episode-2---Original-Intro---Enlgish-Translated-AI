# Project status

Updated 2026-10-15. Latest build: **0.0.10** (2026-10-09), audited, **not yet tested in game**.

## Summary

| Area | State |
|---|---|
| Campaign (Operations 01–28) | **6,822 / 6,822** lines translated, validated, reviewed line by line and applied |
| Extra missions, tutorial, flashbacks, short missions | 457 + 628 + 122 + 142 lines, applied |
| Menus, encyclopedia, messages | **2,171 / 2,171**, applied (encyclopedia and letters retranslated in full) |
| HUD, speaker labels, enemy names, system windows | complete (256, 118 + 83, 89, 8) |
| Fonts | printable ASCII completed in all 4 fonts / 13 bundles; original glyphs untouched |
| "Glorious" opening | in every build; standalone swap tool for players |
| In-game testing | 0.0.1 (Op 01) and 0.0.9 tested in PCSX2; 0.0.10 not yet |

## Known issues

1. **Menu labels wider than about 141 px are not drawn** (the whole label is blank). Found in the 0.0.9 test on the
   Intermission, Options > Game and Options > Controller screens. 0.0.10 shortens those labels; about 305 other
   one-line menu labels are still over 141 px (unit names, regions, objectives, save and versus screens whose boxes
   have not been measured). List them with `tools\research\label_widths.py over`.
2. **Crash when pausing during a mission** (0.0.9; the PCSX2 log records nothing). 0.0.10 keeps every pause-menu
   item (`hud3013`) within the Japanese width. Not confirmed fixed. If it still happens, the next suspects are the
   grown mission containers and the HUD font atlas (38000/2501).
3. Provisional width limits: mission dialogue (380 px) and most menus are estimated from the Japanese, not measured.
   142 lines are wider than the widest Japanese line of their table (`work/ui/wide_0.0.9.txt`, mostly objectives in
   `menu3055`/`menu3056`).
4. The 21-px font (`38002/3`) has no `@` (no room); which screen uses this font is unknown.

## What to test

Boot normally (save states keep the old font). Please report the operation/mission and a screenshot.

- **Pause in the middle of a mission** (the 0.0.9 crash), in several operations.
- Intermission, Options > Game, Options > Controller: no blank labels.
- Briefings: three full lines inside the box. Mission dialogue: a long line near 380 px.
- Report signatures aligned with fullwidth spaces; the ending credits (`m6285`).
- Two-line objectives (Operations 06, 09, 14, 18, 22).
- The "Rei" speaker label in a Layzner mission (Op 19); "81％" and other percent signs (Op 08, Op 21).
- Command list "Hold ① + □□□□□" (198 px in a 197 px limit).
- Pilot ranks (`menu3001`, `#i` codes: SS, S… Ace, Rookie); the save slot "No. 00" (`menu3041#13`).
- The lines in `work/ui/wide_0.0.9.txt` and `work/translation/agent/width_waivers.json`.
- No freeze in any mission (their containers grew).

## Not translated yet

| Where | What | Plan |
|---|---|---|
| Texture `50641` in `62050`, `62052`, `62054`, `62057` | "プレイヤーユニット / アナザーユニット" header on unit select | translate (4 copies) |
| Texture `50019` in `38002`, `38003` | boot notice: the story is original to the game and differs from the series | translate |
| Texture `50196` in `62057` | copyright with company names in Japanese | optional (romanize) |
| Texture `50020` in `38005`, `38006` | G Gundam "明鏡止水" cut-in | probably keep |
| Executable `SLPS_258.29` (0x219150) | save title shown in the PS2 memory-card browser | optional |
| `MOVIE001.PSS`, `MOVIE002.PSS` | burned-in text not checked | check |
| Voices | audio | out of scope |

The texture census (`tools/research/texture_census.py`) found 1,655 images; only these have Japanese. New textures
must not change original pixels outside the replaced area (same rule as the fonts).

## Open decisions

- Spellings: Tak / Tack; Sinapus / Synapse; Barkholz / Barkholtz; Show / Sho; Gekiganger / Gekigangar;
  King of Hearts / King of Heart; Sarge Opus / Sarge Aupus.
- Provisional terms: 地上人 = Upper Earthling; ナナフシ = Nanafushi; トランスユニット = Trans Unit; Ｄ兵器 = D-weapons;
  ダンコフ = Dankova; 聖戦士 = Holy Warrior; ボドル基艦 = Boddole Flagship; 先輩 = "Senpai" (used in Op 21) vs
  "Senior Gale" (`m6009#22/24`).
- Misa Hayase: 早瀬大尉 = "Capt. Hayase" by the rank table, but the glossary describes her as a Lieutenant.
- Credits: uncertain readings of some staff names; long-vowel style (Satou, Ohtsuka) vs the public spelling of voice
  actors (Toru Furuya, Akio Otsuka).
- Tutorial weapons without official English names (Flame/Flare Bomb, Removed/Removable Arm, Slit Wafer…).
- The source itself is inconsistent in places (Misa is 大尉 and 中尉 in different lines; "Fifth" vs "4th" air base;
  Boddole Zer's fleet "millions" vs "5 million"); the English follows each line.

## Next steps

1. Test 0.0.10 (list above).
2. Measure the menu boxes from screenshots, record them in `work/ui/limits.json`, and undo the abbreviations the
   provisional limits forced ("B. Rifle", "Sub Cann. 01"…).
3. The textures and the save title.
4. Glossary gaps (Mirauli, Sally Po, Peacemillion, Titans, Mobile Doll, Sanc Kingdom…) and the open decisions.
5. Validator: check full names, not only one word of them.
6. 0.0.10 is published as a pre-release patch; the first regular release (0.1.0) comes once a build passes the
   in-game test ([RELEASING.md](RELEASING.md)).
