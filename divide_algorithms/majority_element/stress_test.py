from algorithm_test import AlgorithmTestStressBase
import random


class AlgorithmTestStress(AlgorithmTestStressBase):
    """ Stress test to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        data_size (integer) : maximum size of data set to use for test
        max_value (integer) : maximum value to be used in a data point within the data set
     """

    random.seed(4)

    def build_data(self, **kwargs):
        max_num = self.max_value
        max_len = self.data_size

        # build data
        data = {
            "param_1": (random.randint(0, max_num) % 10) * 10,
            "param_2": (random.randint(0, max_num) % 10) * 10,
            "list_1": [
                (random.randint(0, max_num) % 10) * 10 for element in range(0, max_len)
            ],
        }

        return data
