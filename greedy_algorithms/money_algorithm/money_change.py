# Uses python3
import sys

def get_change(m):
    tens = 0
    fives = 0
    ones = 0
    money = m
    while money > 0:
        if money % 10 == 0:
            tens = money // 10
            return tens

        tens = money // 10
        money = money - (tens * 10)

        if money % 5 == 0:
            fives = money // 5
            return fives + tens

        fives = money // 5
        money = money - (fives * 5)

        ones = money // 1
        money = money - (ones * 1)

        return tens + fives + ones

# n = 18
# print(get_change(n))
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
