# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

This repository (AGPL-3.0) is the historical home of Ultralytics HUB, which shut down on July 31, 2026 and was replaced by [Ultralytics Platform](https://platform.ultralytics.com). It now holds only the Platform redirect READMEs, sample datasets, and GitHub workflows.

## Core Principles (CRITICAL)

**Less is more. The simplest solution is the best solution.** The action hierarchy for every change: **Delete > Replace > Add**.

1. **Solve at the owner**: Put behavior in the code path that owns or observes it. For fixes, never guard a symptom with a staleness check, initialization flag, skip-first-call branch, or `try/except` around broken logic; relocate the trigger and delete the wrong path. For features, extend the existing owner rather than creating a parallel abstraction.
2. **Search and reuse first**: Search the whole repository before creating a feature, component, helper, workflow, or utility. Reuse or adapt what exists, consolidate in-scope duplication in the shared owner, and delete duplicate paths. Three similar lines beat a helper nobody else calls.
3. **Delete and modify existing code before creating new code**: Bugfixes are net-negative by default unless deletion and relocation are demonstrably impossible. A new file must first prove it cannot fit cleanly in an existing owner.
4. **Keep scope minimal**: Implement only the simplest complete solution. Avoid impossible-state handling, speculative flags, compatibility shims, policy scaffolding, and unrelated cleanup. Tests are out of scope by default — rely on existing coverage and focused validation; only an uncovered, high-risk regression path justifies minimal new test code.
5. **Ship zero-regression, production-ready changes**: Understand what you remove instead of retaining broken code as insurance. Remove unused imports, functions, types, files, and comments; run relevant cleanup checks; and thoroughly debug and validate the changed owner. Do not break existing features or workflows unless the PR intentionally removes them with evidence.

**Review gate:** for every addition, the reviewer decides whether deleting or changing existing code would have fixed the problem instead — if it would, that is a blocking finding. A missing or thin PR description is never itself a finding.

NEVER push to `main`. NEVER force push. Always start work in a new git worktree (`git worktree add`) on a feature branch and open a PR — never edit the primary checkout directly, it may hold in-flight work.

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Review the full diff in-session against the Core Principles, performance, and the review gate above, then batch the fixes into one commit and push. After each round of bot or human commits, pull and resume the same reviewer on `<last-reviewed-sha>..HEAD` plus anything that delta could have invalidated. Repeat until the local head matches the live head.
3. Hand off or merge only on a clean final pass: one cold full-diff review returning LGTM with no findings, on a head that is still live at merge time.
4. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never reset or revert commits you did not author.
5. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Format/lint (mirrors Ultralytics Actions; source of truth: action.yml in ultralytics/actions)
npx prettier --write --print-width 120 "**/*.{md,yml,yaml,json}"
```

- There is no unit-test suite, coverage, package build, or live HUB CI. The manually dispatched lychee workflow in `links.yml` checks repository links.

## Architecture

This is the historical repository for Ultralytics HUB, which was deprecated and shut down on July 31, 2026, and fully replaced by Ultralytics Platform. The managed HUB-to-Platform migration was completed during Q2 2026 before shutdown; HUB APIs, services, and API keys no longer work. The repository contains no Python package: just the Platform redirect READMEs, extracted sample datasets in `example_datasets/` (YOLO-format coco8/coco8-human/coco8-pose/coco8-seg/dota8 and a classification folder layout in imagenet10), and `.github/`. There is no release or publish pipeline — nothing is versioned or shipped from here.

`format.yml` runs Ultralytics Actions on PR events: it pushes auto-format commits to PR branches and adds AI labels and summaries. `links.yml` checks links by manual dispatch, and `cla.yml` handles CLA signing.

## Conventions

- License header (`# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`) tops every `.py`/`.yml` file — Ultralytics Actions adds it automatically; don't add or revert it manually.
- Prettier formats Markdown/YAML/JSON.
- Do not add or recommend HUB APIs, training, inference, exports, or API keys, and never present the completed Q2 2026 migration as ongoing. Platform behavior is owned and tested outside this historical repository.
- No repo version, dependency installation, or automated dependency update exists; the repository is a historical Platform redirect.
- `README.md` and `README.zh-CN.md` mirror each other — apply content edits to both.
