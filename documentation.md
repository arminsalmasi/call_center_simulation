# Call Center Simulation
This script simulates a call center using Python threads and locks. The design is as follows:

- The call center has 3 types of employees: freshers, technical leads, and product managers.
- Each employee has a name, a minimum and maximum call duration, and a flag indicating whether they have been called before.
- The call center has a list of freshers, a technical lead, and a product manager.
- The call center has a call statistics object to keep track of call center statistics.
- The call center has a lock to ensure thread safety when modifying shared data.
- The call center has a method to find an available fresher.
- The call center has a method to print a summary of the call center statistics.
- Each employee is a thread.
- Each employee has a lock to ensure thread safety when modifying shared data.
- Each employee has a method to set their attributes.
- Each employee has a method to get their attributes.
- Each employee has a method to simulate handling a call (run the thread).
## Code Overview
### Import Statements
```   import random
    import time
    import sys
    from threading import Thread, Lock
```

### Class `Employee`
This is a base class representing an employee in the call center.

Attributes
- `lock`: A thread lock instance to ensure thread safety when modifying shared data.
Methods
- `__init__`: Initializes the thread.
- `_set_call_duration`: Sets call duration based on a minimum and maximum limit.
- `set`: Sets the employee attributes.
- `get`: Gets the attributes of the employee.
- `run`: Simulates the employee handling the call.
### Classes Fresher, TechnicalLead, ProductManager
These are subclasses of the `Employee` class, representing a fresher, technical lead, and product manager employees in the call center, respectively.

### Function `find_free_fresher_index`
This function finds an available fresher employee in the call center. It returns the index of the first available fresher, or -1 if no freshers are available.

### Class `CallStatistics`
This class is for gathering call center statistics.

Attributes
- `fresher_counter`: List of counts of calls handled by each fresher.
- `fresher_call_duration`: List of total call duration handled by each fresher.
- `technical_lead_counter`: Count of calls handled by the technical lead.
- `technical_lead_call_duration`: Total call duration handled by the technical lead.
- `product_manager_counter`: Count of calls handled by the product manager.
- `product_manager_call_duration`: Total call duration handled by the product manager.
Methods
- `add_fresher_call`: Adds statistics for a fresher who handled a call.
- `add_technical_lead_call`: Adds statistics for a technical lead who handled a call.
- `add_product_manager_call`: Adds statistics for a product manager who handled a call.
- `print_summary`: Prints a summary of the call center statistics.
### Class `CallCenterSimulation`
This class represents the call center simulation.

Attributes
- `call_statistics`: Instance to keep track of the call statistics.
- `lock`: A thread lock instance to ensure thread safety when modifying shared data.
Methods
- `set`: Sets the parameters of the simulation.
- `assign_project_manager`: Assigns a call to the product manager.
- `assign_technical_lead`: Assigns a call to the technical lead.
- `assign_freshers`: Assigns a call to a fresher.
 -`termination_message`: Prints a termination message when all lines are busy.
- `run_simulation`: Runs the call center simulation.

### Main Function
The main function sets up and runs the call center simulation. The parameters for the simulation are set using argument parse and read from the terminal.

Example:
```
python script_name.py 8 60 1 5 2 5 10 20
```

The other option is to read the methods and classes in a seperate python file and set the parammeters manually. 

Example (see test.py):
```
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
```

### How to Run
Run this Python script directly to start the call center simulation. During the simulation, the script will print out log messages indicating which employees are handling which calls, how long each call lasts, and summary statistics at the end of the simulation.

### Internal dependencies

![The graph shows internal depenedencies during running the code with the following parameters:
``` python script_name.py 8 60 1 5 2 5 10 20 ```](pycallgraph.png)


