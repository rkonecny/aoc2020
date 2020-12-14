with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")


def parseEntries():
    parsedEntries = []
    passportFields = set()
    for item in list:
        if item == "":
            parsedEntries.append(passportFields)
            passportFields = set()
            continue

        fields = [x for x in item]
        passportFields.update(fields)

    parsedEntries.append(passportFields)
    return parsedEntries


entries = parseEntries()
counts = [len(x) for x in entries]
print(sum(counts))
