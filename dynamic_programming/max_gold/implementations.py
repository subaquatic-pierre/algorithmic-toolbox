def fast_algorithm(self, *args, **kwargs):
    # solve the problem here

    bars = kwargs.get("w")
    bars.append(0)
    bars = sorted(bars)

    total_weight = kwargs.get("W")

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


def working_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    result = sulution

    return result
