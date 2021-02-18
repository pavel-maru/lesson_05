
# Программа сложения двух чисел в любой системе счисления.

from collections import deque

print("\nКалькулятор позволяет суммировать числа в системах счисления от двоичной  до 36-ричной.\n")
BASE = int(input('Введите размерность системы счисления (от 2 до 36): '))
# DIGITS = ('0', '1', '2', '3', '4', '5','6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

# формируем набор символов (цифр)
DEC = 10
STEP = 10

if BASE <= DEC:
    DIGITS = [str(i) for i in range(BASE)]
else:
    DIGITS = [str(i) for i in range(DEC)]
    # print(type(DIGITS))
    DEC_SYM = ord('A')
    # print(FIRST_LETTER)
    # for i in range(FIRST_LETTER, FIRST_LETTER + BASE - 10):
    #     DIGITS.append(chr(i).upper())
    DIGITS.extend(chr(i) for i in range(DEC_SYM, DEC_SYM - DEC + BASE))

DIGITS = tuple(DIGITS)
# print(type(DIGITS), DIGITS)

# Выводим список цифп
print(f'\nПоследовательность цифр в данной размерности '
      f'\n(при вводе чисел используйте только эти символы):')
for i, digit in enumerate(DIGITS):
    print(digit, end='\t')
    if (i + 1) % STEP == 0:
        print()
# print(', '.join(DIGITS))

# for i, digit in enumerate(DIGITS):
#     print(digit, end='   ')
#     if (i + 1) % STEP == 0:
#         print()

num_res = deque()
# print(type(num_res))
overflow = 0

print()
num_1  = deque(input(f'\nВведите первое {BASE}-ричное число: ').upper())
num_2  = deque(input(f'\nВведите второе {BASE}-ричное число: ').upper())
# print(number_1, number_2)

# print(DIGITS.index(num_1[len(num_1) - 1]))

len_res = max(len(num_1), len(num_2)) + 1
# вычисление суммы
for i in range(len_res):
    # добываем последовательно цифры из введённых чисел
    if i < len(num_1):
        dig_1 = num_1[len(num_1) - 1 - i]
        # print(len(num_1) - 1 - i, dig_1)
    else:
        dig_1 = '0'
    if i < len(num_2):
        dig_2 = num_2[len(num_2) - 1 - i]
        # print(len(num_2) - 1 - i, dig_2)
    else:
        dig_2 = '0'
    # print(dig_1, dig_2)
    # определяем результирующую цифру по индексам
    index_ = DIGITS.index(dig_1) + DIGITS.index(dig_2) + overflow
    if index_ < BASE:
        num_res.appendleft(DIGITS[index_])
        # print(num_res)
        overflow = 0
    else:
        num_res.appendleft(DIGITS[index_ - BASE])
        # print(num_res)
        overflow = 1

# num_res.reverse()
# print(num_res)
# удаляем незначащий ноль в начале числа
num_res.popleft() if num_res[0] == '0' else num_res
# if num_res[0] == '0':
#     # del num_res[0]
#     num_res.popleft()
# del num_res[0] if num_res[0] == '0'
# print(num_res)

# преобразуем массивы чисел в строчный вид и выводим
# num_1 = ''.join(num_1)
# num_2 = ''.join(num_2)
# num_res = ''.join(num_res)
# print(f'{num_1} + {num_2} = {num_res}')
print()
print(''.join(num_1), '+', ''.join(num_2), '=', ''.join(num_res))
