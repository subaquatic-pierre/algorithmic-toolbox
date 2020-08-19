import sys

def calc_fib(n):
    prev = 0
    cur = 1
    total = 0

    if n <=1:
        return n

    for i in range(0,n-1):
        total = cur + prev
        prev = cur
        cur = total

    return total

# n = int(input())
# print(calc_fib(n))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calc_fib(n))