# Uses python3
import sys

d = {}


def optimal_sequence(n):

    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (optimal_sequence(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = optimal_sequence(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = optimal_sequence(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans


def print_solution(n):
    ans = []
    while optimal_sequence(n)[1] != -1:
        ans.append(n)
        n = optimal_sequence(n)[1]
    ans.append(1)
    ans.reverse()
    print(len(ans) - 1)
    for x in ans:
        print(x, end=" ")


def solve(n):
    for i in range(1, n):
        optimal_sequence(i)[0]
    print_solution(n)
    print("")


# input = sys.stdin.read()
n = int(input())
solve(n)
# sequence = list(build_list(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=" ")
# print()
