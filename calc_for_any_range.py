
# Программа сложения двух чисел в любой системе счисления. 

from collections import deque

print("Калькулятор позволяет суммировать числа в любой системе счисления.")
BASE = int(input('Введите размерность (число от 2 до 36): '))
# DIGITS = ('0', '1', '2')

FIRST_LETTER = 97

if BASE <= 10:
    DIGITS = [str(sym) for sym in range(BASE)]
    DIGITS = tuple(DIGITS)
    # print(type(DIGITS), DIGITS)
else:
    DIGITS = [str(sym) for sym in range(10)]
    # print(type(DIGITS))
    for i in range(FIRST_LETTER, FIRST_LETTER + BASE - 10):
        DIGITS.append(chr(i).upper())
    DIGITS = tuple(DIGITS)
    # print(type(DIGITS), DIGITS)

print(f'\nПоследовательность символов (цифр) в данной размерности:\n{DIGITS}\n')

num_res = deque()
# print(type(num_res))
overflow = 0

num_1  = deque(input('Введите первое число в выбранном представлении: ').upper())
num_2  = deque(input('Введите второе число в выбранном представлении: ').upper())
# print(number_1, number_2)

# print(digits.index(num_1[len(num_1) - 1]))

len_res = max(len(num_1), len(num_2)) + 1

for i in range(len_res):
    if len(num_1) - i > 0:
        dig_1 = num_1[len(num_1) - 1 - i]
    else:
        dig_1 = '0'
    if len(num_2) - i > 0:
        dig_2 = num_2[len(num_2) - 1 - i]
    else:
        dig_2 = '0'
    # print(dig_1, dig_2)

    index_spam = DIGITS.index(dig_1) + DIGITS.index(dig_2) + overflow

    if index_spam < BASE:
        num_res.appendleft(DIGITS[index_spam])
        # print(num_res)
        overflow = 0
    else:
        num_res.appendleft(DIGITS[index_spam - BASE])
        # print(num_res)
        overflow = 1

# print(num_res)

# num_res.reverse()
# print(num_res)

if num_res[0] == '0':
    del num_res[0]
# print(num_res)

num_1 = ''.join(num_1)
num_2 = ''.join(num_2)
num_res = ''.join(num_res)
print(f'{num_1} + {num_2} = {num_res}')
