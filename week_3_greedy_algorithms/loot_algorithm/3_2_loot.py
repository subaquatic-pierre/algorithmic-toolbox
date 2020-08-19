import sys

def get_optimal_value(capacity, weights, values):
    total_value = 0
    
    combined_data = [(a,b) for a,b in zip(weights, values)]
    sorted_data = sorted(combined_data, key=lambda sub: abs(sub[1] / sub[0]))

    while sorted_data:
        item = sorted_data.pop()
        weight, value = item

        if capacity == 0: break

        if weight < capacity:
            total_value += value
            capacity -= weight
            continue

        remaining_value = value * (capacity/weight)
        total_value += remaining_value
        capacity = 0

    result = total_value

    return result


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))