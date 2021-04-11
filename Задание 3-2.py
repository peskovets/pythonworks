def my_func(**kwargs):
    config = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
    kwargs = {}
    for filed in config:
        kwargs[filed] = input(f'Введите значение поля {filed}: ')
    info = kwargs.values()
    return  '  '.join(info)

print(my_func())