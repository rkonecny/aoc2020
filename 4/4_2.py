import re

fo = open("input", "r")
list = [i for i in fo.readlines()]
for i in range(len(list)):
  list[i] = list[i].replace("\n", "")
fo.close()

requiredFields = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']

def parseEntries():
  parsedEntries = []
  passportFields = {}
  for item in list:
    if item == "":
      parsedEntries.append(passportFields)
      passportFields = {}
      continue

    fields = {x[0]: x[1] for x in [x.split(":") for x in item.split(" ")]}
    passportFields.update(fields)

  parsedEntries.append(passportFields)
  return parsedEntries

def checkInterval(input, min, max):
  s = input
  year = int(s) if s.isdigit() else -1
  return min <= int(year) <= max  

def checkByr(passport):
  return checkInterval(passport['byr'], 1920, 2002)

def checkIyr(passport):
  return checkInterval(passport['iyr'], 2010, 2020)

def checkEyr(passport):
  return checkInterval(passport['eyr'], 2020, 2030)

def checkHgt(passport):
  min = {"cm": 150, "in": 59}
  max = {"cm": 193, "in": 76}
  s = passport['hgt']
  unit = s[-2:]
  if unit not in ['cm', 'in']:
    return False
    
  return checkInterval(s[:-2], min[unit], max[unit])

def checkHcl(passport):
  return re.fullmatch(r"#([a-f]|\d){6}", passport['hcl'])

def checkEcl(passport):
  return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].count(passport['ecl']) == 1

def checkPid(passport):
  return re.fullmatch(r"\d{9}", passport['pid'])

def checkPassportFields(passport):
  keys = [*passport]
  for field in requiredFields:
    if keys.count(field) == 0:
      return False
      
  return True

def checkPassport(passport):
  checks = [checkByr, checkIyr, checkEyr, checkHgt, checkHcl, checkEcl, checkPid]
  return checkPassportFields(passport) and all([x(passport) for x in checks])

entries = parseEntries()
passportsCheck = [checkPassport(passport) for passport in entries]
print(passportsCheck.count(True))
