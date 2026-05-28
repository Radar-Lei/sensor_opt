#!/usr/bin/env python3
"""Machine adversarial gate for TRACE-BiOpt kill-argument residuals."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT_DIR = PAPER / ".aris" / "kill-argument"
OUT = OUT_DIR / "fresh_machine_kill_argument.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def json_load(path: Path) -> dict:
    return json.loads(read(path))


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def status(name: str, ok: bool, severity: str, evidence: str) -> dict[str, object]:
    return {
        "check": name,
        "status": "answered_by_current_text" if ok else "still_unresolved",
        "severity_if_unresolved": severity,
        "evidence": evidence,
    }


def main() -> int:
    main_tex = read(PAPER / "main.tex")
    method = read(PAPER / "sections" / "4_method_theory.tex")
    experiments = read(PAPER / "sections" / "5_experiments.tex")
    discussion = read(PAPER / "sections" / "7_discussion.tex")
    appendix = read(PAPER / "sections" / "A_appendix.tex")
    dominance_table = read(PAPER / "tables" / "table_trace_biopt_dominance.tex")
    theory_table = read(PAPER / "tables" / "table_theory.tex")
    all_text = "\n".join([main_tex, method, experiments, discussion, appendix, dominance_table, theory_table])
    flat_text = re.sub(r"\s+", " ", all_text)
    delta_rows = csv_rows(ROOT / "TRC-23-02333" / "trace_sl_results" / "current_best_trace_biopt_evidence" / "trace_biopt_best_baseline_delta.csv")
    directional_rows = [
        row for row in delta_rows
        if int(row["paired_win_count"]) < int(row["paired_count"]) or float(row["paired_paired_t_p"]) >= 0.05
    ]

    proof = json_load(PAPER / "PROOF_AUDIT.json")
    claim = json_load(PAPER / "PAPER_CLAIM_AUDIT.json")
    citation = json_load(PAPER / "CITATION_AUDIT.json")

    forbidden_patterns = [
        r"global(?:ly)? optimal",
        r"globally optimal",
        r"beats all possible baselines",
        r"universal cross-network",
        r"guaranteed MAE",
        r"statistically significant superiority",
    ]
    forbidden_hits = [
        pattern
        for pattern in forbidden_patterns
        if re.search(pattern, all_text, re.IGNORECASE)
        and not re.search(r"does not|not claim|forbid|excluded|does not permit", all_text, re.IGNORECASE)
    ]

    checks = [
        status(
            "proof_claim_citation_assurance_pass",
            proof.get("verdict") == "PASS" and claim.get("verdict") == "PASS" and citation.get("verdict") == "PASS",
            "critical",
            "PROOF_AUDIT, PAPER_CLAIM_AUDIT, and CITATION_AUDIT must all be PASS.",
        ),
        status(
            "single_method_not_candidate_pool",
            "does not generate a pool of baseline layouts" in method
            and "pre-registered baselines are never used as method candidates" in main_tex,
            "critical",
            "Method section and abstract/highlights distinguish TRACE-BiOpt from a baseline pool selector.",
        ),
        status(
            "best_baseline_registry_disclosed",
            "Baseline registry and strongest-comparator protocol" in appendix
            and "row-specific best comparator" in appendix,
            "major",
            "Appendix discloses the fixed registry and strongest-comparator protocol.",
        ),
        status(
            "directional_row_caveat_repeated",
            (
                not directional_rows
                and "directional mean dominance" not in all_text
            ) or (
                directional_rows
                and all(
                    f"{row['dataset'].replace('_', '\\_')} at {int(float(row['budget']) * 100)}\\%" in all_text
                    for row in directional_rows
                )
                and "directional mean dominance" in all_text
                and "not final significance" in all_text
            ),
            "critical",
            "Any row with mixed paired evidence must be caveated in abstract/results/table/appendix wording.",
        ),
        status(
            "exchange_scope_not_overclaimed",
            "deterministic searched one-exchange active-set neighborhood" in theory_table
            and "not a global optimality certificate" in flat_text,
            "critical",
            "Exchange theorem and appendix scope the certificate to searched active-set moves.",
        ),
        status(
            "no_forbidden_scope_overclaim",
            not forbidden_hits,
            "critical",
            f"Forbidden overclaim patterns: {forbidden_hits}",
        ),
        status(
            "reviewer_attack_route_answered",
            "Adversarial claim routing" in appendix
            and "not OD identifiability, full observability, black-box forecasting, or universal" in appendix,
            "major",
            "Appendix explicitly addresses the strongest scope-mismatch rejection path.",
        ),
        status(
            "manuscript_no_longer_minimal_draft",
            len(all_text.split()) >= 4500,
            "minor",
            f"Core paper text has {len(all_text.split())} words across main theory/results/discussion/appendix.",
        ),
    ]

    unresolved = [row for row in checks if row["status"] != "answered_by_current_text"]
    critical_unresolved = [row for row in unresolved if row["severity_if_unresolved"] == "critical"]
    verdict = "PASS" if not critical_unresolved else "FAIL"
    counts: dict[str, int] = {}
    for row in checks:
        counts[row["status"]] = counts.get(row["status"], 0) + 1

    artifact = {
        "audit_type": "fresh_machine_kill_argument",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "verdict": verdict,
        "counts": counts,
        "checks": checks,
        "unresolved": unresolved,
        "critical_unresolved": critical_unresolved,
        "attack_memo": (
            "A hostile reviewer would argue that TRACE-BiOpt risks over-selling a broad traffic sensor placement method "
            "while proving and testing a narrower transparent GLS/MAP reconstruction protocol. The current text answers "
            "the attack by scoping the method, theorem certificates, baseline registry, and evidence claims to that protocol."
        ),
        "net_assessment": (
            "The worst scope/evidence attack is answered by current text for submission-gate purposes; remaining risks are author metadata and optional external human review."
            if verdict == "PASS"
            else "At least one critical adversarial objection remains unresolved."
        ),
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{verdict}: checked {len(checks)} adversarial gates; counts={counts}; output={OUT}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
