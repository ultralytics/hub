# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

"""Run scheduled HUB export checks with per-format reporting."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass

from ultralytics import checks, hub

POLL_DELAYS = (30, 60, 90, 120, 240, 360)
TOTAL_TIMEOUT_SECONDS = 55 * 60
REQUIRED_FORMATS = (
    "torchscript",
    "onnx",
    "openvino",
    "coreml",
    "saved_model",
    "pb",
    "tflite",
    "tfjs",
    "paddle",
    "ultralytics_tflite",
    "ultralytics_coreml",
    "ncnn",
)
OPTIONAL_FORMATS = ("edgetpu", "engine")


@dataclass
class ExportResult:
    name: str
    required: bool
    ok: bool
    attempts: int
    detail: str


def poll_export(model_id: str, name: str, required: bool, deadline: float) -> ExportResult:
    """Start one export and poll until it succeeds or exhausts the retry window."""
    if time.monotonic() >= deadline:
        detail = "skipped because the CI timeout budget was exhausted"
        print(f"{name}: {detail}", flush=True)
        return ExportResult(name, required, False, 0, detail)

    print(f"Starting {name} export...", flush=True)
    try:
        hub.export_model(model_id, format=name)
    except Exception as e:
        return ExportResult(name, required, False, 0, f"start failed: {e}")

    detail = "no status returned"
    for attempt, delay in enumerate(POLL_DELAYS, start=1):
        if time.monotonic() + delay >= deadline:
            detail = "stopped before the CI timeout budget was exhausted"
            print(f"{name}: {detail}", flush=True)
            return ExportResult(name, required, False, attempt - 1, detail)
        time.sleep(delay)
        try:
            export = hub.get_export(model_id, format=name)
        except Exception as e:
            detail = f"poll failed: {e}"
            print(f"{name}: attempt {attempt}/{len(POLL_DELAYS)} {detail}", flush=True)
            continue

        if export.get("success"):
            print(f"{name}: done", flush=True)
            return ExportResult(name, required, True, attempt, "success")

        detail = f"success={export.get('success')}"
        print(f"{name}: attempt {attempt}/{len(POLL_DELAYS)} {detail}", flush=True)

    return ExportResult(name, required, False, len(POLL_DELAYS), detail)


def write_summary(results: list[ExportResult]) -> None:
    """Append a compact export table to the GitHub step summary."""
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    rows = [
        "### HUB export summary",
        "",
        "| Format | Required | Result | Attempts | Detail |",
        "| --- | --- | --- | --- | --- |",
    ]
    for result in results:
        rows.append(
            f"| {result.name} | {'yes' if result.required else 'no'} | "
            f"{'pass' if result.ok else 'fail'} | {result.attempts} | {result.detail} |"
        )

    with open(summary_path, "a", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")


def main() -> None:
    checks()
    model_id = os.environ["MODEL_ID"]
    deadline = time.monotonic() + TOTAL_TIMEOUT_SECONDS
    results = [poll_export(model_id, name, True, deadline) for name in REQUIRED_FORMATS] + [
        poll_export(model_id, name, False, deadline) for name in OPTIONAL_FORMATS
    ]

    write_summary(results)

    failed_required = [result for result in results if result.required and not result.ok]
    failed_optional = [result for result in results if not result.required and not result.ok]
    for result in failed_optional:
        print(f"::warning::Optional HUB export {result.name} failed after {result.attempts} attempts: {result.detail}")
    if failed_required:
        names = ", ".join(result.name for result in failed_required)
        raise AssertionError(f"Required HUB exports failed: {names}")


if __name__ == "__main__":
    main()
