import math
def prime_numbers(interval):
    print("Простые числа от 1 до", interval)
    for i in range(2, interval + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
prime_numbers(100)
