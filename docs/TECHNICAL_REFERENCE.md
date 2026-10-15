# Technical reference

File formats of Another Century's Episode 2 — Special Vocal Version (SLPS-25829), how the tools rebuild the disc, and
what each script does. The working notes this comes from are in Portuguese in `docs/ESTUDO_ACE2.md`.

Translation target: English in 1-byte ASCII inside CP932 (Shift-JIS) strings, as in the ACE1 and ACE3 English
patches.

## Discs

| Use | Image | Executable | `DATA.BIN` |
|---|---|---|---|
| Base of every build | Special Vocal Version (Japan) | `SLPS_258.29` | 1,315,378,208 bytes, 5,867 resources |
| Opening movie only | Original 2006 release (Japan) | `SLPS_256.23` | — |

The executable opens `DATA.BIN` **by name** (`\DATA.BIN;1`), not by sector, so `DATA.BIN` can grow: the files after
it move into the empty tail of the disc (~20 MB free) and the ISO9660 and UDF records are rewritten.

## Why the earlier fan patch was not reused

An independent audit (`tools/ace2/audit_iso.py`) of the previous English patch found: fonts never completed (text in
fullwidth capitals, 2 bytes per letter, no apostrophe or comma); text written in place within the Japanese byte budget,
leaving 160 unreadable tables, briefing pointers outside their resource and one resource moved on top of a texture;
2,097 lines with altered control codes (`<ab()>`, `<ed()>`, `<op()>`, `%d％` → `%d%%`), strong candidates for its
crashes; and an extractor that numbered resources by index position instead of ID (the IDs have gaps), so its text
was shifted to the wrong missions. Everything here was re-extracted from scratch, and its files are not used.

## Formats

The parsers come from the ACE3 English patch (MIT), via the ACE1 project; only the `DATA.BIN` index differs.

| Item | Format |
|---|---|
| `DATA.BIN` | `BND\0` index binder, 36-byte header: +12 total size, +16 count, +24 `0x30800` (kept). 12-byte entries `(id, offset, size)`. IDs ascending **with gaps**, payloads 2048-aligned, no names. |
| Inner binder | `BND\0`, `(id, offset)` pairs, payloads 32-aligned |
| LZSS | ACE3 variant: `00 01 00 00` + big-endian unpacked size. False signature positives handled by `try_unpack`. |
| Text table | magic `0x10000`, ranges, pointer array, CP932 string pool |
| Mission container | `00 01 00 00`; +8..+12: 16-byte `(id, offset)` records of one-row sub-tables (enemy names); +20: pointer to the dialogue table |
| Font | map `00 00 01 00` (height at +8, 24-byte records: 4 float UV + int16 offset, width, advance) + TIM2 4-bpp atlas (PSMT4, linear or PSMCT32-swizzled) |
| Movies | `/MOVIE0/MOVIE001.PSS` (opening), `MOVIE002.PSS`: MPEG-2 program streams with audio |

### Where the text is

| Content | Resources | Unique lines |
|---|---|---|
| Mission dialogue | `6005–6998` and twins `42xxx` (identical lines) | 6,583 in 106 tables |
| Enemy names (lock-on HUD) | one-row sub-tables inside the mission containers | 89 |
| Briefings, debriefings, reports | `63000–63300` | 1,588 in 168 tables |
| Menus, encyclopedia, logs | bundles `62050–62057` (inner `3000–3077`), copies in `5000`, `120` | 2,171 in 44 tables |
| Gameplay HUD | bundles `38000–38006` (inner `3013`, `3020`, `3021`, `3024`) | 256 |
| System windows | `8031` (+ copies in `8033`, `60000`) | 8 |

