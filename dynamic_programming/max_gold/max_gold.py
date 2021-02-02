# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    bars = w
    bars.append(0)
    bars = sorted(bars)

    total_weight = W

    # build matrix
    D = [0 for weight in range(len(bars))]

    for i in range(len(bars)):
        D[i] = [0 for weight in range(total_weight + 1)]

    for row in range(len(D)):
        bar = bars[row]
        for weight in range(total_weight + 1):
            above_cell = D[row - 1][weight]
            if bar > weight:
                D[row][weight] = above_cell
            else:
                added_bar_value = bar + D[row - 1][weight - bar]
                D[row][weight] = max(above_cell, added_bar_value)

    result = D[-1][-1]

    return result


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
