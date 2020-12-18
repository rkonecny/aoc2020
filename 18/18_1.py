with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")
    inputList[i] = inputList[i].replace("(", "( ")
    inputList[i] = inputList[i].replace(")", " )")


lines = [[x for x in y.split(" ")] for y in inputList]


def calcOperation(i, j, operation):
    if operation == "*":
        return i * j
    if operation == "+":
        return i + j

    return j


def calculate(inputString, sum, i):
    operation = ""

    while i < len(inputString):
        if inputString[i] == '(':
            innerSum, i = calculate(inputString, 0, i + 1)
            sum = calcOperation(sum, innerSum, operation)
            if i >= len(inputString):
                break
        if inputString[i] == ')':
            return (sum, i + 1)
        if inputString[i] in ["+", "*"]:
            operation = inputString[i]
        if inputString[i].isdigit():
            sum = calcOperation(sum, int(inputString[i]), operation)

        i += 1

    return (sum, i)


results = [calculate(x, 0, 0)[0] for x in lines]

print(sum(results))
