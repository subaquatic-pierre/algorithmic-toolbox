from abc import abstractmethod, ABC
from test_result import TestResult
import random
import time

class AlgorithmTest(ABC):
    """ 
    Base test class used for testing algorithms
     """

    def __init__(self, algorithms, test_data=None):
        self.algorithms = algorithms
        self.test_results = None
        self.data = test_data

    @abstractmethod
    def run(self):
        """ 
        Runs all the tests passed in at creation
         """
        pass

    def set_results(self, results):
        self.test_results = results

    def get_results(self):
        return self.test_results

    def set_data(self, data):
        self.data = data
    
    def print_data(self):
        data = self.data
        if data == None:
            print("No test data is set yet")
        else:
            print(data)

    def print_results(self):
        results = self.test_results
        if results == None:
            print("No tests have been run yet")
        else:
            for result in results:
                result.check_results()


class AlgorithmTestMinimal(AlgorithmTest):
    """ Minimal tests to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        test_data (list) : list of data points to be used for each test case
     """
    def __init__(self, algorithms, test_data):
        super().__init__(algorithms, test_data)

    def run(self):
        """ 
        Runs all tests against each data point in test data set
         """
        algorithms = self.algorithms
        data_set = self.data
        data_set_test_results = []

        for data_point in data_set:
            test_name = data_point.get('name')
            del data_point['name']
            test_results = []

            for algorithm in algorithms:
                algorithm_result = algorithm.use(**data_point)
                test_results.append(algorithm_result)
            
            test_result = TestResult(test_name, algorithms, test_results, data_point)        
            data_set_test_results.append(test_result)

        self.set_results(data_set_test_results)


class AlgorithmTestStress(AlgorithmTest):
    """ Stress test to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        data_size (integer) : maximum size of data set to use for test
        max_value (integer) : maximum value to be used in a data point within the data set
     """
    random.seed(1)

    def __init__(self, algorithms, capacity, data_size, max_value):
        super().__init__(algorithms)
        self.data_size = data_size
        self.max_value = max_value
        self.capacity = capacity
   
    def build_data(self, data_size, max_value, max_capacity):
        weights = []
        values = []
        capacity = random.randint(self.capacity, max_capacity)

        for i in range(data_size):
            ran1 = random.randint(11, max_value)
            ran2 = random.randint(11, max_value)
            
            weight = ran1 - (ran1 % 10)
            value = ran2 - (ran2 % 10)

            weights.append(weight)
            values.append(value)

        data = (weights, values)
        self.set_data(data)
        return weights, values, capacity

    def run(self, duration=3, max_capacity=500):
        """ 
        Runs all the tests passed in at creation
         """
        M = self.max_value
        n = self.data_size
        algorithms = self.algorithms

        start_time = time.time()
        end_time = start_time + duration
        iterations = 0
        print(f'Running stress test iterations for {duration} seconds ...')

        while True:
            # ensure timed
            now = time.time()
            iterations += 1
            if now >= end_time:
                print(f'\n------ ALL ITERATIONS PASSED ------')
                print(f'------ ELAPSED TIME - {round(now - start_time, 2)} SECONDS ------')
                print(f'------ ITERATIONS - {iterations} ------')
                break
            
            # build test data
            weights, values, capacity = self.build_data(n, M, max_capacity)
            test_data = {
                'capacity': capacity,
                'weights': weights,
                'values': values
            }
            test_name = f'Iteration_{iterations}'

            # get test results
            test_results = []
            for algorithm in algorithms:
                algorithm_result = round(algorithm.use(**test_data),2)
                test_results.append(algorithm_result)

            result = TestResult(test_name, algorithms, test_results, test_data)
            result.check_results(show_print=False)
            
            if result.failure == True:
                result.print_fail()
                break