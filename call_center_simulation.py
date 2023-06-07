"""Call center simulation using threads and locks."""
"""
    Design:
        - The call center has 3 types of employees: freshers, technical leads, and project managers.
        - Each employee has a name, a minimum and maximum call duration, and a flag indicating whether they have been called before.
        - The call center has a list of freshers, a technical lead, and a project manager.
        - The call center has a call statistics object to keep track of call center statistics.
        - The call center has a lock to ensure thread safety when modifying shared data.
        - The call center has a method to find an available fresher.
        - The call center has a method to print a summary of the call center statistics.
        - Each employee is a thread.
        - Each employee has a lock to ensure thread safety when modifying shared data.
        - Each employee has a method to set their attributes.
        - Each employee has a method to get their attributes.
        - Each employee has a method to simulate handling a call (run the tread).
 """
# Imports
import random
import time
import sys
from threading import Thread, Lock
import argparse

class Employee(Thread):
    """Base class representing an employee in the call center.

    Attributes:
        lock (Lock): A thread lock instance to ensure thread safety when modifying shared data.
    """
    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def _set_call_duration(self):
        """Private method to set call duration based on a minimum and maximum limit.

        Returns:
            int: Random number between the min and max call duration range.
        """
        return random.randint(self.min_max_call_duration[0], self.min_max_call_duration[1])

    def set(self, name, min_max_call_duration):
        """Sets the employee attributes.

        Args:
            name (str): The name of the employee.
            min_max_call_duration (tuple): The min and max duration of the calls this employee can handle.
        """
        self.name = name
        self.min_max_call_duration = min_max_call_duration
        self.call_duration = self._set_call_duration()
        self.was_called_before = False

    def get(self):
        """Get the attributes of the employee.

        Returns:
            tuple: The name of the employee, call duration, was_called_before flag, and min_max_call_duration.
        """
        return (self.name, self.call_duration, self.was_called_before, self.min_max_call_duration)

    def run(self):
        """Run method that will be invoked when the thread is started. Simulates the employee handling the call."""
        print(f"{self.name} took the call. The call will take {self.call_duration} seconds.")
        time.sleep(self.call_duration)
        print(f"{self.name} has hung up the call.")
        self.lock.acquire()
        try:
            self.was_called_before = True
        finally:
            self.lock.release()

class Fresher(Employee):
    """Subclass of Employee representing a fresher employee in the call center."""
    def __init__(self):
        super().__init__()

class TechnicalLead(Employee):
    """Subclass of Employee representing a technical lead employee in the call center."""
    def __init__(self):
        super().__init__()

class ProjectManager(Employee):
    """Subclass of Employee representing a project manager employee in the call center."""
    def __init__(self):
        super().__init__()

def find_free_fresher_index(bool_list):
    """Find an available fresher employee in the call center.

    Args:
        bool_list (list): List of booleans indicating which freshers are available.

    Returns:
        int: Index of the first available fresher, -1 if no freshers are available.
    """
    for index, value in enumerate(bool_list):
        if value:
            return index
    return -1

class CallStatistics:
    """Class for gathering call center statistics.

    Attributes:
        fresher_counter (list): List of counts of calls handled by each fresher.
        fresher_call_duration (list): List of total call duration handled by each fresher.
        technical_lead_counter (int): Count of calls handled by the technical lead.
        technical_lead_call_duration (int): Total call duration handled by the technical lead.
        project_manager_counter (int): Count of calls handled by the project manager.
        project_manager_call_duration (int): Total call duration handled by the project manager.
    """
    def __init__(self):
        self.fresher_counter = []
        self.fresher_call_duration = []
        self.technical_lead_counter = 0
        self.technical_lead_call_duration = 0
        self.project_manager_counter = 0
        self.project_manager_call_duration = 0

    def add_fresher_call(self, index, call_duration):
        """Add statistics for a fresher who handled a call.

        Args:
            index (int): Index of the fresher in the fresher list.
            call_duration (int): Duration of the call handled by the fresher.
        """
        while len(self.fresher_counter) <= index:
            self.fresher_counter.append(0)
            self.fresher_call_duration.append(0)
        self.fresher_counter[index] += 1
        self.fresher_call_duration[index] += call_duration

    def add_technical_lead_call(self, call_duration):
        """Add statistics for a technical lead who handled a call.

        Args:
            call_duration (int): Duration of the call handled by the technical lead.
        """
        self.technical_lead_counter += 1
        self.technical_lead_call_duration += call_duration

    def add_project_manager_call(self, call_duration):
        """Add statistics for a project manager who handled a call.

        Args:
            call_duration (int): Duration of the call handled by the project manager.
        """
        self.project_manager_counter += 1
        self.project_manager_call_duration += call_duration

    def print_summary(self):
        """Prints a summary of the call center statistics."""
        print("----------------------------------------------")
        print('Summary:')
        for i, f in enumerate(self.fresher_counter):
            print(f'fresher {i + 1}: answered {f} calls and spent {self.fresher_call_duration[i]} seconds on the phone.')
        print(f'Technical lead: answered {self.technical_lead_counter} calls and spent {self.technical_lead_call_duration} seconds on the phone.')
        print(f'Project manager: answered {self.project_manager_counter} calls and spent {self.project_manager_call_duration} seconds on the phone.')

