menu = """
Нажмите(1) - Добавить контакт
Нажмите(2) - Удалить запись
Нажмите(3) - Поиск
Нажмите(4) - Сортировка
Нажмите(5) - Выход
"""


class NoteBook:
    def menu(self):
        """ Метод позволяющий обрабатывать метод экранного меню """
        print(f"\n Записная книжка\n Меню:{menu}")
        try:
            with open('notebook.txt', 'r', encoding='utf-8') as d:
                a = d.readlines()
            if len(a) == 0:
                print('Пока нет загруженных записей')
            else:
                if len(a) % 10 == 1:
                    print(f"загруженно: {len(a)} запись")
                else:
                    print(f"загруженно: {len(a)} записей")
        except FileNotFoundError:
            print("Файла notebook.txt нет, нужно его создать с помощью "
                  "первого пункта меню")
        while True:
            try:
                command = int(input("Введите номер пункта меню"))
                if command == 1:
                    self.add_person()
                elif command == 2:
                    self.delete()
                elif command == 3:
                    self.search_person()
                elif command == 4:
                    self.sort_lst()
                elif command == 5:
                    self.exit()
                else:
                    print("Такого пункта в меню нет")
                    continue
                break
            except ValueError:
                print("Вы ввели не правильно")
                continue

    @staticmethod
    def _list(list_notes):
        # преобразуем в список со списками
        list_lst_notes = []
        for i in list_notes:
            list_lst_notes.append(i.split(','))
        # убираем лишние символы
        signs = ["'", '{', '}', ':', ',', '\n']
        for i in range(len(list_lst_notes)):
            for j in range(len(list_lst_notes[i])):
                for e in range(len(list_lst_notes[i][j])):
                    for s in range(len(signs)):
                        if list_lst_notes[i][j][e] == signs[s]:
                            list_lst_notes[i][j] = list_lst_notes[i][
                                j].replace(signs[s], ' ')
        # создаем список со списками из списков
        for i in range(len(list_lst_notes)):
            for j in range(len(list_lst_notes[i])):
                list_lst_notes[i][j] = list_lst_notes[i][j].split()
        # преобразуем элементы(списки со списками) списка в словари
        # получаем список из словарей
        list_dict_notes = []
        for i in range(len(list_lst_notes)):
            note_dict = {list_lst_notes[i][j][0]: list_lst_notes[i][j][-1]
                         for j in range(len(list_lst_notes[i]))}
            list_dict_notes.append(note_dict)
        return list_dict_notes

    def add_person(self):
        """ Добавляет данные человека """
        print("Добавляем запись\nПоля помеченные * обязательны к заполнению\n")
        while True:
            name = input("*Введите Имя: ")
            if name == "":
                print("Это поле не может быть пустым")
                continue
            else:
                break
        while True:
            surname = input("*Введите Фамилию: ")
            if surname == "":
                print("то поле не может быть пустым")
                continue
            else:
                break
        while True:
            number = input("*Введите номер телефона ")
            if number == "":
                print("то поле не может быть пустым ")
                continue
            else:
                break
        address = input("Введите Адрес: ")
        if address == "":
            address = "None"

        birthday = input("Введите Дату Рождения: ")
        if birthday == "":
            birthday = "None"

        my_note = {
           "Имя": name,
           "Фамилия": surname,
           "Номер телефона": number,
           "Адрес": address,
           "Дата Рождения": birthday}

        with open("notebook.txt", "a", encoding='utf-8') as f:
            f.write(f"{str(my_note)}\n")
        print("Запись сохранена")
        self.menu()

    def delete(self):
        """ Метод удаляет запись по номеру в списке """
        while True:
            with open("notebook.txt", 'r', encoding='utf-8') as f:
                file_notes = f.read()
            if file_notes == "":
                print('Нет записей')
            else:
                with open('notebook.txt', 'r', encoding='utf-8') as f:
                    print("Записи:")
                    count = 0
                    notes_lst = []
                    for line in f:
                        print(f"{count}:\n{line}")
                        notes_lst.append(line)
                        count += 1

                while True:
                    try:
                        num_del = input("Введите номер для удаления")
                        num_del = int(num_del)
                        notes_lst.remove(notes_lst[num_del])

                        with open("notebook.txt", 'w', encoding='utf-8') as f:
                            for i in notes_lst:
                                f.write(i)
                        print("Запись удалена")
                        break
                    except (ValueError, IndexError):
                        print("Такого номера записи нет")
                        break
                    self.menu()

    def search_person(self):
        """ Метод ищет по имени и по номеру телефона """
        while True:
            command = """
            Нажмите(1) Поиск по имени
            Нажмите(2) Поиск по телефону
                        """
            print(command)
            with open("notebook.txt", 'r+', encoding="utf-8") as f:
                list_n = self._list(f.readlines())
            while True:
                try:
                    num = int(input("Введите число: "))
                    if num == 1:
                        print("Поиск по имени")
                        name = input("Введите имя: ")
                        list_f = []
                        for i in range(len(list_n)):
                            if name == list_n[i]["Имя"]:
                                list_f.append(list_n[i])
                        if len(list_f) > 0:
                            print("записи: ")
                            for i in list_f:
                                print(i)
                        else:
                            print("Ничего не найдено")
                        break
                    elif num == 2:
                        print("Поиск по номеру телефона")
                        number = input("Введите номер ""телефона: ")
                        list_f = []
                        for i in range(len(list_n)):
                            if number == list_n[i]["Номер телефона"]:
                                list_f.append(list_n[i])
                        if len(list_f) > 0:
                            print("Записи: ")
                            for i in list_f:
                                print(i)
                        else:
                            print("Ничего не найдено")
                        break
                    else:
                        print("Такого поиска нет")
                        continue
                except ValueError:
                    print("Вы ввели не число")
                    continue
            self.menu()

    def sort_lst(self):
        """ Метод сортирует по имени и по фамилии """
        while True:
            command = """
        Нажмите(1) - Сортировка по имени
        Нажмите(2) - Сортировка по фамилии
                    """
            print(command)
            with open("notebook.txt", 'r+', encoding="utf-8") as f:
                list_of_dict_notes = self._list(f.readlines())
            with open("notebook.txt", 'r', encoding='utf-8') as f:
                if f.read() == '':
                    print("Нет записей")
                else:
                    while True:
                        try:
                            sort_by = int(input("Введите число:"))
                            if sort_by == 1:
                                sorted_list_of_dict = sorted(
                                    list_of_dict_notes, key=lambda k: k['Имя'])
                                with open('notebook.txt', 'w',
                                          encoding='utf-8') \
                                        as f1:
                                    for i in sorted_list_of_dict:
                                        f1.write(f'{str(i)}\n')
                                    print("Отсортировано по имени")
                                    break
                            elif sort_by == 2:
                                sorted_list_of_dict = sorted(list_of_dict_notes,
                                                             key=lambda k:
                                                             k['Фамилия'])
                                with open('notebook.txt', 'w',
                                          encoding='utf-8') \
                                        as f2:
                                    for i in sorted_list_of_dict:
                                        f2.write(f'{str(i)}\n')
                                    print("Отсортировано по фамилии")
                                    break
                            else:
                                print("Такой сортировки нет")
                                continue
                        except ValueError:
                            print("Вы ввели не число ")
                            continue
            break
        self.menu()

    @staticmethod
    def exit():
        """Метод закрывает программу"""
        print("Выход из книжки")
        exit()


if __name__ == "__main__":
    my_notebook = NoteBook()
    my_notebook.menu()
