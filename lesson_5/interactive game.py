# Сгенерировать случайное число
from random import random
number = round(random() * 100)  # Ввести счетчик попыток
i = 1
print('Компьютер загадал число.Отгадайте его.Число в диапазоне от 0 до 100')
import math
while i <= math.inf:  # Константа плавающей точки бесконечности.
    try:
        enter = int(input(str(i) + '-я попытка:'))
        if enter > number:
            print('много')
        elif enter < number:
            print('мало')
        else:
            print('Вы угадали с %d-й попытки' % i)
            break
    except ValueError:
        print('Ошибка вы ввели букву,а не число')
    i += 1
