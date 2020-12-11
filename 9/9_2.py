fo = open('input', "r")
int_list = [int(i) for i in fo.readlines()]
fo.close()

number = 23278925


def getInterval():
  for i in range(len(int_list)):
    sum = int_list[i]
    for j in range(i+1, len(int_list)):
      sum += int_list[j]
      if sum > number:
        break
      if sum == number:
        return(i,j)

interval = getInterval()

sorted = int_list[interval[0]: interval[1]+1]
sorted.sort()
print(sorted[0] + sorted[-1])