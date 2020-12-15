with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")

parsedInput = [(i.split(" ")[0], int(i.split(" ")[1])) for i in inputList]

accessed = [0 for _ in parsedInput]

accumulator = 0
index = 0


def next():
    global accumulator
    global index

    op = parsedInput[index]
    accessed[index] += 1

    if (accessed[index] > 1):
        return False

    if op[0] == "nop":
        index += 1
        return True
    if op[0] == "acc":
        index += 1
        accumulator += op[1]
        return True
    if op[0] == "jmp":
        index += op[1]
        return True


while next():
    continue

print(accumulator)
