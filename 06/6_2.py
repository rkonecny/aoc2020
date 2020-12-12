fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

def parseEntries():
  parsedEntries = []
  passportFields = set()
  newGroup = True
  for item in list:
    if item == "":
      parsedEntries.append(passportFields)
      passportFields = set()
      newGroup = True
      continue

    fields = [x for x in item]
    if newGroup:
      passportFields.update(fields)
      newGroup = False
    else :
      passportFields = passportFields.intersection(fields)

  parsedEntries.append(passportFields)
  return parsedEntries

entries = parseEntries()
counts = [len(x) for x in entries]
print(sum(counts))