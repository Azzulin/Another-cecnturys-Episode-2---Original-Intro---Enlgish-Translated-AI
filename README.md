# Another Century's Episode 2 — English Translation (AI-assisted) + Original "Glorious" Opening

A fan translation of **Another Century's Episode 2 — Special Vocal Version** (PS2, Japan, SLPS-25829) into English,
plus a tool that puts the **original 2006 opening movie with the song "Glorious"** back on the Special Vocal Version.

> **Status: test builds (0.0.x).** Every text table of the game is in English (campaign 6,822/6,822 lines, menus
> 2,171/2,171, extra missions, tutorial, HUD, names). The latest build (0.0.10) has **not been tested in game yet**,
> and 0.0.9 had two known problems (some menu labels blank, a crash when pausing a mission). Read
> [docs/STATUS.md](docs/STATUS.md) before playing.

This repository contains **no game data**. You need your own copy of the game. Patches are published under
[Releases](../../releases); the tools here rebuild everything from your own discs.

## What do you want to do?

| I want to… | Read |
|---|---|
| Play in English: apply the patch to my ISO | [docs/INSTALL_PATCH.md](docs/INSTALL_PATCH.md) |
| Get the "Glorious" opening on my Special Vocal Version (English **or** untouched Japanese) | [docs/GLORIOUS_OPENING.md](docs/GLORIOUS_OPENING.md) |
| Build the English ISO myself from source | [docs/BUILD_FROM_SOURCE.md](docs/BUILD_FROM_SOURCE.md) |
| Fix or change the English text, or make my own translation | [docs/MAKE_YOUR_OWN_TRANSLATION.md](docs/MAKE_YOUR_OWN_TRANSLATION.md) |
| Understand how the AI translation was produced and reviewed | [docs/AI_TRANSLATION_WORKFLOW.md](docs/AI_TRANSLATION_WORKFLOW.md) |
| Know the file formats and how the disc is rebuilt | [docs/TECHNICAL_REFERENCE.md](docs/TECHNICAL_REFERENCE.md) |
| Publish a release (maintainers) | [docs/RELEASING.md](docs/RELEASING.md) |
| See what is done, what is broken, what is left | [docs/STATUS.md](docs/STATUS.md), [CHANGELOG.md](CHANGELOG.md) |

## The two discs

| Disc | Serial | Used for | SHA-256 of the image (2048-byte sectors) |
|---|---|---|---|
| Another Century's Episode 2 — **Special Vocal Version** (Japan) | SLPS-25829 | **Base of everything.** The patch applies to this disc. | `efd791e7c50af2ec476f4026c6bda57fcf6d64babf20c12174db642b54941741` |
| Another Century's Episode 2 (Japan), **original 2006 release** | SLPS-25623 | Optional. Only its opening movie (`MOVIE001.PSS`, "Glorious") is used. | `c9dcaeda5e466120c777d771639e4b247a787c84f3cc7131322f8e6dd390eef5` |

The Special Vocal Version replaced the opening song. Both discs store the opening as `/MOVIE0/MOVIE001.PSS` with
**exactly the same size** (275,251,204 bytes), so the movie can be swapped as a whole file without rebuilding the disc
([docs/GLORIOUS_OPENING.md](docs/GLORIOUS_OPENING.md)). The release patch never contains that movie: you take it from
your own 2006 disc.

## How the translation was made (short version)

- The game's text was extracted from scratch from the Special Vocal Version (10,695 unique lines in 934 text tables).
- An **external AI translator (a Google AI agent)** translated batches of 80 lines in play order, with a glossary,
  per-series voice notes and the surrounding lines as context. It only ever wrote its answers to one folder.
- **Claude (Anthropic), working in Claude Code**, did everything else: the tools, the font work, automatic
  validation of every batch, a line-by-line meaning review against the Japanese (1,486 corrections), the
  builds and the audits.
- Every build is checked by an independent auditor (`tools/ace2/audit_iso.py`): all control codes in the original
  order, every pointer valid, every file not meant to change byte-identical to the original disc.

This is a machine translation with automated and AI review, not a professional human translation. Expect awkward
lines; reports are welcome (see [docs/MAKE_YOUR_OWN_TRANSLATION.md](docs/MAKE_YOUR_OWN_TRANSLATION.md#reporting-a-bad-line)).
Details: [docs/AI_TRANSLATION_WORKFLOW.md](docs/AI_TRANSLATION_WORKFLOW.md).

## Repository layout

```
README.md, CHANGELOG.md     this file; release history in English
docs/*.md (English names)   English guides (this repo's documentation)
docs/ESTUDO_ACE2.md, docs/CHANGELOG.md, docs/RETOMADA.md, docs/REVISAO_PARALELA.md
                            the original working notes in Portuguese (the most detailed record of every decision)
AGENTS.md                   rules for AI assistants working in this folder (Portuguese)
requirements.txt            Python packages (numpy, pillow, pycdlib)
tools/ace2/                 the pipeline: extraction, fonts, validation, build, audit, movie swap, release patch
tools/research/             one-off research scripts (not used by the build)
work/translation/en/        one JSON per text table: Japanese source + English (the build input)
work/translation/en/_fill/  English per table, by row position (what translators and reviewers edit)
work/translation/agent/     the AI-translator work package: batches, returns, validation and review reports
work/translation/auto/      rows filled automatically (exact repeats / already-translated lines)
work/glossary/              names and terms with sources; name fixes applied by script
work/ui/                    measured text-box limits, texture census
work/proof/                 font atlas proofs (images)
work/output/                build reports (JSON); the ISOs themselves are not committed
```

## Requirements at a glance

- **Players:** the Special Vocal Version ISO, an xdelta patcher, and (for "Glorious") the 2006 ISO plus Python 3.8+.
- **Builders/translators:** Windows (the font generator uses Windows' TrueType fonts; see
  [BUILD_FROM_SOURCE](docs/BUILD_FROM_SOURCE.md#fonts) for other systems), Python 3.14, about 8 GB free disk space.
- **Emulator tested:** PCSX2 2.6.3.

## Credits and legal

- Translation pipeline, review and builds: Claude (Anthropic) with the project owner
  ([Azzulin](https://github.com/Azzulin)). Machine translation: Google AI agent.
- Format codecs (DATA.BIN binders, LZSS, text tables) were first written for the Another Century's Episode 3
  English patch (MIT) and adapted through the ACE1 project.
- Another Century's Episode 2 © BANPRESTO / FromSoftware; the robots and characters belong to their respective
  rights holders (Sunrise and others). This is an unofficial, non-commercial fan project. No game files, ISOs or
  movies are distributed here. Buy the game.
