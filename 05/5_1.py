with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")


def getPosition(upper, lowerIdentifier, sequence):
    min = 0
    max = upper
    for i in sequence:
        avg = (min + max) // 2
        if i == lowerIdentifier:
            max = avg
        else:
            min = avg + 1

    return min


def getSeat(sequence):
    row = getPosition(127, "F", sequence[:7])
    column = getPosition(7, "L", sequence[7:])
    return row * 8 + column


seatIds = [getSeat(seq) for seq in list]
print(max(seatIds))
