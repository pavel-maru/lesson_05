
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

quantity = int(input('Введите количество предприятий: '))

collect = defaultdict(list)
sum = 0

for num in range(quantity):
    collect[num, 0] = input(f'\nВведите название {num + 1} предприятия: ')
    profit = 0
    for quart in [1, 2, 3, 4]:
        profit += float(input(f'Введите прибыль предприятия {collect[num, 0]} за {quart} квартал: '))

    collect[num, 1] = profit
    sum += collect[num, 1]

# print(collect)

av_profit = sum / quantity
print(f'\nСредняя прибыль по всем предприятиям за год: {av_profit}')

print('\nПредприятия, у которых прибыль выше средней: ')
for num in range(quantity):
    if collect[num, 1] > av_profit:
        print(collect[num, 0])

print('\nПредприятия, у которых прибыль ниже средней: ')
for num in range(quantity):
    if collect[num, 1] < av_profit:
        print(collect[num, 0])
