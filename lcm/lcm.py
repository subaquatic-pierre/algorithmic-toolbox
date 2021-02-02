# Uses python3
import sys

def get_lcm(num1, num2):
    biggest_num = max(num1,num2)
    smallest_num = min(num1,num2)
    dif = biggest_num - smallest_num

    if biggest_num % smallest_num == 0:
        return biggest_num

    for i in range(dif,smallest_num):
        prod = biggest_num * i
        res1 = prod % num1 
        res2 = prod % num2
        if res1 == 0 and res2 ==0:
            return prod

    return biggest_num * smallest_num


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(get_lcm(a, b))

