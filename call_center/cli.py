"""CLI entrypoint for the call center simulation."""

from __future__ import annotations

import argparse
import logging
import sys

from call_center.engine import CallCenterSimulation
from call_center.validation import validate_simulation_params

logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Call Center Simulation")
    parser.add_argument(
        "number_of_freshers", type=int, help="Number of freshers in the call center"
    )
    parser.add_argument("run_time", type=int, help="Total run time of the simulation")
    parser.add_argument(
        "min_calls_per_wave", type=int, help="Minimum number of calls per wave"
    )
    parser.add_argument(
        "max_calls_per_wave", type=int, help="Maximum number of calls per wave"
    )
    parser.add_argument(
        "min_sleep_interval", type=int, help="Minimum sleep interval between waves"
    )
    parser.add_argument(
        "max_sleep_interval", type=int, help="Maximum sleep interval between waves"
    )
    parser.add_argument("min_call_duration", type=int, help="Minimum call duration")
    parser.add_argument("max_call_duration", type=int, help="Maximum call duration")
    parser.add_argument(
        "--seed", type=int, default=None, help="Optional RNG seed for reproducibility"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        validate_simulation_params(
            args.number_of_freshers,
            args.run_time,
            (args.min_calls_per_wave, args.max_calls_per_wave),
            (args.min_sleep_interval, args.max_sleep_interval),
            (args.min_call_duration, args.max_call_duration),
        )
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))
        return 2
    except SystemExit as exc:
        return int(exc.code or 0)

    sim = CallCenterSimulation()
    sim.set(
        args.number_of_freshers,
        args.run_time,
        (args.min_calls_per_wave, args.max_calls_per_wave),
        (args.min_sleep_interval, args.max_sleep_interval),
        (args.min_call_duration, args.max_call_duration),
        seed=args.seed,
    )

    try:
        sim.run_simulation()
    except KeyboardInterrupt:
        print("\nSimulation interrupted.")
        sim.stop()
        return 130
    except Exception:
        logging.error("Unhandled exception in main", exc_info=True)
        print("An error occurred. Check logs for details.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
