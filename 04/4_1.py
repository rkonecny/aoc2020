with open('input', "r") as fo:
    list = fo.readlines()

for i in range(len(list)):
    list[i] = list[i].replace("\n", "")

requiredFields = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']


def parseEntries():
    parsedEntries = []
    passportFields = []
    for item in list:
        if item == "":
            parsedEntries.append(passportFields)
            passportFields = []
            continue

        fields = [x[0] for x in [x.split(":") for x in item.split(" ")]]
        passportFields += fields

    parsedEntries.append(passportFields)
    return parsedEntries


def checkPassport(passport):
    for field in requiredFields:
        if passport.count(field) == 0:
            return False

    return True


entries = parseEntries()
passportsCheck = [checkPassport(passport) for passport in entries]
print(passportsCheck.count(True))
