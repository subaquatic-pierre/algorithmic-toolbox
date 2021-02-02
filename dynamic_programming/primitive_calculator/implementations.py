def f(n):
    d = {}

    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans


def build_list(n):
    ans = []
    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]
    ans.reverse()
    return ans
    for x in ans:
        print(x)


def solve(n):
    for i in range(1, n):
        f(i)[0]
    ans = print_solution(n)
    return ans


def fast_algorithm(self, *args, **kwargs):

    n = kwargs.get("n")

    result = solve(n)
    print(result)

    return result


def working_algorithm(self, *args, **kwargs):
    # solve the problem here
    solution = 42

    result = sulution

    return result
