# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

**Delete > Replace > Add.** Before writing any change, answer in order: what can I delete? what can I replace? only then, what must I add?

The most common agent failure in this repo is reaching for the locally-safest edit — a new guard, flag, or helper — instead of fixing ownership. These tripwires override that instinct:

1. **Never guard a symptom — relocate the trigger.** A fix that adds a condition to suppress bad behavior (a staleness check, an is-initialized flag, a skip-first-call guard, a try/except around broken logic) is wrong by default. Find the code path that should own the behavior, move the logic there, and delete the code that got it wrong. Example: a warning fired from stale state; the right fix was not a recency guard — it deleted the stale detection and moved the trigger into the code path that observes the event live.
2. **Bugfixes are net-negative by default.** A bugfix that adds more lines than it removes needs a one-sentence justification in the PR body naming why deletion and relocation were impossible.
3. **Search before creating anything.** This repo is small — workflows in `.github/workflows/`, one export script in `.github/scripts/`, two mirrored READMEs, and sample datasets. Before adding a workflow, step, or script, check whether the behavior already exists here or is already owned by the shared `ultralytics/actions` workflows (formatting, labeling, spelling, link-checking); reuse it instead of reimplementing. Avoid premature abstraction — three similar lines beat a helper nobody else calls.
4. **Deletion beats caution.** Zero regression means understanding the code you remove, not leaving it in place as insurance. Keeping broken or duplicated code "to be safe" is itself the regression: it is how repos rot. All changes must still ship debugged, validated, and production ready.

**Output gate:** every PR body must contain a `Deleted:` line naming the code removed (functions, branches, files, config). Features must name what they reused or consolidated. `Deleted: nothing` demands the rule-2 justification.

**Review gate:** adversarial reviewers must answer two questions before LGTM: (a) what could have been deleted instead of added? (b) does any added condition suppress a symptom rather than relocate a trigger? A finding on either blocks LGTM.

**This file is code — additions require deletions.** To add a rule here, remove or merge one. When everything is emphasized, nothing is.

**NEVER push to `main`. NEVER force push.** Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

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
npx prettier --write --print-width 120 "**/*.{md,yml,yaml,json}"
```

- CI matrix (`.github/workflows/ci.yml`): ubuntu-latest, Python 3.11 only.
- There is no unit-test suite, coverage, package build, or in-repo lint config — CI "tests" are the live HUB API steps in `ci.yml` plus the nightly lychee link checks in `links.yml`.

## Architecture

This is the legacy support repository for Ultralytics HUB (deprecated, winding down at the end of July 2026) and contains no Python package: just the READMEs, the `hub.ipynb` Colab notebook, sample datasets in `example_datasets/` (zips plus extracted directories: YOLO-format coco8/coco8-human/coco8-pose/coco8-seg/dota8 and a classification folder layout in imagenet10), `requirements.txt` (single dependency: `ultralytics`), and `.github/`. There is no release or publish pipeline — nothing is versioned or shipped from here.

CI (`ci.yml`, name "HUB CI") runs on push/PR to `main`, `workflow_dispatch`, and a nightly 02:00 UTC cron. Its test steps call the live HUB API (reset + train a model, inference API request) and are gated on repo secrets: missing secrets skip the steps on `pull_request` (e.g. fork PRs) but fail the run for all other events. The export sweep (`.github/scripts/run_hub_exports.py`) runs only on `schedule`/`workflow_dispatch`, and a Slack alert fires only on first-attempt `schedule`/`push` failures in `ultralytics/hub`.

`format.yml` runs Ultralytics Actions on issue opens and PR events: it pushes auto-format commits to PR branches and adds AI labels, summaries, and a first-issue response. `links.yml` (nightly/dispatch) checks links with lychee; `cla.yml` and `stale.yml` handle CLA signing and stale issues.

## Conventions

- License header (`# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`) tops every `.py`/`.yml` file — Ultralytics Actions adds it automatically; don't add or revert it manually.
- Python follows Ruff formatting at line length 120 with a docstring on every function (see `.github/scripts/run_hub_exports.py`); Prettier formats Markdown/YAML/JSON.
- All CI test steps hit the live HUB network — nothing runs offline, so don't expect them to pass locally without HUB credentials.
- No repo version exists to bump; Dependabot (monthly) raises the `ultralytics` floor in `requirements.txt` and workflow action tags.
- `README.md` and `README.zh-CN.md` mirror each other — apply content edits to both.
