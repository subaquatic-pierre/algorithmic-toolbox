from algorithm_test import AlgorithmTest
from test_result import TestResult


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

        for data_point_raw in data_set:
            data_point = data_point_raw.copy()
            test_name = data_point.get("name")
            del data_point["name"]
            test_results = []
            for algorithm in algorithms:
                algorithm_result = algorithm.use(**data_point)
                test_results.append(algorithm_result)

            test_result = TestResult(test_name, algorithms, test_results, data_point)
            data_set_test_results.append(test_result)

        self.set_results(data_set_test_results)
        results = self.get_results()

        if all(result.get_status() == "pass" for result in data_set_test_results):
            self.set_all_passed(True)
        else:
            self.print_results()

        return data_set_test_results
