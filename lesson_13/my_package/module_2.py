"""
Модуль содержит функции
       f_login - свой простой класс исключений.
       compare1 - compare2 - работа декорированых функций вызвает функции с
                  одинаковыми последовательностями и одинковыми числами для
                  поиска, и сравнить какой метод работы в выигрше по првемени
       tapeerror - функция использует обрабатку исключений, которая
                   запрашивает ввод двух значений.Если хотя бы одно из них не
                   является числом, то должна выполняться конкатенация.
"""


class LoginError(Exception):
    msg = 'Неверный логин!'

    def __init__(self, value=None):
        if value is not None:
            self.msg = value

    def __str__(self):
        return self.msg


def f_login(login):
    pass_login = 'ihor.i147'
    try:
        if login != pass_login:
            raise LoginError('Неверный логин!')
    except LoginError as error:
        print(error.__str__())


# name = input('Введите логин(правильный логин ihor.i147):')
# f_login(name)

import random
import time


def benchmark(function):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        return_value = end-start
        # print('Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

#вызываем функции для сравнения linear_search_1 и linear_search_2


@benchmark
def linear_search_1(sequence1, look_for1):
    i = 0
    length1 = len(sequence1)
    while i < length1 and look_for1 != sequence1[i]:
        i += 1
    return i if i < length1 else None
#вызываем рандомный список для сравниния функций


random_spisok = [random.randint(1,1000000000)for i in range(1000000)]+[1000]
random_number = 1000
compare1 = linear_search_1(random_spisok, random_number)


@benchmark
def linear_search_2(sequence2, look_for2):
    k = 0
    sequence2.append(look_for2)
    lenght2 = len(sequence2)-1
    while look_for2 != sequence2[k]:
        k += 1
    return k if k < lenght2 else None


compare2 = linear_search_2(random_spisok, random_number)
# print(f"Первый линейный поиск занимает {compare1} , второй линейный поиск "
#       f"{compare2} секунд на " f"{compare1-compare2} секунд меньше")


def tapeerror():
    a = input('Введите 1 значение:')
    b = input('Введите 2 значение:')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        compound = ''.join(map(str, (a, b)))
        print('Соединение строк: ', compound)
    else:
        c = a + b
        print('Сумма чисел:', c)

# tapeerror()
