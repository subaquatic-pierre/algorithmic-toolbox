import random
from algorithm import Algorithm
from stress_test import AlgorithmTestStress
from minimal_test import AlgorithmTestMinimal
from minimal_test_data import test_data, data1
from implementations import (
    fast_algorithm,
    working_algorithm,
)

# instantiate algorithms
fast_algorithm = Algorithm("fast_algorithm", fast_algorithm)
working_algorithm = Algorithm("working_algorithm", working_algorithm)

# build test data
algorithms = [fast_algorithm, working_algorithm]
data = [data1]

minimal_test = AlgorithmTestMinimal(algorithms, data)

minimal_test.run()
minimal_test.print_results()


# if __name__ == "__main__":
#     # run minimal tests
#     minimal_test = AlgorithmTestMinimal(algorithms, data)
#     minimal_test.run()
#     minimal_test.print_results()

# if minimal_test.all_passed == True:
#     # run stress tests
#     stress_test = AlgorithmTestStress(algorithms, data_size=9, max_value=200)
#     stress_test.run(1)

