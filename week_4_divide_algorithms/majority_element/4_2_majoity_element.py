# Uses python3
import sys


def get_majority_element(a, left, right):
    size = len(a)

    value_counts = {}
    for elem in a:
        if elem in value_counts.keys():
            value_counts[elem] += 1
        else:
            value_counts[elem] = 1

    found = False
    for key, value in value_counts.items():
        if value > size / 2:
            found = True
            return key
    if not found:
        return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
