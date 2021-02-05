
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой —
# цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
# как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import namedtuple

BASE = 16
digits = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

print('Программа суммирования двух шестнадцатиричных чисел.')
num_1  = list(input('Введите первое шестнадцатиричное число: '))
num_2  = list(input('Введите второе шестнадцатиричное число: '))
# print(number_1, number_2)

arr_spam = []
num_res = []
next_dig = 0

# print(digits.index(num_1[len(num_1) - 1]))

if len(num_1) > len(num_2):
    len_res = len(num_1) + 1
else:
    len_res = len(num_2) + 1

for i in range(len_res):
    if len(num_1) - i > 0:
        dig_1 = num_1[len(num_1) - 1 - i]
    else:
        dig_1 = '0'
    if len(num_2) - i > 0:
        dig_2 = num_2[len(num_2) - 1 - i]
    else:
        dig_2 = '0'
    print(dig_1, dig_2)

    if digits.index(dig_1) + digits.index(dig_2) < BASE - 1:
        arr_spam.append(digits[digits.index(dig_1) + digits.index(dig_2) + next_dig])
        print(arr_spam)
        next_dig = 0
    else:
        arr_spam.append(digits[digits.index(dig_1) + digits.index(dig_2) - BASE + next_dig])
        print(arr_spam)
        next_dig = 1

print(arr_spam)

for i in range(len_res):
    num_res.append(arr_spam[len_res - 1 - i])

print(num_res)
