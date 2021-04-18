b = {}
c = []
d = []
with open('test6.txt', 'r') as a:
    for line in a:
        c = line.replace('(', ' ').split()
        print(c)
        for el in c:
            try:
                d.append(int(el))
            except  IndexError:
                continue
            except ValueError:
                continue
        b[c[0]] = d[:]
        d.clear()

for k, v in b.items():
    b[k] = sum(v)
print(b)