class CallCenterSimulation:
    """Class representing the call center simulation.

    Attributes:
        call_statistics (CallStatistics): Instance to keep track of the call statistics.
        lock (Lock): A thread lock instance to ensure thread safety when modifying shared data.
    """
    def __init__(self):
        self.call_statistics = CallStatistics()
        self.lock = Lock()  # Create a lock instance

    def set(self, number_of_freshers, run_time, min_max_calls_per_wave, min_max_sleep_interval, min_max_call_duration):
        """Set the parameters of the simulation.

        Args:
            number_of_freshers (int): Number of fresher employees.
            run_time (int): Total run time of the simulation.
            min_max_calls_per_wave (tuple): Min and max number of calls per wave.
            min_max_sleep_interval (tuple): Min and max sleep interval between call waves.
            min_max_call_duration (tuple): Min and max duration of calls.
        """
        self.number_of_freshers = number_of_freshers
        self.run_time = run_time
        self.min_max_calls_per_wave = min_max_calls_per_wave
        self.min_max_sleep_interval = min_max_sleep_interval
        self.min_max_call_duration = min_max_call_duration

    def assign_project_manager(self, technical_lead, project_manager):
        """Assign a call to the project manager.

        Args:
            technical_lead (TechnicalLead): The technical lead instance.
            project_manager (projectManager): The project manager instance.

        Returns:
            ProjectManager: The project manager instance.
        """
        print(f"{technical_lead.name} is busy, call is being forwarded to the {project_manager.name}.")
        print(f"{project_manager.name} is free and will answer the call.")
        self.lock.acquire()
        try:
            if project_manager.was_called_before:
                project_manager = ProjectManager()
            project_manager.set("project manager", self.min_max_call_duration)
            project_manager.start()
            self.call_statistics.add_project_manager_call(project_manager.call_duration)
        finally:
            self.lock.release()

        return project_manager

    def assign_technical_lead(self, technical_lead):
        """Assign a call to the technical lead.

        Args:
            technical_lead (TechnicalLead): The technical lead instance.

        Returns:
            TechnicalLead: The technical lead instance.
        """
        print(f"All freshers are busy, call is being forwarded to the {technical_lead.name}.")
        print(f"{technical_lead.name} is free and will answer the call.")
        self.lock.acquire()
        try:
            if technical_lead.was_called_before:
                technical_lead = TechnicalLead()
                technical_lead.set("technical lead", self.min_max_call_duration)
            technical_lead.start()
            self.call_statistics.add_technical_lead_call(technical_lead.call_duration)
        finally:
            self.lock.release()

        return technical_lead

    def assign_freshers(self, freshers, fresher_counter, idx):
        """Assign a call to a fresher.

        Args:
            freshers (list): List of fresher instances.
            fresher_counter (list): List of fresher call counters.
            idx (int): Index of the fresher to assign the call.
        """
        print(f"{freshers[idx].name} is {'busy' if freshers[idx].is_alive() else 'free'}.")
        self.lock.acquire()
        try:
            if freshers[idx].was_called_before:
                freshers[idx] = Fresher()
                freshers[idx].set(f"fresher {idx + 1}", self.min_max_call_duration)
            freshers[idx].start()
            fresher_counter[idx] += 1
            self.call_statistics.add_fresher_call(idx, freshers[idx].call_duration)
        finally:
            self.lock.release()

    def termination_message(self, project_manager):
        """Print a termination message when all lines are busy.

        Args:
            project_manager (projectManager): The project manager instance.
        """
        print(f"{project_manager.name} is busy.")
        print("All lines are busy. Please try again later.")
        print("----------------------------------------------")

    def run_simulation(self):
        """Runs the call center simulation."""
        # Initialize freshers, technical lead, and project manager
        freshers = []
        for i in range(self.number_of_freshers):
            fresher = Fresher()
            fresher.set(f"fresher {i + 1}", self.min_max_call_duration)
            freshers.append(fresher)
        technical_lead = TechnicalLead()
        technical_lead.set("technical lead", self.min_max_call_duration)
        project_manager = ProjectManager()
        project_manager.set("project manager", self.min_max_call_duration)

        # Run the simulation
        end_time = time.time() + self.run_time
        fresher_counter = [0] * self.number_of_freshers

        # Exception handling
        loop_number = 1
        try:
            while True:
                if time.time() >= end_time:
                    break
                # Process call waves
                number_of_calls = random.randint(self.min_max_calls_per_wave[0], self.min_max_calls_per_wave[1])
                print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
                print(f"Incoming calls: {number_of_calls}, loop: {loop_number}")
                print("----------------------------------------------")
                # Process individual calls
                for call in range(number_of_calls):
                    # Find indices of free freshers, -1 if none
                    idx = find_free_fresher_index([not fresher.is_alive() for fresher in freshers])
                    print(f"Call {call + 1} is on top of the queue.")
                    print("----------------------")

                    if idx > -1:
                        # If any of the freshers ia available then assign the call to that fresher
                        # If the employee was in a call before then the thread should be re-initialized 
                        self.assign_freshers(freshers, fresher_counter, idx)
                    else:
                        # If all freshers are busy then assign the call to the technical lead
                        if not technical_lead.is_alive():
                            # If the employee was in a call before then the thread should be re-initialized 
                            technical_lead = self.assign_technical_lead(technical_lead)
                        else:
                            # If the technical lead is busy then assign the call to the project manager
                            if not project_manager.is_alive():
                                # If the employee was in a call before then the thread should be re-initialized 
                                project_manager = self.assign_project_manager(technical_lead, project_manager)
                            else:
                                self.termination_message(project_manager)

                # Wait for the next call wave
                time_interval = random.randint(self.min_max_sleep_interval[0], self.min_max_sleep_interval[1])
                print(f"Waiting for {time_interval} seconds before initiating the next wave of calls.")
                print("----------------------------------------------")

                time.sleep(time_interval)
                loop_number += 1

            
            # Safty time margin to finish up the remaining calls
            time.sleep(self.min_max_call_duration[1]+10)
            
            # Finish up the remaining calls by joining all threads
            while True:
                for fresher in freshers:
                    if not(fresher.is_alive()) and fresher.was_called_before:
                        fresher.join(timeout=2)
                if not(technical_lead.is_alive()) and technical_lead.was_called_before:
                        technical_lead.join(timeout=2)
                if not(project_manager.is_alive()) and project_manager.was_called_before:
                        project_manager.join(timeout=2)
                
                if not(technical_lead.is_alive()) and not(project_manager.is_alive()) and all([not(fresher.is_alive()) for fresher in freshers]):
                    break

            # Print call statistics
            self.call_statistics.print_summary()

        except Exception as e:
            print(f"An error occurred during the call center simulation: {str(e)}")
            sys.exit(1)
        return True

