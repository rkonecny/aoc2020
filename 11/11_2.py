with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")


increments = [[-1, -1], [-1, 0], [-1, 1],
              [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

dimensionY = len(list) + 2
dimensionX = len(list[1]) + 2

list1 = [['.' for j in range(dimensionX)] for i in range(dimensionY)]
list2 = [[list[i][j] for j in range(dimensionX-2)]
         for i in range(dimensionY-2)]

for y in range(dimensionY-2):
    for x in range(dimensionX-2):
        list1[y+1][x+1] = list2[y][x]


def getDirectionOccupation(xIncrement, yIncrement, x, y, seating):
    xMod = x + xIncrement
    yMod = y + yIncrement
    returnValue = seating[yMod][xMod]
    while (xMod >= 0 and xMod < dimensionX and yMod >= 0 and yMod < dimensionY):
        returnValue = seating[yMod][xMod]
        if (returnValue != '.'):
            return returnValue
        xMod += xIncrement
        yMod += yIncrement
    return returnValue


def getOccupation(x, y, seating):
    currentSeat = seating[y][x]
    if currentSeat == '.':
        return '.'
    grid = []
    for increment in increments:
        grid.append(getDirectionOccupation(
            increment[0], increment[1], x, y, seating))
    sumOccupied = grid.count('#')
    if currentSeat == 'L' and sumOccupied == 0:
        return '#'
    if currentSeat == '#' and sumOccupied > 4:
        return 'L'

    return currentSeat


oldList = [[list1[i][j] for j in range(dimensionX)] for i in range(dimensionY)]
newList = [['L' for j in range(dimensionX)] for i in range(dimensionY)]

while oldList != newList:
    for y in range(dimensionY):
        for x in range(dimensionX):
            newList[y][x] = getOccupation(x, y, oldList)
    newList, oldList = oldList, newList

print(sum(row.count('#') for row in oldList))
