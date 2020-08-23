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
        self.all_passed = None

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

    def get_all_passed(self):
        return self.all_passed

    def set_all_passed(self, passed):
        self.all_passed = passed
        print(f"\n--------------------------")
        print(f" ALL MINIMAL TESTS PASSED ")
        print(f"--------------------------\n")

    def print_results(self):
        results = self.get_results()
        if results == None:
            results = self.run()
            for result in results:
                if result.status == "fail":
                    self.print_fail(result)
                elif result.status == "pass":
                    self.print_pass(result)
        else:
            for result in results:
                if result.status == "fail":
                    self.print_fail(result)
                elif result.status == "pass":
                    self.print_pass(result)

    def print_fail(self, result):
        test_name = result.get_name()
        test_data = result.get_data()
        algorithms = result.get_algorithms()
        results = result.get_test_result()
        print("\n---TEST FAIL---")
        print(f"TEST NAME : {test_name}")
        print(f"TEST DATA : {test_data}")
        print("------")
        for i, algorithm in enumerate(algorithms):
            result = results[i]
            print(f"ALGORITHM NAME: {algorithm.name}")
            print(f"RESULT : {result}")
        print("------\n")

    def print_pass(self, result):
        test_name = result.get_name()
        test_data = result.get_data()
        algorithms = result.get_algorithms()
        results = result.get_test_result()
        print("\n---TEST PASSED---")
        print(f"TEST NAME : {test_name}")
        print(f"TEST DATA : {test_data}")
        for i, algorithm in enumerate(algorithms):
            result = results[i]
            print(f"ALGORITHM NAME: {algorithm.name}")
            print(f"RESULT : {result}")
        print("------\n")


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

    def print_fail(self, result):
        test_name = result.get_name()
        test_data = result.get_data()
        algorithms = result.get_algorithms()
        results = result.get_test_result()
        print("\n---TEST FAIL---")
        print(f"TEST NAME : {test_name}")
        print(f"TEST DATA : {test_data}")
        print("------")
        for i, algorithm in enumerate(algorithms):
            result = results[i]
            print(f"ALGORITHM NAME: {algorithm.name}")
            print(f"RESULT : {result}")
        print("------\n")

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

            if result.get_status() == "fail":
                self.print_fail(result)
                break
