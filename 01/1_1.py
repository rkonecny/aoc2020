with open('input', "r") as fo:
    list = [int(i) for i in fo.readlines()]


def solve():
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] + list[j] == 2020:
                return [list[i], list[j]]


solution = solve()
print(solution[0], solution[1], solution[0] * solution[1])
