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


tapeerror()
        