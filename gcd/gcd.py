import sys

def get_gcd(num1, num2):
    if num2 == 0:
        return num1
    
    remainder = num1 % num2
    
    return  get_gcd(num2, remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(get_gcd(a, b))