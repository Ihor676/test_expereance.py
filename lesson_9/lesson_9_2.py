import random
# генерируем список
my_spisok = [random.randint(1, 15)for i in range(8)]
print(my_spisok)
# результат применения лямды функции к каждому числу
my_function = list(map(lambda x, y=3: x**y, my_spisok))
print(my_function)
