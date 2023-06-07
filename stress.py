import sys
from call_center_simulation import CallCenterSimulation

# The code for Employee, Fresher, TechnicalLead, ProductManager, find_free_fresher_index, CallStatistics, and CallCenterSimulation remains the same as in the original code.

def stress_test_call_center():
    try:
        # Set the parameters for the stress test
        number_of_simulations = 100
        number_of_freshers = 100
        run_time = 60
        min_max_calls_per_wave = (50, 100)
        min_max_sleep_interval = (0, 1)
        min_max_call_duration = (10, 30)

        for i in range(number_of_simulations):
            print(f"Running call center simulation #{i + 1}")

            # Run the call center simulation
            call_center = CallCenterSimulation()
            # Set the parameters of the call center simulation
            call_center.set(
                number_of_freshers,
                run_time,
                min_max_calls_per_wave,
                min_max_sleep_interval,
                min_max_call_duration
            )
            # Run the call center simulation
            call_center.run_simulation()

            print(f"Call center simulation #{i + 1} completed\n")

    except Exception as e:
        print(f"An error occurred during the execution of the call center simulation: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    stress_test_call_center()
