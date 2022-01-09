from my_package import module_1


print("Функция должна проверить есть ли в списке 2 числа сума которых "
      "еквивалентна числу переданому 2 м параметром.")
print(module_1.my_scroll1)
print(module_1.my_spisok1)
print(module_1.function1(module_1.my_scroll1, module_1.my_spisok1))

print('Написать анонимную функцию которая приниммает 2 значения x,y  где y по'
   'умолчанию == числу . Результат работы функции - число x  в степени y.')
print(module_1.my_spisok)
print(module_1.my_function)

print('создать функцию генератор ПРОСТЫХ чисел в дипазоне заданых 2-мя '
      'аргументами чисел.')
module_1.prime_numbers(100)
#print(help(module_1))
