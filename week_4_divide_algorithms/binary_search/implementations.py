def fast_algorithm(self, *args, **kwargs):
    list_1 = sorted(kwargs.get("list_1"))
    list_2 = kwargs.get("list_2")

    indeces = []

    l = len(list_1)
    for key in list_2:
        m = len(list_1) // 2
        checked = []

        while True:
            elem = list_1[m]
            checked.append(m)
            if key == elem:
                indeces.append(m)
                break
            elif key < elem:
                tmp = m // 2
                if m == 0:
                    indeces.append(-1)
                    break
                if tmp == 0:
                    m = 0
                else:
                    m = 0 + tmp

                # if index is already checked append not found, break
                if m in checked:
                    indeces.append(-1)
                    break

            else:
                tmp = (l - m) // 2
                if tmp == 2:
                    tmp = 1
                m = m + tmp

    return indeces


def working_algorithm(self, *args, **kwargs):

    list_1 = sorted(kwargs.get("list_1"))
    list_2 = kwargs.get("list_2")

    indeces = []
    for key in list_2:
        try:
            indeces.append(list_1.index(key))
        except ValueError:
            indeces.append(-1)

    return indeces
