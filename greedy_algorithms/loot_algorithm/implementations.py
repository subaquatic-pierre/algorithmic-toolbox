def optimal_value_fast(self, *args, **kwargs):
    total_value = 0

    # get arguments
    weights = kwargs.get('weights')
    values = kwargs.get('values')
    capacity = kwargs.get('capacity')

    # combine weigths and values
    combined_data = [(a,b) for a,b in zip(weights, values)]

    # sort by tge greatest ratio
    sorted_vals = sorted(combined_data, key=lambda sub: abs(sub[1] - sub[0]), reverse=True)

    index = 0
    tmp_capacity = capacity 
    for item in sorted_vals:
        item_weight = item[0]
        item_value = item[1]

        if tmp_capacity > 0 and tmp_capacity - item_weight >= 0:
            total_value = total_value + item_value
            tmp_capacity = tmp_capacity - item_weight
            index += 1

            continue

        elif tmp_capacity == 0:
            return total_value

    
    if tmp_capacity > 0 and index != len(values):
        value_ratio = item_value / item_weight
        dif = tmp_capacity % item_weight
        total_value = total_value + (value_ratio * dif)

    result = total_value

    return result



def optimal_value_pop(self, *args, **kwargs):
    total_value = 0

    weights = kwargs.get('weights')
    values = kwargs.get('values')
    capacity = kwargs.get('capacity')

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


def optimal_value_foundry(self, *args, **kwargs):
    total_value = 0

    weights = kwargs.get('weights')
    values = kwargs.get('values')
    capacity = kwargs.get('capacity')

    index = list(range(len(values)))
    # contains ratios of valuess to weight
    ratio = [v/w for v, w in zip(values, weights)]
    # index is sorted according to values-to-weights ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    fractions = [0]*len(values)
    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            total_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity/weights[i]
            total_value += values[i]*capacity/weights[i]
            break

    result = total_value

    return result