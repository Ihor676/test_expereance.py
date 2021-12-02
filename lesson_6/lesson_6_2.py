# Для генерации случайных чисел используются функции модуля random
from random import randint
number_list = [randint(1, 10) for x in range(6)]
print(number_list)
k, c = [int(s) for s in input().split()]
number_list.append(0)
for i in range(len(number_list) - 1, k, -1):
    number_list[i] = number_list[i - 1]
number_list[k] = c
print(' '.join([str(i) for i in number_list]))
