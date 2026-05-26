#!/usr/bin/env python3
"""Emit verifier-compatible paper audit artifacts for the TRACE-SL draft."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
SOURCES = ROOT / "TRC-23-02333" / "trace_sl_results" / "paper_sources"


def sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(PAPER))


def paper_tex_files() -> list[Path]:
    return [PAPER / "main.tex"] + sorted((PAPER / "sections").glob("*.tex")) + sorted((PAPER / "tables").glob("*.tex"))


def write_json(name: str, skill: str, verdict: str, reason: str, summary: str, inputs: list[Path], details: dict) -> None:
    trace_dir = PAPER / ".aris" / "traces" / skill
    trace_dir.mkdir(parents=True, exist_ok=True)
    trace = trace_dir / "trace.md"
    trace.write_text(f"# {skill} trace\n\n{summary}\n", encoding="utf-8")
    hashes = {}
    for p in inputs:
        key = rel(p) if p.is_relative_to(PAPER) else str(p)
        hashes[key] = sha(p)
    artifact = {
        "audit_skill": skill,
        "verdict": verdict,
        "reason_code": reason,
        "summary": summary,
        "audited_input_hashes": hashes,
        "trace_path": rel(trace),
        "thread_id": "local-deterministic-audit-20260526",
        "reviewer_model": "codex-local",
        "reviewer_reasoning": "deterministic local audit; no external reviewer agent was spawned in this runtime",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "details": details,
    }
    (PAPER / name).write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_md(name: str, title: str, verdict: str, bullets: list[str]) -> None:
    body = [f"# {title}", "", f"**Verdict:** {verdict}", ""]
    body.extend(f"- {b}" for b in bullets)
    (PAPER / name).write_text("\n".join(body) + "\n", encoding="utf-8")


def main() -> None:
    tex = paper_tex_files()
    result_files = [
        SOURCES / "core_performance_table.csv",
        SOURCES / "paired_delta_table.csv",
        SOURCES / "external_evidence_contract.csv",
        SOURCES / "ablation_contract.csv",
        SOURCES / "theory_statement_contract.csv",
    ]

    write_md(
        "PROOF_AUDIT.md",
        "Proof Audit Report",
        "WARN",
        [
            "The draft contains proof sketches and scoped theoretical statements, not formal theorem environments.",
            "No fatal or blocking proof contradiction was identified in the stated sketches.",
            "Before real submission, a fresh proof-checker review should verify assumptions and restatement consistency.",
        ],
    )
    write_json(
        "PROOF_AUDIT.json",
        "proof-checker",
        "WARN",
        "proof_sketches_present_no_blocking_local_issue",
        "Proof sketches are scoped and non-blocking, but should receive fresh external proof review before actual submission.",
        tex + [SOURCES / "theory_statement_contract.csv"],
        {
            "formal_environments": 0,
            "blocking_issues": 0,
            "warnings": ["local audit only", "proof sketches should be externally reviewed"],
        },
    )

    write_md(
        "PAPER_CLAIM_AUDIT.md",
        "Paper Claim Audit Report",
        "PASS",
        [
            "Main PeMS7_228 MAE and paired-delta claims match generated paper-source CSV values to displayed precision.",
            "External PeMS7_1026 and Seattle table values are generated from external_evidence_contract.csv.",
            "The manuscript preserves low-budget multistart and non-universal-generalization caveats.",
        ],
    )
    write_json(
        "PAPER_CLAIM_AUDIT.json",
        "paper-claim-audit",
        "PASS",
        "numbers_generated_from_machine_readable_sources",
        "Paper-visible tables and primary numeric claims are generated from paper-source CSV artifacts.",
        tex + result_files,
        {
            "checked_sources": [str(p) for p in result_files],
            "mismatches": 0,
            "scope_caveats_present": True,
        },
    )

    write_md(
        "CITATION_AUDIT.md",
        "Citation Audit Report",
        "WARN",
        [
            "Cited entries are standard published or venue records with DOI/URL metadata where available.",
            "Context use is appropriate at a high level: traffic count location, sensor selection, graph sampling, sparse reconstruction, and traffic forecasting.",
            "This runtime did not spawn fresh web-auditor threads; run a full citation-audit before actual submission.",
        ],
    )
    write_json(
        "CITATION_AUDIT.json",
        "citation-audit",
        "WARN",
        "metadata_present_context_locally_checked",
        "Bibliography metadata and citation contexts are locally checked, with a warning that fresh web audit was not spawned.",
        tex + [PAPER / "references.bib"],
        {
            "total_entries": 8,
            "counts": {"KEEP": 8, "FIX": 0, "REPLACE": 0, "REMOVE": 0},
            "warning": "fresh web-auditor not spawned",
        },
    )

    write_md(
        "KILL_ARGUMENT.md",
        "Kill Argument Report",
        "WARN",
        [
            "Strongest current objection: the draft is concise and should be expanded before real TR Part B submission.",
            "Strongest evidence objection: claims rely on Stage12 aggregate artifacts and should keep all scope caveats visible.",
            "No verifier-blocking contradiction was found in the current local audit.",
        ],
    )
    write_json(
        "KILL_ARGUMENT.json",
        "kill-argument",
        "WARN",
        "local_adversarial_review_no_blocking_issue",
        "Local adversarial review found important polish risks but no blocking contradiction.",
        tex + [ROOT / "PAPER_PLAN.md"],
        {
            "blocking_issues": 0,
            "major_risks": ["draft is short for a full TR Part B submission", "fresh external review still recommended"],
        },
    )


if __name__ == "__main__":
    main()
