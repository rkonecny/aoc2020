with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")

list_length = len(list[0])

x = 0
trees = 0

for i in range(1, len(list)):
    x = (x + 3) % list_length
    if list[i][x] == '#':
        trees += 1

print(trees)
