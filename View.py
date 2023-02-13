class View:
    def print_all_notes(self, notes):
        if len(notes)!=0:
            print('Список всех заметок\n'
                  '----------------------------------------------------')
            for i in notes:
                print(f'id: {i["id"]}\n'
                      f'Дата добавления (редактирования): {i["time"]}\n'
                      f'Заголовок: {i["title"]}\n'
                      f'Текст: {i["text"]}\n'
                      '----------------------------------------------------')
        else:
            print('----------------------------------------------------\n'
                  'Список заметок пуст\n'
                  '----------------------------------------------------')

    def print_note(self, note):
        print('----------------------------------------------------\n'
              f'id: {note["id"]}\n'
              f'Дата добавления (редактирования): {note["time"]}\n'
              f'Заголовок: {note["title"]}\n'
              f'Текст: {note["text"]}\n'
              '----------------------------------------------------')

    def input_id(self):
        return int(input("Введите id заметки: "))

    def input_title_note(self):
        title = input("Введите заголовок заметки: ")
        return title

    def input_text_note(self):
        text = input("Введите текст заметки: ")
        return text

    def completed_add(self):
        print('Заметка добавлена\n'
              '----------------------------------------------------')

    def completed_rafact(self):
        print('----------------------------------------------------\n'
              'Заметка изменена\n'
              '----------------------------------------------------')

    def error_index(self):
        print('----------------------------------------------------\n'
              'Неверный индекс\n'
              '----------------------------------------------------')

    def completed_del_note(self):
        print('----------------------------------------------------\n'
              'Заметка удалена\n'
              '----------------------------------------------------')

    def completed_del_notes(self):
        print('----------------------------------------------------\n'
              'Все заметки удалены\n'
              '----------------------------------------------------')
