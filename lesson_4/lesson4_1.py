x = input("Введите натуральное число:")
print("Да." if any(str(i)*2 in x for i in range(10)) else "Нет.")


