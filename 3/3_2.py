from functools import reduce

fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

list_length = len(list[0])

def treeSum(right, down):
  x = 0
  trees = 0

  for i in range(down, len(list), down):  
    x = (x + right) % list_length
    if list[i][x] == '#':
      trees += 1

  return trees


result = [treeSum(1,1), treeSum(3,1), treeSum(5,1), treeSum(7,1), treeSum(1,2)]
print(result)
print(reduce((lambda x, y: x * y), result))