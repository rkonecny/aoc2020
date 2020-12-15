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


def reverseRules(rules):
    reverseRules = {}
    for key in rules:
        for rule in rules[key]:
            if rule[0] in reverseRules:
                reverseRules[rule[0]].add(key)
            else:
                reverseRules[rule[0]] = {key}

    return reverseRules


def expand(oldBase, ruleset):
    newBase = {x for x in oldBase}
    for rule in oldBase:
        if rule in ruleset:
            newBase.update(ruleset[rule])

    if oldBase == newBase:
        return newBase

    return expand(newBase, ruleset)


rules = dict(parseLine(x) for x in inputList)

reverseRules = reverseRules(rules)

base = {'shiny gold'}
result = expand(base, reverseRules)
print(len(result) - 1)
