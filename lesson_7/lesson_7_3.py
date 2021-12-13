counter = {}
for word in input("Введите через пробел текст одной строкой:").split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
