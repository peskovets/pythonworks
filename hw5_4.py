f = open('test4.txt', 'w')
n = 0
with open('test3.txt', 'r+') as a:
    for line in a:
        n += 1
        if n == 1:
            print(line.replace('One', 'Один'))
            f.write(line.replace('One', 'Один'))
        elif n == 2:
            print(line.replace('Two', 'Два'))
            f.write(line.replace('Two', 'Два'))
        elif n == 3:
            print(line.replace('Three', 'Три'))
            f.write(line.replace('Three', 'Три'))
        else:
            print(line.replace('Four', 'Четыре'))
            f.write(line.replace('Four', 'Четыре'))
f.close()