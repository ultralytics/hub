# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

Respecting these principles is critical for every PR.

**Less is more. The simplest solution is the best solution.**

The action hierarchy for every change: **Delete > Replace > Add**. The best code change is a deletion. The second best is modifying what exists. Adding new code is the last resort.

1. **Minimal**: The simplest solution that works. Do not over-engineer, over-abstract, or add code just in case. Three similar lines beat a premature abstraction. Avoid error handling for impossible states, feature flags, compatibility shims, or policy scaffolding unless they are truly required.
2. **Solve at the source**: Do not hack fixes. Solve problems at their root. If something is broken, fix or remove the broken thing. Never patch over a broken abstraction, add workarounds, or add synchronization code for state that should not be duplicated.
3. **Delete ruthlessly**: When replacing code, delete what it replaced. Remove unused imports, functions, types, files, and commented-out code. Git preserves history. Run the repo's relevant dead-code or cleanup check when available.
4. **Replace > Add**: Modify existing code over adding new code. Edit existing files, extend existing components or functions with minimal parameters, and reuse existing utilities. If creating a new file, first prove it cannot fit cleanly in an existing file.
5. **Check existing**: Search the entire repo before creating anything new. If a feature, component, helper, responder, workflow, or utility already solves a similar problem, reuse or adapt it and delete the duplicate path.
6. **Deduplicate**: Do not duplicate existing code when updating the repo. Consolidate or refactor duplicates you find when it is in scope and low risk.
7. **Zero Regression**: Do not break existing features or workflows unless the PR intentionally removes them with evidence.
8. **Production ready**: All changes must be thoroughly debugged, validated, and production ready.

**When fixing bugs, ask: "What can I delete?" before "What can I replace?" before "What should I add?"**

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Launch an independent adversarial review agent with cold context (just the PR diff and this file) to hunt for bugs, regressions, and Core Principles violations — use the Codex CLI, one fresh `codex exec` run per round. Fix, push, and repeat until a fresh run reports LGTM.
3. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never force-push, reset, or revert commits you did not author.
4. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Install (matches ci.yml; always uv pip, never bare pip)
uv pip install --system ultralytics hub-sdk --extra-index-url https://download.pytorch.org/whl/cpu

# Environment check (run by CI after install)
yolo checks

# CI integration tests (live HUB API, need ULTRALYTICS_HUB_API_KEY + ULTRALYTICS_HUB_MODEL_ID)
yolo login "$API_KEY"                     # HUB login
python .github/scripts/run_hub_exports.py # export sweep, reads MODEL_ID env var

# Format/lint (mirrors Ultralytics Actions; source of truth: action.yml in ultralytics/actions)
ruff check --fix --unsafe-fixes --extend-select F,I,D,UP,RUF,FA --target-version py39 --ignore D100,D104,D203,D205,D212,D213,D401,D406,D407,D413,RUF001,RUF002,RUF012 .
ruff format --line-length 120 .
npx prettier --write --print-width 120 "**/*.{yml,yaml,json}"
```

- CI matrix (`.github/workflows/ci.yml`): ubuntu-latest, Python 3.11 only.
- There is no unit-test suite, coverage, package build, or in-repo lint config — the only "tests" are the live HUB API steps in `ci.yml`.

## Architecture

This is the legacy support repository for Ultralytics HUB (deprecated, winding down at the end of July 2026) and contains no Python package: just the READMEs, the `hub.ipynb` Colab notebook, YOLO-format sample archives in `example_datasets/`, `requirements.txt` (single dependency: `ultralytics`), and `.github/`. There is no release or publish pipeline — nothing is versioned or shipped from here.

CI (`ci.yml`, name "HUB CI") runs on push/PR to `main`, `workflow_dispatch`, and a nightly 02:00 UTC cron. Its test steps call the live HUB API (reset + train a model, inference API request) and are gated on repo secrets: missing secrets skip the steps on `pull_request` (e.g. fork PRs) but fail the run for all other events. The export sweep (`.github/scripts/run_hub_exports.py`) runs only on `schedule`/`workflow_dispatch`, and a Slack alert fires only on first-attempt `schedule`/`push` failures in `ultralytics/hub`.

`format.yml` runs Ultralytics Actions on issue opens and PR events: it pushes auto-format commits to PR branches and adds AI labels, summaries, and a first-issue response. `links.yml` (nightly/dispatch) checks links with lychee; `cla.yml` and `stale.yml` handle CLA signing and stale issues.

## Conventions

- License header (`# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`) tops every `.py`/`.yml` file — Ultralytics Actions adds it automatically; don't add or revert it manually.
- Python follows Ruff formatting at line length 120 with a docstring on every function (see `.github/scripts/run_hub_exports.py`); Prettier formats Markdown/YAML/JSON.
- All CI test steps hit the live HUB network — nothing runs offline, so don't expect them to pass locally without HUB credentials.
- No repo version exists to bump; Dependabot (monthly) raises the `ultralytics` floor in `requirements.txt` and workflow action tags.
- `README.md` and `README.zh-CN.md` mirror each other — apply content edits to both.
