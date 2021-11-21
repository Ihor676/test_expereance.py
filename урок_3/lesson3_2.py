print("Введите год")
year = int(input(""))
if   (year<=1900):
     print("Введеный год не отвечает условиям.")
elif (year>=1000000):
     print("Введеный год не отвечает условиям.")
elif (year % 400 == 0) and (year % 100 == 0) and (year % 4 == 0):
     print(year, "Год высокосный")
else:
     print(year, "Год не высокосный")















