from call_center_simulation import CallCenterSimulation

def main():
    """The main function to run the simulation."""
    try:
        # Set the parameters of the call center simulation
        number_of_freshers = 3
        run_time = 20
        min_max_calls_per_wave = (1, 3)
        min_max_sleep_interval = (5, 6)
        min_max_call_duration = (5, 10)

        # Create and set up the call center simulation
        call_center_simulation = CallCenterSimulation()
        call_center_simulation.set(number_of_freshers, run_time, min_max_calls_per_wave, min_max_sleep_interval, min_max_call_duration)
        
        # Run the simulation
        call_center_simulation.run_simulation()

    except KeyboardInterrupt:
        print("\nSimulation interrupted.")
    else:
        print("\nSimulation completed.")
        return True

if __name__ == "__main__":
    if main():
        print("\n ---- Test completed. ----\n")