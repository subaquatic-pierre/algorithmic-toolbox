def fast_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    coins = kwargs.get("coins")
    amount = kwargs.get("amount")

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
        values = D[0]

        # skip first row
        if row == 0:
            continue

        for col in range(1, len(values)):
            if D[row][0] > values[col]:
                D[row][col] = D[row - 1][col]
            else:
                D[row][col] = min(D[row - 1][col], 1 + D[row][col - D[row][col]])

        print(D[row])

    result = solution

    return result


def working_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    result = solution

    return result
