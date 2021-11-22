def number(i):
    tmp = int(i) ** 2
    return True if str(tmp)[-len(i):] == i else False
n = input('Введите N=')
for i in range(1, int(n) + 1):
    if number(str(i)):
        print(f'{i}*{i}={i * i}')





