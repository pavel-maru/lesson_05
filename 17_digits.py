
# Программа сложения двух семнадцатиричных чисел. 

from collections import deque

BASE = 17
DIGITS = ('0', '1', '2', '3', '4', '5','6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G')

# print(type(HEX_DIGITS), HEX_DIGITS)

num_res = deque()
# print(type(num_res))
overflow = 0

print('Программа суммирования двух семнадцатиричных чисел.')
num_1  = deque(input('Введите первое число в семнадцатиричном представлении (только цифры от 0 до G): ').upper())
num_2  = deque(input('Введите второе число в семнадцатиричном представлении (только цифры от 0 до G): ').upper())
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
