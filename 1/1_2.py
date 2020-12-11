fo = open('input', "r")
list = [int(i) for i in fo.readlines()]
fo.close()

def solve():
  for i in range(len(list)):
    for j in range(i, len(list)):
      for k in range(j, len(list)):
        if list[i] + list[j] + list[k] == 2020:
          return [list[i], list[j], list[k]]

solution = solve()
print(solution[0], solution[1], solution[2], solution[0]*solution[1]*solution[2])