# Uses python3
import sys


def get_change(m):
    coins = [4, 3, 1]
    amount = m

    D = [coin for coin in coins]
    D.insert(0, 0)

    # build matrix
    for i in range(len(coins) + 1):
        D[i] = [0 for num in range(amount + 2)]
        if i == 0:
            D[i][0] = 0
            D[i][1] = 0
            for j in range(1, amount + 1):
                D[i][j + 1] = j
        else:
            D[i][0] = coins[i - 1]

    for row in range(len(D)):
        # skip first row
        if row == 0:
            continue

        for col in range(1, amount + 2):
            cell_above = D[row - 1][col]
            coin = D[row][0]
            value = D[0][col]
            if coin > col:
                D[row][col] = cell_above
            else:
                D[row][col] = min(cell_above, 1 + D[row][col - coin])

    result = D[-1][-1]

    return result


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
