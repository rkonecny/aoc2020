with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")

initialState1 = [[(x, y, 0) for x, k in enumerate(l) if k == "#"]
                 for y, l in enumerate(inputList)]

initialState = set()
for x in initialState1:
    initialState.update(x)

print(initialState)


def checkCube(cubeCoordinates, initialState, newState, shouldContinue):
    xBase, yBase, zBase = cubeCoordinates
    isCubeActive = cubeCoordinates in initialState

    count = 0

    for z in range(zBase - 1, zBase + 2):
        for y in range(yBase - 1, yBase + 2):
            for x in range(xBase - 1, xBase + 2):
                if (x, y, z) in initialState:
                    if (x, y, z) != cubeCoordinates:
                        count += 1

                if shouldContinue:
                    checkCube((x, y, z), initialState, newState, False)

    if isCubeActive and 2 <= count <= 3:
        newState.add(cubeCoordinates)
        return

    if not isCubeActive and count == 3:
        newState.add(cubeCoordinates)


for cycle in range(6):
    newState = set()
    for cube in initialState:
        checkCube(cube, initialState, newState, True)

    initialState = newState.copy()

print(len(initialState))
