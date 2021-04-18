my_file = open('new_text.txt', 'w')
stroka = input()
while True:
    my_file.writelines(f"{stroka}\n")
    stroka = input()
    if not stroka:
        break
my_file.close()




