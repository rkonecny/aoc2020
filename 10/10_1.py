fo = open('input', "r")
int_list = [int(i) for i in fo.readlines()]
int_list.sort()
fo.close()

ones = 1
threes = 1

for i in range(len(int_list)-1):
  diff = int_list[i+1] - int_list[i] 
  if (diff == 1): 
    ones = ones + 1
    continue
  if (diff == 3):
    threes = threes + 1
    continue

print(ones*threes)
