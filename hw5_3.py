b = []
with open('test2.txt', 'r') as a:
    for line in a:
        b = line.split()
        if int(b[1]) <= 20000:
            print(b[0])
        else:
            continue
