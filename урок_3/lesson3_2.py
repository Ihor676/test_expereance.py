print("Введите год")
year = int(input(""))
if (1900 < year) and (year < 1000000):
    print("введеный год отвечает условиям.")
else:
    print("Введеный год не отвечает условиям.")

if (year % 400 == 0):
   (year % 100 == 0)
   (year % 4 == 0)
   print(year, "Год високосный")
else:
    print(year, "Год не високосный")

