import random
import math


def function1(a, x):
    o = 1
    for i in range(0, len(a)):
        for j in range(o, len(a)):
            if a[i] + a[j] == x:
                return True
        o += 1
    return False


my_scroll1 = [random.randint(1, 15) for k in range(10)]
# print(my_scroll1)
my_spisok1 = random.randint(1, 10)
# print(my_spisok1)
# print(function1(my_scroll1, my_spisok1))


# генерируем список
my_spisok = [random.randint(1, 15)for i in range(8)]
# print(my_spisok)
# результат применения лямды функции к каждому числу
my_function = list(map(lambda x, y=3: x**y, my_spisok))
# print(my_function)


def prime_numbers(interval):
    print("Простые числа от 1 до", interval)
    for i in range(2, interval + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
