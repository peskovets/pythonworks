def my_func(a=int(input("a = ")), b=int(input("b = "))):
    if b == 0:
        return "На ноль делить нельзя!"
    else:
        return a / b

print(my_func())