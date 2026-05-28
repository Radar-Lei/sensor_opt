"""TRACE-BiOpt CLI entry point.

Thin wrapper that invokes transparent_estimator_eval.main() with
``--include-biopt`` automatically appended.  All other flags are
forwarded unchanged to the transparent evaluator's argparse.

Usage examples:

    # Smoke test (small budget, one seed):
    python TRC-23-02333/trace_biopt.py \\
        --data-root TRC-23-02333/dataset/PeMS7_228 \\
        --budgets "0.10" \\
        --seeds 25 \\
        --include-baseline-portfolio \\
        --output-dir TRC-23-02333/trace_sl_results/example_trace_biopt

    # Full reproduction with baseline portfolio:
    python TRC-23-02333/trace_biopt.py \\
        --data-root TRC-23-02333/dataset/PeMS7_228 \\
        --include-baseline-portfolio \\
        --output-dir TRC-23-02333/trace_sl_results/stage15_biopt_allbudget_seed25

See ``python TRC-23-02333/transparent_estimator_eval.py --help`` for the
complete flag reference.
"""

import sys

from transparent_estimator_eval import main


def trace_biopt_main():
    if "--include-biopt" not in sys.argv:
        sys.argv.append("--include-biopt")
    main()


if __name__ == "__main__":
    trace_biopt_main()
