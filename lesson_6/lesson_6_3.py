# Для генерации случайных чисел используются функции модуля random
from random import randint
# это встроенный тип, предлагающий широкий набор возможностей, которые повторяют теорию множеств из математики.
number_list1 = set([randint(1, 10) for x in range(6)])
number_list2 = set([randint(1, 10) for i in range(6)])
print(number_list1, number_list2)
number_list3 = (number_list1 & number_list2)
# возвращает длину (количество элементов) в объекте
print(len(number_list3))
