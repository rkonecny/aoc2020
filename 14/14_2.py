from itertools import product

with open("input", "r") as fo:
    listInput = fo.readlines()

for i in range(len(listInput)):
    listInput[i] = listInput[i].replace("\n", "")

mask = ""

products = {}

values = {}


def replaceX(value, replacement):
    i = 0
    newList = []
    for x in list(value):
        if x == "X":
            newList.append(replacement[i])
            i += 1
        else:
            newList.append(x)

    return "".join(newList)


def generateAddresses(value):
    global products

    xCount = value.count('X')
    if xCount not in products:
        prodList = list(product("01", repeat=xCount))
        products.update({xCount: prodList})

    for x in products[xCount]:
        aaa = replaceX(value, x)
        yield replaceX(value, x)


def applyMask(value):
    binary = format(value, "b")
    binaryForMask = ("0" * (36 - len(binary))) + binary
    maskApplied = "".join([binaryForMask[i] if mask[i] == "0"
                           else mask[i] for i, _ in enumerate(mask)])

    addresses = generateAddresses(maskApplied)
    for address in addresses:
        yield int("0b"+address, 2)


def process(entry):
    global mask

    if entry[0] == "mask":
        mask = entry[1]
        return

    addressess = applyMask(int(entry[0][4:-1]))
    value = int(entry[1])
    for address in addressess:
        values.update({address: value})


for i in listInput:
    x = i.split(" = ")
    process(x)

result = sum(values.values())
print(result)
