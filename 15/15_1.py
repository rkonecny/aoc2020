with open("input", "r") as fo:
    listInput = fo.read()

numbers = {int(x): i+1 for i, x in enumerate(listInput.split(',')[:-1])}


def getNumber(last, index):
    if last in numbers:
        number = index - numbers[last]
        numbers[last] = index
        return number

    numbers[last] = index
    return 0


limit = 2020

lastSpoken = int(listInput.split(',')[-1])

for i in range(len(numbers) + 1, limit):
    lastSpoken = getNumber(lastSpoken, i)

print(lastSpoken)
