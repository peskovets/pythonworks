from functools import reduce
print(reduce(lambda x, y: x * y, [el for el in list(range(100, 1002, 2))]))
