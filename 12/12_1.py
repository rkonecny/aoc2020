fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

navigationList = [(x[0], int(x[1:])) for x in list]
directions = ['E', 'S', 'W', 'N']
direction = 'E'
eastSouth = [0,0]

def getDirection(input):
  global direction
  degrees = input[1] if input[0] == 'R' else 360-input[1]
  x = degrees // 90
  index = (directions.index(direction) + x) % 4
  
  direction = directions[index]
  return (direction, 0)


def getMove(input):
  if ['E', 'W', 'N', 'S'].count(input[0]) == 1:
    return input
  if input[0] == 'F':
    return (direction, input[1])
  
  return getDirection(input)


def move(input):
  input = getMove(input)
  if input[0] == 'E':
    eastSouth[0] += input[1]
    return
  if input[0] == 'W':
    eastSouth[0] -= input[1]
    return
  if input[0] == 'S':
    eastSouth[1] += input[1]
    return
  if input[0] == 'N':
    eastSouth[1] -= input[1]
    return

for i in navigationList:
  move(i)

print(eastSouth)
print(abs(eastSouth[0]) + abs(eastSouth[1]))