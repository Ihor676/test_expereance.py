import random
def function(a, x):
    o = 1
    for i in range(0, len(a)):
        for j in range(o, len(a)):
            if a[i] + a[j] == x:
                return True
        o += 1
    return False
my_scroll = [random.randint(1, 15) for k in range(10)]
print(my_scroll)
my_spisok = random.randint(1, 10)
print(my_spisok)
print(function(my_scroll, my_spisok))
