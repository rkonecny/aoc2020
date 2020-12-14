with open("input", "r") as fo:
    listInput = fo.readlines()

for i in range(len(listInput)):
    listInput[i] = listInput[i].replace("\n", "")

mask = ""

values = {}


def applyMask(value):
    binary = format(value, "b")
    binaryForMask = ("0" * (36 - len(binary))) + binary
    maskApplied = "".join([mask[i] if mask[i] !=
                           "X" else binaryForMask[i] for i, _ in enumerate(mask)])

    return int("0b"+maskApplied, 2)


def process(entry):
    global mask

    if entry[0] == "mask":
        mask = entry[1]
        return

    address = int(entry[0][4:-1])
    value = applyMask(int(entry[1]))
    values.update({address: value})


for i in listInput:
    x = i.split(" = ")
    process(x)

result = sum(values.values())
print(result)
