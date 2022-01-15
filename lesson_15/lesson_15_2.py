file = open('article.txt', mode='r', encoding='utf-8')
a = file.read()
b = a.split()
print(b)


def longest_words(file):
    """
    longest_words(file), которая выводит слово, имеющее максимальную длину
    (или список слов, если таковых несколько).
    """
    c = ''
    for i in b:
        if len(i) > len(c):
            c = i
    print('Dыводит слово, имеющее максимальную длину:---', c)


if __name__ == '__main__':
    longest_words(b)
    file.close()
