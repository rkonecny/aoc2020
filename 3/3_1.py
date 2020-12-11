fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

list_length = len(list[0])

x = 0
trees = 0

for i in range(1, len(list)):  
  x = (x + 3) % list_length
  if list[i][x] == '#':
    trees += 1

print(trees)