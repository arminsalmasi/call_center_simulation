"""Engine integration tests with deterministic seed and instant sleep."""

import pytest

from call_center.engine import CallCenterSimulation
from call_center.validation import validate_simulation_params


def test_validate_rejects_bad_types():
    with pytest.raises(TypeError):
        validate_simulation_params(
            "eight", 10, (1, 2), (1, 2), (1, 2)
        )


def test_validate_rejects_zero_sleep_max():
    with pytest.raises(ValueError):
        validate_simulation_params(2, 10, (1, 2), (0, 0), (1, 2))


def test_run_simulation_short_deterministic():
    sleeps: list[float] = []

    def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)

    sim = CallCenterSimulation(sleep_fn=fake_sleep)
    sim.set(
        number_of_freshers=2,
        run_time=1,
        min_max_calls_per_wave=(2, 2),
        min_max_sleep_interval=(1, 1),
        min_max_call_duration=(0, 0),
        seed=123,
    )
    # Tiny run_time so the wave loop exits quickly even with fake sleep.
    assert sim.config is not None
    sim.config.run_time = 0.01

    assert sim.run_simulation() is True
    snap = sim.status_snapshot()
    assert snap["status"] == "finished"
    assert snap["stats"]["freshers"]
    # At least one sleep from call handling or wave wait steps occurred.
    assert sleeps


def test_stop_background_simulation():
    sim = CallCenterSimulation(sleep_fn=lambda _s: None)
    sim.set(2, 30, (1, 1), (1, 1), (0, 0), seed=1)
    assert sim.config is not None
    sim.config.run_time = 5
    sim.run_simulation(background=True)
    sim.stop(wait=True, timeout=5)
    status = sim.status_snapshot()["status"]
    assert status in {"stopped", "finished"}
