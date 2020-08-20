import random
from algorithm import Algorithm
from algorithm_test import AlgorithmTestMinimal, AlgorithmTestStressBase
from minimal_test_data import test_data, data1, data2, data3, data4
from implementations import (
    fast_algorithm,
    naive_algorithm,
    working_algorithm,
)


class AlgorithmTestStress(AlgorithmTestStressBase):
    """ Stress test to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        data_size (integer) : maximum size of data set to use for test
        max_value (integer) : maximum value to be used in a data point within the data set
     """

    random.seed(1)

    def build_data(self, **kwargs):
        data = {"awesome": True}

        return data


# instantiate algorithms
fast_algorithm = Algorithm("fast_algorithm", fast_algorithm)
pop_algorithm = Algorithm("naive_algorithm", naive_algorithm)
foundry_algorithm = Algorithm("working_algorithm", working_algorithm)

# build test data
algorithms = [pop_algorithm, foundry_algorithm, fast_algorithm]
data = test_data


if __name__ == "__main__":
    # run minimal tests
    minimal_test = AlgorithmTestMinimal(algorithms, data)
    minimal_test.run()
    minimal_test.print_results()

    if minimal_test.all_passed == True:
        # run stress tests
        stress_test = AlgorithmTestStress(algorithms, data_size=9, max_value=200)
        stress_test.run(1)

