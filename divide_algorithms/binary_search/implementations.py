def fast_algorithm(self, *args, **kwargs):
    list_a = sorted(kwargs.get("list_a"))
    list_b = kwargs.get("list_b")

    indeces = []
    for elem in list_b:
        print(elem)
        indeces.append(binary_search(list_a, elem))

    return indeces


def working_algorithm(self, *args, **kwargs):

    list_1 = sorted(kwargs.get("list_a"))
    list_2 = kwargs.get("list_b")

    indeces = []
    for key in list_2:
        try:
            indeces.append(list_1.index(key))
        except ValueError:
            indeces.append(-1)

    return indeces
