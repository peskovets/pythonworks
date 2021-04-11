# Вариант 1
def my_func(x,y):
    new_x = round(abs(x))
    new_y = round(abs(y))
    return 1 / new_x ** new_y
example = my_func(2,-3)
print(example)

# Вариант 2
def my_func(x,y):
    new_x = round(abs(x))
    new_y = round(abs(y))
    if new_y == 0:
        print("Неверно введены аргументы функции")
    elif new_y == 1:
        return 1 / new_x
    else:
        i = 2
        b = new_x * new_x
        while i < new_y:
            b = b * new_x
            i = i + 1
    return 1 / b

example2 = my_func(2,-3)
print(example2 )