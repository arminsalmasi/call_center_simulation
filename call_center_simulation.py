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
import secrets
import time
import sys
import logging
from threading import Thread, Lock
import argparse

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

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
        return secrets.SystemRandom().randint(self.min_max_call_duration[0], self.min_max_call_duration[1])

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

def find_free_fresher_index(freshers):
    """Find an available fresher employee in the call center.

    Args:
        freshers (list): List of fresher employees.

    Returns:
        int: Index of the first available fresher, -1 if no freshers are available.
    """
    for index, fresher in enumerate(freshers):
        if not fresher.is_alive():
            return index
    return -1

class CallStatistics:
    """Class for gathering call center statistics.

    Attributes:
        fresher_statistics (dict): Dict of statistics mapped by fresher index. Contains counter and call duration.
        technical_lead_counter (int): Count of calls handled by the technical lead.
        technical_lead_call_duration (int): Total call duration handled by the technical lead.
        project_manager_counter (int): Count of calls handled by the project manager.
        project_manager_call_duration (int): Total call duration handled by the project manager.
    """
    def __init__(self):
        self.fresher_statistics = {}
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
        if index not in self.fresher_statistics:
            self.fresher_statistics[index] = {'counter': 0, 'call_duration': 0}
        self.fresher_statistics[index]['counter'] += 1
        self.fresher_statistics[index]['call_duration'] += call_duration

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
        for i, stats in sorted(self.fresher_statistics.items()):
            print(f'fresher {i + 1}: answered {stats["counter"]} calls and spent {stats["call_duration"]} seconds on the phone.')
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
        # Security Enhancement: Validate inputs to prevent Resource Exhaustion (DoS risk)
        if not (0 <= number_of_freshers <= 1000):
            raise ValueError("number_of_freshers must be between 0 and 1000")
        if run_time < 0 or run_time > 86400:  # Max 1 day simulation
            raise ValueError("run_time must be between 0 and 86400")
        if not (0 <= min_max_calls_per_wave[0] <= min_max_calls_per_wave[1] and min_max_calls_per_wave[1] <= 10000):
            raise ValueError("Invalid min_max_calls_per_wave range")
        if not (0 <= min_max_sleep_interval[0] <= min_max_sleep_interval[1]):
            raise ValueError("Invalid min_max_sleep_interval range")
        if not (0 <= min_max_call_duration[0] <= min_max_call_duration[1]):
            raise ValueError("Invalid min_max_call_duration range")

        self.number_of_freshers = number_of_freshers
        self.run_time = run_time
        self.min_max_calls_per_wave = min_max_calls_per_wave
        self.min_max_sleep_interval = min_max_sleep_interval
        self.min_max_call_duration = min_max_call_duration
        self.call_statistics = CallStatistics(number_of_freshers)

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

    def assign_freshers(self, freshers, idx):
        """Assign a call to a fresher.

        Args:
            freshers (list): List of fresher instances.
            idx (int): Index of the fresher to assign the call.
        """
        print(f"{freshers[idx].name} is {'busy' if freshers[idx].is_alive() else 'free'}.")
        self.lock.acquire()
        try:
            if freshers[idx].was_called_before:
                freshers[idx] = Fresher()
                freshers[idx].set(f"fresher {idx + 1}", self.min_max_call_duration)
            freshers[idx].start()
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

    def _initialize_employees(self):
        """Initializes the freshers, technical lead, and project manager.

        Returns:
            tuple: A tuple containing the list of freshers, the technical lead, and the project manager.
        """
        freshers = []
        for i in range(self.number_of_freshers):
            fresher = Fresher()
            fresher.set(f"fresher {i + 1}", self.min_max_call_duration)
            freshers.append(fresher)
        technical_lead = TechnicalLead()
        technical_lead.set("technical lead", self.min_max_call_duration)
        project_manager = ProjectManager()
        project_manager.set("project manager", self.min_max_call_duration)
        return freshers, technical_lead, project_manager

    def _process_call_wave(self, loop_number, freshers, fresher_counter, technical_lead, project_manager):
        """Processes a single wave of calls.

        Args:
            loop_number (int): The current loop iteration number.
            freshers (list): List of fresher instances.
            fresher_counter (list): List of counts for calls handled by each fresher.
            technical_lead (TechnicalLead): The technical lead instance.
            project_manager (ProjectManager): The project manager instance.

        Returns:
            tuple: The updated technical lead and project manager instances.
        """
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
        return technical_lead, project_manager

    def _finish_remaining_calls(self, freshers, technical_lead, project_manager):
        """Waits for all remaining calls to finish by joining threads.

        Args:
            freshers (list): List of fresher instances.
            technical_lead (TechnicalLead): The technical lead instance.
            project_manager (ProjectManager): The project manager instance.
        """
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

    def run_simulation(self):
        """Runs the call center simulation."""
        freshers, technical_lead, project_manager = self._initialize_employees()

        # Run the simulation
        end_time = time.time() + self.run_time

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
                    idx = find_free_fresher_index(freshers)
                    print(f"Call {call + 1} is on top of the queue.")
                    print("----------------------")

                    if idx > -1:
                        # If any of the freshers ia available then assign the call to that fresher
                        # If the employee was in a call before then the thread should be re-initialized 
                        self.assign_freshers(freshers, idx)
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
                time_interval = secrets.SystemRandom().randint(self.min_max_sleep_interval[0], self.min_max_sleep_interval[1])
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
                
                if not(technical_lead.is_alive()) and not(project_manager.is_alive()) and all(not(fresher.is_alive()) for fresher in freshers):
                    break

            # Print call statistics
            self.call_statistics.print_summary()

        except Exception as e:
            logging.error("Exception occurred during the call center simulation", exc_info=True)
            print("An unexpected error occurred during the call center simulation. Please check the logs.")
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

        # Validate arguments
        if args.number_of_freshers <= 0:
            parser.error("number_of_freshers must be greater than 0")
        if args.run_time <= 0:
            parser.error("run_time must be greater than 0")
        if args.min_calls_per_wave < 0:
            parser.error("min_calls_per_wave must be non-negative")
        if args.min_sleep_interval < 0:
            parser.error("min_sleep_interval must be non-negative")
        if args.min_call_duration <= 0:
            parser.error("min_call_duration must be strictly positive")

        if args.min_calls_per_wave > args.max_calls_per_wave:
            parser.error("min_calls_per_wave cannot be greater than max_calls_per_wave")
        if args.min_sleep_interval > args.max_sleep_interval:
            parser.error("min_sleep_interval cannot be greater than max_sleep_interval")
        if args.min_call_duration > args.max_call_duration:
            parser.error("min_call_duration cannot be greater than max_call_duration")

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
