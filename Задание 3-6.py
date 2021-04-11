# Задача 6-7
# (возможно, неправильно понимаю задание, но созданная функция преобразует как слова так и стороки,
# зависит от того, что вводим)
def int_func(text):
    text = text.lower()
    return text.title()
# Проверка на слове
print(int_func("education"))

# Проверка на строке
a = input("Введите несколько латинских слов в нижнем регистре:")
print(int_func(a))

print(int_func("homo homini lupus est"))