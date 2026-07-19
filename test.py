from call_center import CallCenterSimulation


def main():
    sim = CallCenterSimulation()
    sim.set(
        number_of_freshers=3,
        run_time=5,
        min_max_calls_per_wave=(1, 3),
        min_max_sleep_interval=(1, 2),
        min_max_call_duration=(1, 2),
        seed=42,
    )
    sim.run_simulation()


if __name__ == "__main__":
    main()
