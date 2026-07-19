"""Single source of truth for simulation input validation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Bounds:
    max_freshers: int = 1000
    max_run_time: int = 86_400
    max_calls_per_wave: int = 10_000
    max_sleep_interval: int = 86_400
    max_call_duration: int = 86_400


BOUNDS = Bounds()


def _require_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an int, got {type(value).__name__}")
    return value


def _require_number(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")
    return float(value)


def validate_range(
    name: str,
    low: int,
    high: int,
    *,
    min_low: int = 0,
    max_high: int | None = None,
    high_must_be_positive: bool = False,
) -> tuple[int, int]:
    low = _require_int(f"{name}[0]", low)
    high = _require_int(f"{name}[1]", high)
    if low < min_low:
        raise ValueError(f"{name} minimum must be >= {min_low}")
    if low > high:
        raise ValueError(f"{name} minimum cannot exceed maximum")
    if high_must_be_positive and high <= 0:
        raise ValueError(f"{name} maximum must be strictly positive")
    if max_high is not None and high > max_high:
        raise ValueError(f"{name} maximum must be <= {max_high}")
    return low, high


def validate_simulation_params(
    number_of_freshers: object,
    run_time: object,
    min_max_calls_per_wave: tuple[object, object],
    min_max_sleep_interval: tuple[object, object],
    min_max_call_duration: tuple[object, object],
) -> tuple[int, float, tuple[int, int], tuple[int, int], tuple[int, int]]:
    n = _require_int("number_of_freshers", number_of_freshers)
    if not (0 < n <= BOUNDS.max_freshers):
        raise ValueError(
            f"number_of_freshers must be in 1..{BOUNDS.max_freshers}"
        )

    rt = _require_number("run_time", run_time)
    if not (0 < rt <= BOUNDS.max_run_time):
        raise ValueError(f"run_time must be in (0, {BOUNDS.max_run_time}]")

    calls = validate_range(
        "min_max_calls_per_wave",
        min_max_calls_per_wave[0],  # type: ignore[index]
        min_max_calls_per_wave[1],  # type: ignore[index]
        max_high=BOUNDS.max_calls_per_wave,
    )
    sleep = validate_range(
        "min_max_sleep_interval",
        min_max_sleep_interval[0],  # type: ignore[index]
        min_max_sleep_interval[1],  # type: ignore[index]
        max_high=BOUNDS.max_sleep_interval,
        high_must_be_positive=True,
    )
    duration = validate_range(
        "min_max_call_duration",
        min_max_call_duration[0],  # type: ignore[index]
        min_max_call_duration[1],  # type: ignore[index]
        min_low=0,
        max_high=BOUNDS.max_call_duration,
    )

    return n, rt, calls, sleep, duration
