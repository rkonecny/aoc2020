with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")

parsedInput = [[i.split(" ")[0], int(i.split(" ")[1])] for i in inputList]


def resetInput():
    return [[x for x in y] for y in parsedInput]


newInput = resetInput()

accessed = [0 for _ in newInput]

accumulator = 0
index = 0

lastChangedIndex = 0


def next():
    global accumulator
    global index

    if index >= len(parsedInput):
        return 1

    op = newInput[index]
    accessed[index] += 1

    if (accessed[index] > 1):
        return -1

    if op[0] == "nop":
        index += 1
        return 0
    if op[0] == "acc":
        index += 1
        accumulator += op[1]
        return 0
    if op[0] == "jmp":
        index += op[1]
        return 0


def changeInput():
    global newInput
    global lastChangedIndex
    global accessed
    global accumulator
    global index

    newInput = resetInput()
    for i in range(lastChangedIndex + 1, len(parsedInput)):
        if parsedInput[i][0] == "nop":
            newInput[i][0] = "jmp"
            lastChangedIndex = i
            break
        if parsedInput[i][0] == "jmp":
            newInput[i][0] = "nop"
            lastChangedIndex = i
            break

    accessed = [0 for _ in newInput]
    index = 0
    accumulator = 0


while True:
    result = next()
    if result == -1:
        changeInput()
        continue
    if result == 0:
        continue
    if result == 1:
        break


print(accumulator)
