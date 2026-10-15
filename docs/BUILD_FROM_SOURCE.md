# Building the English ISO from source

This rebuilds the English disc from your own Special Vocal Version ISO and the translation files in this repository,
exactly as the maintainers do. If you only want to play, the patch is simpler: [INSTALL_PATCH.md](INSTALL_PATCH.md).

Time: about 5 minutes (2 to plan, 2–3 to write 3.6 GB). Disk: 3.7 GB per build plus the source ISOs.

## 1. Get the repository

```
git clone https://github.com/Azzulin/Another-cecnturys-Episode-2---Original-Intro---Enlgish-Translated-AI.git "Ace 2"
cd "Ace 2"
```

(Or download the ZIP from GitHub and extract it.)

## 2. Put the ISOs in the repository root

The tools look for these **exact file names** in the repository root (next to `README.md`):

| File name | Required? | SHA-256 |
|---|---|---|
| `Another Century's Episode 2 - Special Vocal Version (Japan).iso` | **Yes** (base of every build) | `efd791e7c50af2ec476f4026c6bda57fcf6d64babf20c12174db642b54941741` |
| `Another Century's Episode 2 (Japan).iso` | Only for the "Glorious" opening (default) | `c9dcaeda5e466120c777d771639e4b247a787c84f3cc7131322f8e6dd390eef5` |

They are ignored by git (`.gitignore`), so they never get committed. Without the 2006 disc, build with
`--svv-opening` (step 6).

## 3. Python environment (Windows)

Install **Python 3.14** from [python.org](https://www.python.org/downloads/) (3.12+ should work; 3.14.7 is the
tested one). In the repository root, in PowerShell:

```
py -3.14 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONIOENCODING = 'utf-8'
```

- `requirements.txt` pins numpy 2.5.3, pillow 12.3.0 and pycdlib 1.21.0.
- Always call `.venv\Scripts\python.exe` (on some Windows installs a bare `python` opens the Microsoft Store).
- **`PYTHONIOENCODING=utf-8` is required** in every new terminal: the tools print game text (①, ○, Japanese), and
  the Windows console code page breaks on it. `merge_fill.py` stops half-way without it, leaving tables unmerged.
  Git Bash: `export PYTHONIOENCODING=utf-8`.

The commands below use Windows paths. On Linux/macOS use `.venv/bin/python` and forward slashes.

## 4. Fonts

The game fonts have no lowercase Latin letters and almost no punctuation. `tools/ace2/fonts.py` draws the missing
printable ASCII characters into free space of each font atlas, choosing, by pixel comparison with the game's own
glyphs, the TrueType font that matches best. It reads them from `C:\Windows\Fonts`. The fonts chosen for every
build so far:

