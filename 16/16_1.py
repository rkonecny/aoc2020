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

    return (rules, tickets)


def checkNumberInRules(number, rules):
    for key, ruleLine in rules:
        if number >= ruleLine[0][0] and number <= ruleLine[0][1] or number >= ruleLine[1][0] and number <= ruleLine[1][1]:
            return True

    return False


def checkTicket(ticket, rules):
    sumOfInvalid = 0
    for ticketNumber in ticket:
        if not checkNumberInRules(ticketNumber, rules):
            sumOfInvalid += ticketNumber

    return sumOfInvalid


rules, tickets = parseInput(inputList)
sumOfInvalidTickets = sum([checkTicket(ticket, rules) for ticket in tickets])
print(sumOfInvalidTickets)
