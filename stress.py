"""Lightweight stress runner using the refactored engine."""

from call_center import CallCenterSimulation


def main():
    sim = CallCenterSimulation()
    sim.set(
        number_of_freshers=20,
        run_time=10,
        min_max_calls_per_wave=(5, 15),
        min_max_sleep_interval=(1, 2),
        min_max_call_duration=(1, 3),
        seed=1,
    )
    sim.run_simulation()


if __name__ == "__main__":
    main()
