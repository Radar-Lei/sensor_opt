import sys

from transparent_estimator_eval import main


def trace_biopt_main():
    if "--include-biopt" not in sys.argv:
        sys.argv.append("--include-biopt")
    main()


if __name__ == "__main__":
    trace_biopt_main()
