with open("input", "r") as fo:
    input = fo.readlines()

departTimestamp = int(input[0])
busLines = [int(x) for x in input[1].split(",") if x.isdigit()]

earliestDepartures = []

for i in busLines:
    x = departTimestamp // i
    earliestDepart = i * (x+1)
    earliestDepartures.append(earliestDepart)

firstDepart = min(earliestDepartures)
index = earliestDepartures.index(firstDepart)
busLine = busLines[index]
print(busLine * (firstDepart - departTimestamp))
