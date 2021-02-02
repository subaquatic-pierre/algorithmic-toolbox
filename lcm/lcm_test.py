import sys

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 1:
        return b
    m = a % b
    return b if m == 0 else gcd(b, m)

def lcm(a,b):
    return a * b / gcd(a,b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # a = 10565
    # b = 10567
    print(int(lcm(a, b)))