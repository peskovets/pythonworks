def my_func():
    res = 0
    while True:
        numbers = input("Введите список чисел или q для выхода").split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Результат - {res}')
                    return
                else:
                    res += int(i)
            except ValueError:
                print("Введите число или 'q'")
        print(f'Результат - {res}')

my_func()