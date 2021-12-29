import random
while True:
    M = int(input('Введите целочисленое количество М(более 5) элементов '
                  'двухмерного списка МхМ:'))
    if M < 6:
        continue
    else:
        break
Matrix = [[random.randint(1, 100) for i in range(M)]for y in range(M)]
print('Матрица до сортировки')
def sort_matrix(Matrix_):
    sumy = [0 for i in range(M)]
    for y in range(len(Matrix)):
        sumy = [sumy[index] + i for index, i in enumerate(Matrix[y])]
    for i in range(len(sumy)-1):
        for j in range(len(sumy) - i - 1):
            if sumy[j] > sumy[j + 1]:
                sumy[j], sumy[j + 1] = sumy[j + 1], sumy[j]
                for y in range(len(Matrix)):
                    Matrix_[y][j], Matrix_[y][j + 1] = Matrix_[y][j + 1], \
                                                       Matrix_[y][j]
        for x in range(len(Matrix)):
            for i in range(len(Matrix) - 1):
                for j in range(len(Matrix) - i - 1):
                    if x % 2 != 0:
                        if Matrix_[j][x] > Matrix_[j + 1][x]:
                            Matrix_[j][x], Matrix_[j + 1][x] = Matrix_[j +
                                                                       1][x],\
                                                               Matrix_[j][x]
                    else:
                        if Matrix_[j][x] < Matrix_[j + 1][x]:
                            Matrix_[j][x], Matrix_[j + 1][x] = Matrix_[j +
                                                                       1][x],\
                                                               Matrix_[j][x]
    return Matrix_
def print_matrix(Matrix_):
    sumy = [0 for i in range(M)]
    for y in range(len(Matrix)):
        sumy = [sumy[index] + i for index, i in enumerate(Matrix[y])]
        for x in Matrix[y]:
            print('{:<5}'.format(x), end='')
        print('')
    for x in sumy:
        print('{:<5}'.format(x), end='')
    return None
print_matrix(Matrix)
print()
print('Матрица после сортировки')
Matrix = sort_matrix(Matrix)
print_matrix(Matrix)
