def fast_algorithm(self, *args, **kwargs):
    a = kwargs.get("list_1")
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


def working_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    result = sulution

    return result
