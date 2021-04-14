from itertools import count, cycle
a = 3
b = 10
for i in count(a):
    print(i, end=' ')
    if i == b:
        print()
        break
c = [1, 2, 3, "four", "five", 6.5]
d = 15
for num, el in enumerate(cycle(c)):
    print(el, end=' ')
    if num == d:
        print()
        break