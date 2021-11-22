x = list(input("Введите натуральное число:"))
print('Да' if len(set(x)) != len(x) else 'Нет')
