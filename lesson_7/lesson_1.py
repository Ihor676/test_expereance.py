def sieve(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)


# Тесты
print(sieve([1, 2, 3, 3, 2]))
print(sieve([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
print(sieve((1, 2, 3, 4, 5, 6, 7)))