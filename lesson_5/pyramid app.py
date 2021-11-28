number = int(input("Ввести значение чисел от 3 до 9:"))
if (number < 10) and (number >= 3):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
else:
    print("Введенное вами число не в диапазоне")
