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

    def set_all_passed(self, passed):
        self.all_passed = passed

    def print_results(self):
        results = self.test_results
        if results == None:
            print("No tests have been run yet")
        else:
            all_tests = []
            for result in results:
                all_tests.append(result.check_results())

            if all(elem == "pass" for elem in all_tests):
                self.set_all_passed(True)
                print(f"\n--------------------------")
                print(f" ALL MINIMAL TESTS PASSED ")
                print(f"--------------------------\n")


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
            test_name = data_point.get("name")
            del data_point["name"]
            test_results = []

            for algorithm in algorithms:
                algorithm_result = algorithm.use(**data_point)
                test_results.append(algorithm_result)

            test_result = TestResult(test_name, algorithms, test_results, data_point)
            data_set_test_results.append(test_result)

        self.set_results(data_set_test_results)


class AlgorithmTestStressBase(AlgorithmTest, ABC):
    """ Stress test to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        data_size (integer) : maximum size of data set to use for test
        max_value (integer) : maximum value to be used in a data point within the data set
     """

    random.seed(1)

    def __init__(self, algorithms, data_size, max_value):
        super().__init__(algorithms)
        self.data_size = data_size
        self.max_value = max_value

    @abstractmethod
    def build_data(self, **kwargs):
        pass

    def run(self, duration=3):
        """ 
        Runs all the tests passed in at creation
         """
        M = self.max_value
        n = self.data_size
        algorithms = self.algorithms

        start_time = time.time()
        end_time = start_time + duration
        iterations = 0
        print(f"Running stress test iterations for {duration} seconds ...")

        while True:
            # ensure timed
            now = time.time()
            iterations += 1
            if now >= end_time:
                print(f"\n------ ALL ITERATIONS PASSED ------")
                print(
                    f"------ ELAPSED TIME - {round(now - start_time, 2)} SECONDS ------"
                )
                print(f"------ ITERATIONS - {iterations} ------\n")
                break

            # build test data
            test_data = self.build_data()
            test_name = f"Iteration_{iterations}"

            # get test results
            test_results = []
            for algorithm in algorithms:
                algorithm_result = round(algorithm.use(**test_data), 2)
                test_results.append(algorithm_result)

            result = TestResult(test_name, algorithms, test_results, test_data)
            result.check_results(show_print=False)

            if result.failure == True:
                result.print_fail()
                break
