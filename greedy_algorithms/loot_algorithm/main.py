from algorithm import Algorithm
from algorithm_test import AlgorithmTestMinimal, AlgorithmTestStress
from minimal_test_data import test_data, data1, data2, data3, data4
from implementations import optimal_value_fast, optimal_value_pop, optimal_value_foundry



# instantiate algorithms
fast_algorithm = Algorithm('optimal_value_fast', optimal_value_fast)
pop_algorithm = Algorithm('optimal_value_pop', optimal_value_pop)
foundry_algorithm = Algorithm('optimal_value_foundry', optimal_value_foundry)

# build test data
algorithms = [pop_algorithm, foundry_algorithm, fast_algorithm]
data = test_data

# run stress tests
stress_algorithm_test = AlgorithmTestStress(algorithms, 30, 9, 200)
stress_algorithm_test.run(1, max_capacity=100)

# run minimal tests
minimal_algorithm_test = AlgorithmTestMinimal(algorithms, data)
minimal_algorithm_test.run()
minimal_algorithm_test.print_results()

