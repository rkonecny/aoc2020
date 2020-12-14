with open('input', "r") as fo:
    list = [int(i) for i in fo.readlines()]

preamble = 25


def isInvalid(index):
    next = int_list[index]
    for i in range(index-preamble, index-1):
        for j in int_list[i+1: index]:
            if int_list[i]+j == next:
                return False
    return True


for x in range(preamble, len(int_list)):
    if isInvalid(x):
        print(int_list[x])
        break
