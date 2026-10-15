# Publishing a release (maintainers)

A release is an **xdelta patch from the untouched Special Vocal Version** plus a checksum file and the movie-swap
script. No ISO, no movie and no game file is ever uploaded.

## Versions

- `0.0.x`: internal test builds (every build gets the next number; never reuse one).
- `0.x.y`: public releases. The first public release should be the first build that passes the in-game test list
  in [STATUS.md](STATUS.md#what-to-test). Until then, publish only as a GitHub **pre-release**, with the known issues
  in the notes.

## Checklist

### 1. Build, audit, test

```
$env:PYTHONIOENCODING = 'utf-8'
.venv\Scripts\python.exe tools\ace2\build.py --version 0.1.0
.venv\Scripts\python.exe tools\ace2\build.py --version 0.1.0 --write
.venv\Scripts\python.exe tools\ace2\audit_iso.py work\output\ACE2-EN-0.1.0.iso
```

The audit must end in `PASS`. Then test the image in PCSX2.

### 2. Changelogs

Add the version to `CHANGELOG.md` (English, for players) and `docs/CHANGELOG.md` (Portuguese working log), with the
build SHA-256 from `work/output/ACE2-EN-0.1.0.json`. Update [STATUS.md](STATUS.md).

### 3. Install xdelta3

- Windows: download `xdelta3-3.0.11-x86_64.exe.zip` from
  [github.com/jmacd/xdelta-gpl/releases/tag/v3.0.11](https://github.com/jmacd/xdelta-gpl/releases/tag/v3.0.11)
  (the releases so far were made with 3.0.11, the version most patcher front-ends are built on), extract it, and
  either rename it to `xdelta3.exe` and put it on `PATH`, or pass its path with `--xdelta3`.
- Linux: `sudo apt install xdelta3`. macOS: `brew install xdelta`.

### 4. Make the patch

```
.venv\Scripts\python.exe tools\ace2\make_patch.py --version 0.1.0
```

(`--xdelta3 C:\path\to\xdelta3.exe` if it is not on `PATH`.) It:

1. copies the build and puts the **Special Vocal** opening back (`swap_movie.py`), so the patch carries no 2006
   movie;
2. encodes `work/release/ACE2-EN-0.1.0.xdelta` against the untouched Special Vocal ISO (`xdelta3 -e -9 -B 1 GB`);
3. decodes the patch again and checks the result byte for byte;
4. recomputes what a player gets after `swap_movie.py` with the 2006 disc and checks it equals the build's SHA-256;
5. writes `work/release/ACE2-EN-0.1.0-SHA256.txt` (input disc, optional 2006 disc, patch, output with each opening,
   both movies).

Delete `work/release/ACE2-EN-0.1.0-svv-opening.iso` afterwards; it is only the check copy. `work/release/` is
ignored by git.

### 5. Commit and tag

```
git add -A
git status            # no .iso, .xdelta or .PSS must appear
git commit -m "Release 0.1.0"
git tag -a v0.1.0 -m "English patch 0.1.0"
git push origin main --tags
```

### 6. Create the GitHub release

On GitHub: **Releases → Draft a new release** → choose tag `v0.1.0` → title
`ACE2 English Patch 0.1.0` → paste the notes (template below) → attach:

- `work/release/ACE2-EN-0.1.0.xdelta`
- `work/release/ACE2-EN-0.1.0-SHA256.txt`
- `tools/ace2/swap_movie.py`

Tick **Set as a pre-release** while the build has known issues → **Publish release**.

Or with the GitHub CLI:

```
gh release create v0.1.0 work/release/ACE2-EN-0.1.0.xdelta work/release/ACE2-EN-0.1.0-SHA256.txt tools/ace2/swap_movie.py --title "ACE2 English Patch 0.1.0" --notes-file notes.md --prerelease
```

GitHub accepts assets up to 2 GiB each; the patch is far smaller.

## Release notes template

```markdown
English fan translation of **Another Century's Episode 2 – Special Vocal Version** (PS2, SLPS-25829).
AI translation (Google AI agent) with automatic validation and line-by-line AI review (Claude); see the README.

## Files
- `ACE2-EN-<version>.xdelta` – apply to your untouched Special Vocal Version ISO
- `ACE2-EN-<version>-SHA256.txt` – checksums of the input and of every output
- `swap_movie.py` – optional: puts the original 2006 "Glorious" opening on the patched ISO (needs your 2006 disc and Python 3.8+)

## How to install
Step by step: docs/INSTALL_PATCH.md. In short:
1. Check your ISO: SHA-256 `efd791e7c50af2ec476f4026c6bda57fcf6d64babf20c12174db642b54941741`.
2. `xdelta3 -d -s "<your SVV>.iso" ACE2-EN-<version>.xdelta ACE2-EN-<version>.iso`
   (or Delta Patcher).
3. Optional "Glorious" opening: `python swap_movie.py --target ACE2-EN-<version>.iso --source "<your 2006>.iso" --out ACE2-EN-<version>-Glorious.iso --sha`

## Changes
<copy from CHANGELOG.md>

## Known issues
<copy from docs/STATUS.md>

No game data is included. You need your own copy of the game.
```
