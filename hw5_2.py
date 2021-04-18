stroka = 0
space = 0
with open('hw_text_1.txt', 'r') as f:
   for line in f:
       stroka += 1
       if line.count(' ') == 0:
           space += 1
       elif line.count(' ') == 1:
           space += 2
       else:
           space = space + line.count(' ') + 1

print(f'Количество строк:{stroka}')
print(f'Количество символов:{space}')