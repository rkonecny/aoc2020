import math
with open("input", "r") as fo:
    input = fo.readlines()

busLines = [(int(x), int(x)-i)
            for i, x in enumerate(input[1].split(",")) if x.isdigit()]


# chinese remainder
product = math.prod([x[0] for x in busLines])
total = sum(y * pow(product // x, -1, x) * (product // x) for x, y in busLines)
print(total % product)
