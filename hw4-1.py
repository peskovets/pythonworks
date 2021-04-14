from sys import argv
performance, rate, prize = argv
salary = int(performance) * int(rate) + int(prize)
print(f"Заработная плата сотрудника: {salary}")