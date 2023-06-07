# Documentation for Call Center Simulation Stress Test
## Introduction
This stress test is to measure the efficiency of the call center simulation system. It simulates the operation of a call center under varying workloads and verifies the simulation's ability to perform and handle stress.

## Functionality
The stress test function, stress_test_call_center(), runs multiple instances of a call center simulation and examines the behavior under different workloads. Each simulation represents a separate run of the call center, handling a varying number of calls.

## Parameters
The stress test uses the following parameters:

- `number_of_simulations`: The number of times the call center simulation is run. Default is 10.
- `number_of_freshers`: The number of fresher employees available to take calls in the call center. Default is 8.
- `run_time`: The total time the simulation runs. Default is 60 seconds.
- `min_max_calls_per_wave`: The minimum and maximum number of calls arriving in each wave. Default is between 1 and 10 calls.
- `min_max_sleep_interval`: The minimum and maximum interval between two consecutive waves of calls. Default is between 5 and 10 seconds.
- `min_max_call_duration`: The minimum and maximum duration of each call. Default is between 40 and 50 seconds.

## Execution
The stress test performs the following steps:

## Initializes the parameters for the stress test.
Runs the call center simulation for the specified number of times (number_of_simulations).

For each simulation run:
- The call center simulation is initialized and configured with the defined parameters.
- The simulation is then run.
- After the simulation completes, it outputs a message indicating completion.

If an error occurs during the execution of the simulation, the stress test will output an error message and terminate the program.

## Conclusion
This stress test aids in ensuring the resilience and efficiency of the call center simulation under different conditions. It helps identify potential issues that may occur during high workloads or extended run times, facilitating the improvement of the system's robustness.

## At it's extreme the test function creates a scenario in which there are, e.g., 100 freshers, and each wave of calls can include up to 100 calls with almost no time between the waves. This will push the simulation's ability to handle a high load. It is important to carefully monitor the system's resources (like CPU and memory usage) during the stress test to ensure it's not being overloaded.


