# Для генерации случайных чисел используются функции модуля random
from random import randint
number_list = [randint(1, 10) for x in range(6)]
print(number_list)
k = int(input("Введите числовой индекс k:"))
for i in range(k + 1, len(number_list)):
    number_list[i - 1] = number_list[i]
# Метод pop() удаляет и возвращает последний object или obj из списка.
number_list.pop()
number_list = [print(number_list[i], end=' ')for i in range(len(number_list))]
