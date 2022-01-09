from sort_module import *
import sort_module


list = [52, 155, 26, 3, 2, 88, 45, 22, 11, 104, 0, 1]

print('До сортировки', list)
print('После сортировки методом пузырька:', sort_module.bubble_sort(list))
print('После сортировки методом камня:', sort_module.sort_stone_method(list))
print('После сортировки методом вставки:', sort_module.insert_sort_method(list))