| Game font | Chosen TrueType | SHA-256 of the TTF used |
|---|---|---|
| gameplay 38000/2500, 38002/2500 | `times.ttf` 18 and 21 px | `931c5de5c70401d9324d5014c123802b4fb753000360ceb2f56c589403cd58c5` |
| HUD 38000/2501 | `YuGothR.ttc` 13 px | `cd24b5617c1e26572b0a7fe7e558f7121ca42c36f7b50e8d9216ac222a1c0a93` |
| menus 62050/2500 | `georgia.ttf` 17 px | `38dffcaf1fac89492f7c56c600a14daf36ae42f7c21985cd4134ae113124a58f` |
| `\` (fallback) | `segoeui.ttf` | `704eada12961a27fd271f7d3b09e2066520e758390c1776744eff430fee30f6e` |

The build report (`work/output/ACE2-EN-<version>.json`, key `fonts`) records the choice of each build.

- A different version of these fonts, or an extra candidate installed (`CENTURY.TTF`, which comes with Microsoft
  Office), can change the glyphs and therefore the SHA-256 of the result. The game still works, but your ISO will not
  match the published checksum. Step 7 detects this.
- **Linux/macOS:** copy the candidate files (`CANDIDATES` in `tools/ace2/fonts.py`: `times.ttf`, `georgia.ttf`,
  `YuGothR.ttc`, `segoeui.ttf`…, with exactly those names) from a Windows installation into a folder and point the
  tools to it: `export ACE2_FONTS=/path/to/that/folder`. Not tested by the maintainers.

## 5. Optional: run the self-tests

```
.venv\Scripts\python.exe tools\ace2\test_identity.py
.venv\Scripts\python.exe tools\ace2\test_textdb.py
.venv\Scripts\python.exe tools\ace2\test_disc.py
```

- `test_identity.py`: rebuilding every container without edits reproduces the original bytes (index, 528 binders,
  754 LZSS blocks, 934 text tables).
- `test_textdb.py`: a synthetic translation 1.5× longer than the Japanese fits in every table.
- `test_disc.py`: a disc rebuilt without edits is byte-identical to the original; a grown disc with the movie swap
  verifies. Writes two temporary images (needs ~8 GB).

## 6. Build

Dry run first (plans every change, writes nothing, prints sizes and the fonts chosen):

```
.venv\Scripts\python.exe tools\ace2\build.py --version 0.0.10
```

Then write the image:

```
.venv\Scripts\python.exe tools\ace2\build.py --version 0.0.10 --write
```

Output: `work/output/ACE2-EN-0.0.10.iso` and `work/output/ACE2-EN-0.0.10.json` (report: tables, fonts, sizes,
SHA-256). The last line is `PASS: extents, every file payload and every changed resource verified. SHA-256 …`.

Without the 2006 disc:

```
.venv\Scripts\python.exe tools\ace2\build.py --version 0.0.10 --svv-opening --write
```

writes `work/output/ACE2-EN-0.0.10-svv-opening.iso`. Adding the 2006 movie to it later with
[swap_movie.py](GLORIOUS_OPENING.md) gives the same bytes as the normal build.

What the build does (details in [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md)):

1. reads every `work/translation/en/<table>.json` row that has an `"en"` value and validates it (control codes,
   encoding, line count); any failure stops the build;
2. writes the English into every copy of each table on the disc, growing and relocating tables instead of squeezing
   text into the Japanese byte budget;
3. completes the ASCII glyphs of the 4 fonts in all 13 font bundles, never touching an original glyph;
4. rebuilds `DATA.BIN` (it grows by a few hundred KB), moves the files after it into the empty tail of the disc,
   rewrites the ISO9660 and UDF records, and swaps in the 2006 `MOVIE001.PSS`;
5. re-reads the new image and verifies every file extent, every file's content and every changed resource.

The image size never changes (3,677,028,352 bytes).

## 7. Audit and compare

```
.venv\Scripts\python.exe tools\ace2\audit_iso.py work\output\ACE2-EN-0.0.10.iso
```

(Add `--svv-opening` for an image built with that option.) It independently re-reads the image and checks: no
overlapping files or resources; every file other than `DATA.BIN` and the movie byte-identical to the original disc;
the movie identical to the expected opening; every text table still parses with all control codes in the Japanese
order; every resource without text or font byte-identical. It ends with `PASS: layout, files, opening movie, text
integrity and control tokens`.

For 0.0.10 the build SHA-256 must be `3e8c61433aab58bafa3fb0ff6c0f55d95c63d8eefde1be441d8737be5d578c12`. A
different SHA with `PASS` almost always means different fonts (step 4): compare the `fonts` key of your report with
the one in the repository's `work/output/ACE2-EN-0.0.10.json`.

## 8. Test in PCSX2

Boot the image normally (not from a save state made with another build: save states keep the old font in memory).
What to look at is listed in [STATUS.md](STATUS.md#what-to-test).

## Troubleshooting

| Message | Fix |
|---|---|
| `Output exists: work\output\ACE2-EN-….iso` | The build never overwrites. Delete the old image or use a new version number. |
| `Expected the Special Vocal Version disc (/SLPS_258.29)` | The base ISO in the root is not the Special Vocal Version. |
| `FileNotFoundError: ...Another Century's Episode 2 (Japan).iso` | No 2006 disc in the root: add it or use `--svv-opening`. |
| `Validation failed: ... tokens [...] != [...]` | A translated row lost or reordered a control code. Fix that row (see [MAKE_YOUR_OWN_TRANSLATION.md](MAKE_YOUR_OWN_TRANSLATION.md#control-codes)). |
| `UnicodeEncodeError` in the console | Set `PYTHONIOENCODING=utf-8` (step 3). |
| `OSError: cannot open resource` (fonts) | A candidate TrueType file is missing; see step 4. |
