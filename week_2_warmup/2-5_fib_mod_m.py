import sys

def calc_fib_mod_m(n,m):
    prev = 0
    cur = 1
    total = 0

    if n == 1:
        return 0
    if n == 2:
        return 1

    for i in range(0,n-1):
        total = cur + prev
        prev = cur
        cur = total

    return total % m

n = int(input())
m = int(input())

print(calc_fib_mod_m(n,m))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(calc_fib_mod_m(n))