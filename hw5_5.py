f = open('test7.txt', 'w')
f.write("100 90 80 70 60 50 40 30 20 10")
f.close()
c = []
d = []
sum_f = 0
with open('test7.txt') as a:
    b = a.read()
    c = b.split()
    print(c)
    for el in c:
        d.append(int(el))
    for el in d:
        sum_f = sum_f + el
print(sum_f)