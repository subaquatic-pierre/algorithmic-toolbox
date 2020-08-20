class TestResult:
    def __init__(self, test_name, algorithms, test_results, test_data):
        self.test_name = test_name
        self.algorithms = algorithms
        self.results = test_results
        self.test_data = test_data
        self.status = None

    def get_name(self):
        return self.test_name

    def get_data(self):
        return self.test_data

    def get_test_result(self):
        return self.results

    def get_algorithms(self):
        return self.algorithms

    def get_stress_test_result(self):
        return self.results[0]

    def set_status(self, status):
        self.status = status

    def get_status(self):
        if self.status == None:
            self.check_results()
        return self.status

    def check_results(self, show_print=True):
        results = self.results
        all_equal = all(elem == results[0] for elem in results)

        if not all_equal:
            self.set_status("fail")
        else:
            self.set_status("pass")

