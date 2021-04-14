from itertools import count
from math import factorial

def my_func_generator():
    for el in count(1):
        yield factorial(el)

gen = my_func_generator()
x = 0
for el in gen:
    if x < 10:
        print(el)
        x += 1
    else:
        break