Not in text tables: a few textures with Japanese, the memory-card save title in the executable, the movies
([STATUS.md](STATUS.md#not-translated-yet)).

### Control codes

Preserved in the same order (`tools/ace2/validate.py`, and again by the audit): tags
`<sp()> <ab()> <op()> <ed()> <on()> <off()> <im()> <fz()> <tr()> <of()> <cs()> <ac()>`; colors `#c[RRGGBB]…#c`;
`#i…#i` (rank names); variables `%d`, `%s`, `%%`; button and unit icons, which are glyphs of the font:
`○ × △ □ ㊤ ㊦ ㊧ ㊨ ① … ⑳ ㍉ ㌢ ㌔ ㍍`. The fullwidth `％` after `%d` is a **literal**: turning it into `%%` changes the
printf semantics (one of the old patch's errors).

## Fonts

Four distinct fonts in 13 bundles; every copy is patched.

| Font | Where | Atlas | Height | Style | Native ASCII | TrueType chosen by calibration |
|---|---|---|---|---|---|---|
| 2500/2000 | gameplay `38000/1/4/5/6` | 1024×512 | 19 | Mincho (serif) | `% 0-9 M k` | Times |
| 2500/2000 | gameplay `38002/3` | 512×512 | 21 | Mincho | partial | Times |
| 2500/2000 | menus `62050–62054`, `62057` | 1024×512 | 19 | Mincho | partial | Georgia |
| 2501/2001 | gameplay `38000–38006` (HUD) | 256×256 | 16 | Gothic | full alphabet | Yu Gothic Regular |

`tools/ace2/fonts.py`, for each printable ASCII code 0x20–0x7E: keeps a native ASCII glyph; otherwise reuses the
pixels of the fullwidth glyph with a new, cropped record (digits share one width so numbers stay tabular);
otherwise renders the letter from the TrueType face that best matches the native glyphs (chosen by pixel comparison
among 9 candidates, sized by the native cap height), quantized to the palette's ink levels, outlined with the same
1-px dark border as the natives, and placed in free atlas space.

- Coverage lives in the palette luminance (grey 32…~180; every color has alpha 128), not in alpha.
- The gameplay atlas is almost full: a new cell may overlap the transparent part of another cell, but ink never
  lands in someone else's cell. Guard space is decided from the data (the 2500 fonts already touch neighbours, so the
  game samples by point; the 2501 gets 1 px).
- **No original glyph, record or pixel changes** (checked byte by byte). In the 21-px font `@` did not fit and is
  reported as `skipped`. Visual proofs: `work/proof/font_*.png`.

## Disc writer

`tools/ace2/disc.py` (`write_disc`): rebuilds `DATA.BIN` with every payload 2048-aligned in its original order;
the files after it move by `DATA.BIN`'s growth, absorbed by the empty disc tail, so the image size never changes;
ISO9660 records (both endians) and UDF file entries (with descriptor CRC and checksum) are rewritten; whole-file
swaps from another image (the movie) are copied in. The output is re-read and every extent, every file payload and
every changed resource is verified before it returns.

`tools/ace2/textdb.py`: discovers **all** tables on the disc (walking binders and LZSS payloads recursively), groups
copies, and writes them back. Nothing is squeezed: a mission dialogue table that grows is appended to its container
and the +20 pointer moved; a sub-table that grows is appended and its record moved.

`tools/ace2/swap_movie.py`: replaces `MOVIE001.PSS` in place when both movies have the same size (they do), without
any other change ([GLORIOUS_OPENING.md](GLORIOUS_OPENING.md)).

## Tools (`tools/ace2/`)

| Script | Purpose |
|---|---|
| `ace2lib.py` | formats: ISO9660, `DATA.BIN` index, inner binders, LZSS, text tables, mission containers |
| `disc.py` | disc writer (above) |
| `textdb.py` | table discovery, grouping and write-back |
| `export_text.py` | exports the Japanese to `work/translation/en/<table>.json` (keeps existing English) |
| `validate.py` | per-row rules: codes, CP932, no fullwidth, no Japanese, line breaks |
| `merge_fill.py` | merges `_fill/<table>.json`, validates, measures widths with the completed font |
| `rewrap.py` | re-breaks lines to a pixel width (layout only) |
| `fix_names.py` | applies `work/glossary/name_fixes.json` to all English text |
| `fonts.py`, `font_proof.py` | completes the fonts; draws proof images |
| `build.py` | `--version X` dry run; `--write` writes `work/output/ACE2-EN-X.iso` + JSON report; `--svv-opening` keeps the Special Vocal movie |
| `audit_iso.py` | independent audit of a finished image (`--svv-opening` for images built that way) |
| `swap_movie.py` | puts one disc's opening movie on another (standalone, standard library only) |
| `make_patch.py` | release patch: xdelta from the Special Vocal Version + checksum file ([RELEASING.md](RELEASING.md)) |
| `operations.py` | maps tables to the 28 operations in play order |
| `glossary.py`, `agent_docs.py` | glossary merge; translator reference docs (need the ACE3 glossary folder, see below) |
| `batches.py` | translator batches: `make`, `hand`, `status` |
| `validate_return.py` | validates a translator return; `--apply` writes it to `_fill`; `--auto` refills automatic rows |
| `review_returns.py` | side-by-side review pages |
| `check_fixes.py` | tests proposed corrections without writing |
| `test_identity.py`, `test_disc.py`, `test_textdb.py` | self-tests (see [BUILD_FROM_SOURCE.md](BUILD_FROM_SOURCE.md#5-optional-run-the-self-tests)) |

`tools/research/`: one-off scripts used to map text, widths and textures (not part of the build). Most have the
maintainer's path `D:\Ace 2` hard-coded at the top; `label_widths.py` does not.

External dependency: `glossary.py` and `agent_docs.py` read the ACE3 English patch glossary from
`D:\Ace 1\ACE-3-0.9.3\ACE-3-0.9.3\work\glossary` (constant `ACE3`). Nothing else needs it: the merged
`work/glossary/names.json` is in the repository.

## Text layout limits

| Text | Limit | Source |
|---|---|---|
| Mission dialogue | 2 lines, 380 px | provisional: widest Japanese line 398 px, 99th percentile 359 px |
| Briefing / report | 3 lines, 430 px | measured on a 0.0.1 screenshot (no Japanese briefing line has more than 3 lines) |
| Menu label (list buttons, option cells) | 141 px | 0.0.9 test: 141 px drawn, 154 px and up **not drawn at all** |
| Other text | widest Japanese line of the same table | provisional |

Stored in `work/ui/limits.json`; `merge_fill.py` reports wider lines as `WIDE`.

## Pipeline

```
export_text.py → translation in _fill/ → fix_names.py → merge_fill.py → build.py --write → audit_iso.py → PCSX2
                                                                                └→ make_patch.py → release
```
