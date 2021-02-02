def fast_algorithm(self, *args, **kwargs):
    # solve the problem here

    s = kwargs.get("s")
    t = kwargs.get("t")

    # build the matrix
    D = [0 for elem in range((len(t) + 1))]
    for i in range(len(D)):
        D[i] = [0 for l in range(len(s) + 1)]

    # add letters to first col
    for i in range(1, len(s) + 1):
        D[0][i] = i

    # add letters to first col of each row
    for i in range(1, len(t) + 1):
        D[i][0] = i

    # compare letters
    for row in range(1, len(t) + 1):
        t_letter = t[row - 1]
        for col in range(1, len(s) + 1):
            s_letter = s[col - 1]
            hor_dist = D[row][col - 1] + 1
            vert_dist = D[row - 1][col] + 1
            if s_letter == t_letter:
                diag_dist = D[row - 1][col - 1]
            else:
                diag_dist = D[row - 1][col - 1] + 1

            D[row][col] = min(vert_dist, hor_dist, diag_dist)

    return D[-1][-1]


def working_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    result = sulution

    return result
