import random


def matrix():
    """
    Функция генерирует матрицу со случайными числами, размеры матрици
    задается пользователем.Вычисляется сумма каждой строки и столбца
    """

    M = int(input('Введите целочисленое чило M:'))
    N = int(input('Введите целочисленое чило N:'))

    Matrix = [[random.randint(1, 50) for i in range(M)] for y in range(N)]
    sumy = [0 for k in range(M)]
    for y in range(len(Matrix)):
        sumx = 0
        sumy = [sumy[index] + i for index, i in enumerate(Matrix[y])]
        for x in Matrix[y]:
            print('{:<5}'.format(x), end='')
            sumx += x
        print('{:<5}'.format(sumx))
    for x in sumy:
        print('{:<5}'.format(x), end='')

if __name__ == "__main__":
    matrix()
