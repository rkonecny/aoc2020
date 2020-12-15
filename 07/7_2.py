import re

with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")


def patternMatch(rules):
    for rule in rules:
        match = re.search("([\s\d]+)([\D]*)\sbag.*", rule)
        yield (match.group(2), int(match.group(1)))


def parseRule(rule):
    if rule == "no other bags.":
        return []

    rules = rule.split(",")

    return list(patternMatch(rules))


def parseLine(line):
    bag, rule = line.split(" contain ")
    return ("".join(bag.split(" bags")[:-1]), parseRule(rule))


def getBagsInBags(oldBags, ruleset):
    newBags = []
    for oldBag in oldBags:
        newBags.extend([(bag, quantity * oldBag[1])
                        for bag, quantity in ruleset[oldBag[0]]])
    return newBags


def getBags(base, bags, ruleset):
    bags.append(base)
    inBags = getBagsInBags(base, ruleset)
    if inBags == []:
        return bags

    return getBags(inBags, bags, ruleset)


rules = dict(parseLine(x) for x in inputList)


base = [('shiny gold', 1)]
allBags = getBags(base, [], rules)
count = sum([sum([count for bag, count in depth]) for depth in allBags])
print(count - 1)
