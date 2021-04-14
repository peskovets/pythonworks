a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(a)
b = [el for i, el in enumerate(a) if i > 0 and a[i] > a[i - 1]]
print(b)