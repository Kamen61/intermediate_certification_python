from Note import Note


class Controller:
    def __init__(self, JsonModul, View):
        self.json = JsonModul
        self.view = View

    def menu(self):
        return self.view.comands()

    def bad_menu_index(self):
        self.view.index_menu()

    def create_note(self):
        self.json.add_note(Note(self.view.input_title_note(), self.view.input_text_note()))
        self.view.completed_add()

    def read_note(self):
        try:
            self.view.print_note(self.json.return_note(self.json.check_index(self.view.input_id())))
        except:
            self.view.error_index()

    def update_note(self):
        try:
            self.json.edit_note(self.json.check_index(self.view.input_id()), self.view.input_title_note(),
                                self.view.input_text_note())
            self.view.completed_rafact()
        except:
            self.view.error_index()

    def del_note(self):
        try:
            self.json.del_note((self.json.check_index(self.view.input_id())))
            self.view.completed_del_note()
        except:
            self.view.error_index()

    def del_all_notes(self):
        self.json.del_notes()
        self.view.completed_del_notes()

    def print_all_notes(self):
        self.view.print_all_notes(self.json.sort_notes(self.json.read_notes()))
