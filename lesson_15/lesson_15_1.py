file = open('readme.txt', 'w', encoding='utf-8')
print('Введите текст построчно.После ввода пустой строки будет сформирован '
      'файл readme.txt')
while True:
    s = input()
    if s == '':
        break
    file.write(s)
    file.write('\n')
file.close()
