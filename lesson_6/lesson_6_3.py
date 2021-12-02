from random import randint
number_list1 = set([randint(1, 10) for x in range(6)])
number_list2 = set([randint(1, 10) for i in range(6)])
print(number_list1, number_list2)
number_list3 = (number_list1 & number_list2)
print(len(number_list3))
