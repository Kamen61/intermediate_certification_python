class View:
    def print_all_notes(self, notes):
        print('Список всех заметок\n'
              '----------------------------------------------------')
        for i in notes:
            print(f'id: {notes["id"]}\n'
                  f'date: {notes["date"]}\n'
                  f'title: {notes["title"]}\n'
                  f'text: {notes["text"]}\n')
            print('----------------------------------------------------')

    def input_id(self):
        return int(input("Введите id заметки: "))

    def input_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        return title, text

    def completed_add(self):
        print('----------------------------------------------------\n'
              'Заметка добавлена\n'
              '----------------------------------------------------')

    def completed_rafact(self):
        print('----------------------------------------------------\n'
              'Заметка изменена\n'
              '----------------------------------------------------')

    def error_index(self):
        print('----------------------------------------------------\n'
              'Неверный индекс\n'
              '----------------------------------------------------')

    def del_note(self):
        print('----------------------------------------------------\n'
              'Заметка удалена\n'
              '----------------------------------------------------')

    def del_notes(self):
        print('----------------------------------------------------\n'
              'Все заметки удалены\n'
              '----------------------------------------------------')