def main():
    """The main function to run the simulation."""
    try:
        # Create an argument parser
        parser = argparse.ArgumentParser(description="Call Center Simulation")

        # Add arguments to the parser
        parser.add_argument("number_of_freshers", type=int, help="Number of freshers in the call center")
        parser.add_argument("run_time", type=int, help="Total run time of the simulation")
        parser.add_argument("min_calls_per_wave", type=int, help="Minimum number of calls per wave")
        parser.add_argument("max_calls_per_wave", type=int, help="Maximum number of calls per wave")
        parser.add_argument("min_sleep_interval", type=int, help="Minimum sleep interval between waves")
        parser.add_argument("max_sleep_interval", type=int, help="Maximum sleep interval between waves")
        parser.add_argument("min_call_duration", type=int, help="Minimum call duration")
        parser.add_argument("max_call_duration", type=int, help="Maximum call duration")

        # Parse the arguments
        args = parser.parse_args()

        # Set the parameters of the call center simulation
        number_of_freshers = args.number_of_freshers
        run_time = args.run_time
        min_calls_per_wave = args.min_calls_per_wave
        max_calls_per_wave = args.max_calls_per_wave
        min_sleep_interval = args.min_sleep_interval
        max_sleep_interval = args.max_sleep_interval
        min_call_duration = args.min_call_duration
        max_call_duration = args.max_call_duration

        # Create and set up the call center simulation
        call_center_simulation = CallCenterSimulation()
        min_max_calls_per_wave = (min_calls_per_wave, max_calls_per_wave)
        min_max_sleep_interval = (min_sleep_interval, max_sleep_interval)
        min_max_call_duration = (min_call_duration, max_call_duration)
        call_center_simulation.set(number_of_freshers, run_time, min_max_calls_per_wave, min_max_sleep_interval, min_max_call_duration)

        # Run the simulation
        call_center_simulation.run_simulation()

    except KeyboardInterrupt:
        print("\nSimulation interrupted.")

if __name__ == "__main__":
    main()
