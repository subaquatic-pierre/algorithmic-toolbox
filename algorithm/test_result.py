class TestResult:
    def __init__(self, test_name, algorithms, test_results, test_data):
        self.test_name = test_name
        self.algorithms = algorithms
        self.results = test_results
        self.test_data = test_data
        self.failure = False

    def get_name(self):
        return self.test_name

    def get_data(self):
        return self.test_data

    def get_stress_test_result(self):
        return self.results[0]

    def set_failure(self, status):
        self.failure = status

    def check_results(self, show_print=True):
        results = self.results
        all_equal = all(elem == results[0] for elem in results)

        if not all_equal:
            self.set_failure(True)
            if show_print:
                self.print_fail()
        else:
            self.set_failure(False)
            return "pass"
            # if show_print:
            # self.print_pass()

    def print_fail(self):
        results = self.results
        algorithms = self.algorithms

        print("\n---TEST FAIL---")
        print(f"TEST NAME : {self.get_name()}")
        print(f"TEST DATA : {self.get_data()}")
        print("------")
        for i, algorithm in enumerate(algorithms):
            result = results[i]
            print(f"ALGORITHM NAME: {algorithm.name}")
            print(f"RESULT : {result}")
        print("------\n")

    def print_pass(self):
        results = self.results
        algorithms = self.algorithms

        print("\n---TEST PASSED---")
        print(f"TEST NAME : {self.get_name()}")
        print(f"TEST DATA : {self.get_data()}")
        for i, algorithm in enumerate(algorithms):
            result = results[i]
            print(f"ALGORITHM NAME: {algorithm.name}")
            print(f"RESULT : {result}")
        print("------\n")

