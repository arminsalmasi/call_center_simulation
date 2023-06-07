import unittest
from call_center_simulation import Employee, Fresher, CallStatistics, CallCenterSimulation, TechnicalLead, ProjectManager, find_free_fresher_index

class EmployeeTest(unittest.TestCase):

    """
    Test the _set_call_duration method of the Employee class.

    It ensures that the call duration is set within the specified range.

    Assertions:
        - The call duration is within the specified range.
    """
    def test__set_call_duration(self):
        employee = Employee()
        employee.min_max_call_duration = (10, 20)
        call_duration = employee._set_call_duration()
        self.assertTrue(10 <= call_duration <= 20)
        print('Employee._set_call_duration,... passed\n')
        pass


class FresherTest(unittest.TestCase):    
    def test_set(self):
        """
        Test the set method of the Fresher class.

        It ensures that the name, call duration, and was_called_before attributes are set correctly.

        Assertions:
            - The name attribute is set correctly.
            - The call duration is within the specified range.
            - The was_called_before attribute is set to False.
        """
        fresher = Fresher()
        fresher.set("Fresher 1", (10, 20))
        self.assertEqual(fresher.name, "Fresher 1")
        self.assertTrue(10 <= fresher.call_duration <= 20)
        self.assertFalse(fresher.was_called_before)
        print('Fresher.set,... passed\n')
        pass


    def test_get(self):
 

        """
        Test the get method of the Fresher class.

        It ensures that the method returns the expected values for the name, call duration, was_called_before, and min_max_call_duration attributes.

        Assertions:
            - The returned tuple contains the expected values.
        """

        fresher = Fresher()
        fresher.set("Fresher 1", (10, 20))
        result = fresher.get()
        expected_result = ("Fresher 1", fresher.call_duration, fresher.was_called_before, (10, 20))
        self.assertEqual(result, expected_result)
        print('Fresher.get,... passed\n')
        pass



class CallStatisticsTest(unittest.TestCase):
    def test_set(self):
        """
        Test the set method of the CallStatistics class.

        It ensures that the attributes of the CallCenterSimulation instance are set correctly.

        Assertions:
            - The attributes of the CallCenterSimulation instance are set correctly.
        """
        call_center_simulation = CallCenterSimulation()
        call_center_simulation.set(8,60,(1,5),(2,5),(10,20))   
        self.assertEqual(call_center_simulation.number_of_freshers, 8)
        self.assertEqual(call_center_simulation.run_time, 60)
        self.assertEqual(call_center_simulation.min_max_calls_per_wave, (1,5))
        self.assertEqual(call_center_simulation.min_max_sleep_interval, (2,5))
        self.assertEqual(call_center_simulation.min_max_call_duration, (10,20))
        print('CallStatistics.set,... passed\n')
        pass

 
    def test_add_fresher_call(self):

        """
        Test the add_fresher_call method of the CallStatistics class.

        It ensures that the fresher_counter and fresher_call_duration attributes are updated correctly.

        Assertions:
            - The fresher_counter and fresher_call_duration attributes are updated correctly.
        """
        call_statistics = CallStatistics()
        call_statistics.add_fresher_call(0, 30)
        self.assertEqual(call_statistics.fresher_counter[0], 1)
        self.assertEqual(call_statistics.fresher_call_duration[0], 30)
        print('CallStatistics.add_fresher_call,... passed\n')
        pass


    
    def test_add_technical_lead_call(self):

        """
        Test the add_technical_lead_call method of the CallStatistics class.

        It ensures that the technical_lead_counter and technical_lead_call_duration attributes are updated correctly.

        Assertions:
            - The technical_lead_counter and technical_lead_call_duration attributes are updated correctly.
        """
        call_statistics = CallStatistics()
        call_statistics.add_technical_lead_call(40)
        self.assertEqual(call_statistics.technical_lead_counter, 1)
        self.assertEqual(call_statistics.technical_lead_call_duration, 40)       
        print('CallStatistics.add_technical_lead_call,... passed\n')
        pass



    def test_add_project_manager_call(self):

        """
        Test the add_project_manager_call method of the CallStatistics class.

        It ensures that the project_manager_counter and project_manager_call_duration attributes are updated correctly.

        Assertions:
            - The project_manager_counter and project_manager_call_duration attributes are updated correctly.
        """
        call_statistics = CallStatistics()
        call_statistics.add_project_manager_call(50)
        self.assertEqual(call_statistics.project_manager_counter, 1)
        self.assertEqual(call_statistics.project_manager_call_duration, 50)
        print('CallStatistics.add_project_manager_call,... passed\n')
        pass


    def test_assign_freshers(self):

        """
        Test the assign_freshers method of the CallCenterSimulation class.

        It ensures that the fresher_counter, fresher_call_duration, technical_lead_counter, technical_lead_call_duration,
        and lock attributes are updated correctly.

        Assertions:
            - The fresher_counter, fresher_call_duration, technical_lead_counter, technical_lead_call_duration,
              and lock attributes are updated correctly.
        """
        call_center_simulation = CallCenterSimulation()
        call_center_simulation.set(1, 1, (1, 1), (1, 1), (1, 1))
        
        fresher = Fresher()
        fresher.set(f"fresher {1}", call_center_simulation.min_max_call_duration)
        call_center_simulation.assign_freshers([fresher],[0],0)

        technical_lead = TechnicalLead()
        technical_lead.set(f"technical_lead", call_center_simulation.min_max_call_duration)
        call_center_simulation.assign_technical_lead(technical_lead)

        project_manager = ProjectManager()
        project_manager.set(f"project_manager", call_center_simulation.min_max_call_duration)
        call_center_simulation.assign_project_manager(technical_lead,project_manager)
        
        self.assertEqual(call_center_simulation.call_statistics.fresher_counter,[1])
        self.assertEqual(call_center_simulation.call_statistics.fresher_call_duration,[1])
        self.assertEqual(call_center_simulation.call_statistics.technical_lead_counter,1)
        self.assertEqual(call_center_simulation.call_statistics.technical_lead_call_duration,1)
        self.assertTrue(call_center_simulation.lock.acquire())

        print('CallCenterSimulation.assign_freshers... passed\n')
        print('CallCenterSimulation.assign_technical_lead... passed\n')
        print('CallCenterSimulation.assign_project_manager... passed\n')
        pass


    
    def test_prtest_run_simulation(self):

        """
        Test the run_simulation method of the CallCenterSimulation class.

        It ensures that the method runs successfully without any errors.

        Assertions:
            - The method runs successfully without raising any exceptions.
        """

        call_center_simulation = CallCenterSimulation()
        call_center_simulation.set(1, 1, (1, 1), (1, 1), (1, 1))
        self.assertTrue(call_center_simulation.run_simulation())
        print('CallCenterSimulation.run_simulation... passed\n')

class OtherTest(unittest.TestCase):

    def test_find_free_fresher_index(self):

        """
        Test the find_free_fresher_index function.

        It ensures that the function returns the correct index of the first free fresher or -1 if none are free.

        Assertions:
            - The function returns the correct index of the first free fresher.
            - If no free fresher is available, it returns -1.
        """

        test_list = [False, False, True, True, True, True, True, True]
        self.assertEqual(find_free_fresher_index(test_list),2)
        test_list = [False, False, False, False, False, False, False, False]
        self.assertEqual(find_free_fresher_index(test_list),-1)
        test_list = [True, True, False, False, False, False, False, False]
        self.assertEqual(find_free_fresher_index(test_list),0)
        print('find_free_fresher_index... passed\n')
        pass


if __name__ == '__main__':
    unittest.main()




