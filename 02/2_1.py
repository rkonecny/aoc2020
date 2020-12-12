fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

def parseLine(line):
  splitted = line.split(" ")
  limits = [int(i) for i in splitted[0].split("-")]
  key = splitted[1].split(":")[0]
  return (limits, key, splitted[2])

def isValid(entry):
  count = entry[2].count(entry[1])
  lowerLimit = entry[0][0]
  upperLimit = entry[0][1]
  return 1 if count >= lowerLimit and count <= upperLimit else 0

validities = map(isValid, map(parseLine, list))
print(sum(validities))