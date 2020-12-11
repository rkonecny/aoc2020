fo = open('input', "r")
int_list = [int(i) for i in fo.readlines()]
int_list.sort()
fo.close()

memo = {int_list[-1]+3: 1}

def resolve(i):
  if (memo.get(i) == None):
    memo[i] = 0 if int_list.count(i) == 0 else resolve(i+1) + resolve(i+2) + resolve(i+3)
  return memo[i]

resolve(0)

print(memo[0])