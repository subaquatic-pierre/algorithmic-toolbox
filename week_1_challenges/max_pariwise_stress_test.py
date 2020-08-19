# python3
import random
from max_pairwise_product import max_pairwise_product
from week_1.max_pairwise_product_fast import get_max_pairwaise_fast

random.seed(1)

def stress_test(array_len, max_num):
    nums = []
    for num in range(random.randint(1,array_len)):
        num = random.randint(0, max_num)
        nums.append(num)

    naive_result = max_pairwise_product(nums)
    fast_result = get_max_pairwaise_fast(nums)

    while True:
        if naive_result != fast_result:
            print('\n---- PROBLEM ------\n')
            print('Array length: ', array_len)
            print('Numbers: ', nums)
            print('Naive Solution: ', naive_result)
            print('Fast Solution: ', fast_result)
            print('\n---- ------- ------\n')
            break
        else:
            print('--- OK ---')

stress_test(100, 10000)