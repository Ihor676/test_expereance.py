s = input("Введите 2 слова")
if s == "My Bag":
    s = s.split()
    l = len(s)
    print("Введено", l, "слова")
    print("Вывод:", str.title('My'[::-1]), str.title('Bag'[::-1]))
else:
    print("Ввести еще раз.")
