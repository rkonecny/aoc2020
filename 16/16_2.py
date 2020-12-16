with open('input', "r") as fo:
    inputList = fo.readlines()

for i in range(len(inputList)):
    inputList[i] = inputList[i].replace("\n", "")


def parseRule(input):
    key, rules = input.split(": ")
    numbers = rules.split(" or ")
    values = [x.split("-") for x in numbers]
    return (key, [[int(i) for i in x] for x in values])


def parseInput(input):
    rules = []
    for line in input:
        if line == "":
            break
        rules.append(parseRule(line))

    ticketsIndex = input.index("nearby tickets:")
    tickets = [[int(x) for x in y.split(',')] for y in input[ticketsIndex+1:]]

    myTicketIndex = input.index("your ticket:")
    myTicket = [int(x) for x in input[myTicketIndex+1].split(',')]

    return (rules, tickets, myTicket)


def checkNumberInRules(number, rules):
    for key, ruleLine in rules:
        if number >= ruleLine[0][0] and number <= ruleLine[0][1] or number >= ruleLine[1][0] and number <= ruleLine[1][1]:
            return True

    return False


def checkTicketValid(ticket, rules):
    sumOfInvalid = 0
    for ticketNumber in ticket:
        if not checkNumberInRules(ticketNumber, rules):
            return False

    return True


def checkNumberInRule(number, ruleLine):
    return number >= ruleLine[0][0] and number <= ruleLine[0][1] or number >= ruleLine[1][0] and number <= ruleLine[1][1]


def checkTicket(ticket, rules):
    for i, _ in enumerate(ticket):
        if not checkNumberInRule(ticket[i], rules[i][1]):
            return False

    return True


def getPossibleRulesOrder(tickets, rules):
    possibleRulesOrder = []
    for rule in rules:
        ruleLine = [True for x in rules]
        for ticket in tickets:
            for i, x in enumerate(ticket):
                if not checkNumberInRule(x, rule[1]):
                    ruleLine[i] = False
        possibleRulesOrder.append((rule[0], ruleLine))

    return possibleRulesOrder


def getPossibleRulesOrderCount(rulesOrderSet):
    result = []
    for i in range(len(rulesOrderSet[0][1])):
        summage = sum([x[1][i] for x in rulesOrderSet])
        result.append(summage)
    return result


def getProperRuleOrder(rules, squash, result):
    index = squash.index(1)
    ruleToRemove = [x[0] for x in rules if x[1][index] == True][0]
    newRules = [x for x in rules if x[0] != ruleToRemove]

    result.append((ruleToRemove, index))

    if len(newRules) > 0:
        getProperRuleOrder(
            newRules, getPossibleRulesOrderCount(newRules), result)

    return result


def getDepartureSum(myTicket, rulesOrder):
    departureSum = 1
    for rule in rulesOrder:
        if "departure" in rule[0]:
            departureSum *= myTicket[rule[1]]

    return departureSum


rules, tickets, myTicket = parseInput(inputList)

validTickets = [x for x in tickets if checkTicketValid(x, rules)]
correctRulesOrder = getPossibleRulesOrder(validTickets, rules)

squashed = getPossibleRulesOrderCount(correctRulesOrder)
result = getDepartureSum(myTicket, getProperRuleOrder(
    correctRulesOrder, squashed, []))
print(result)
