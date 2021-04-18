import json
profit = {}
pr = {}
average_profit = 0
firm_profit = 0
i = 0
with open("test8.txt") as f:
    for line in f:
        name, mode, income, outlay = line.split()
        profit[name] = int(income) - int(outlay)
        if profit.setdefault(name) >= 0:
            firm_profit = firm_profit + profit.setdefault(name)
            i += 1
        if i != 0:
            average_profit = firm_profit / i
            print(f'Средняя прибыль: {average_profit}')
        else:
            print('У всех фирм убыток')
        pr = {'average profit': round(average_profit)}
        profit.update(pr)
        print(f'Прибыль фирм: {profit}')

with open("test8.json", "w") as js:
    json.dump(profit, js)
    js_str = json.dumps(profit)