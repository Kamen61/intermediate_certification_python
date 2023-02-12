import datetime
import json


class JsonModul:

    def __init__(self, json):
        self.json = json

    def add_note(self, obj_note):
        json_note = {'id': obj_note.id, 'time': obj_note.time, 'title': obj_note.title,
                     'text': obj_note.text}
        self.write_json(json_note)

    def write_json(self, note):
        try:
            notes = self.read_notes()
        except:
            notes = []
        notes.append(note)
        self.update_notes(notes)

    def read_notes(self):
        try:
            with open(self.json, 'r') as f:
                notes = sorted(json.load(f), key=lambda dictionary: dictionary['time'])
            # notes=sorted(notes,key=lambda dictionary: dictionary['time'])
            return notes
        except:
            return list()

    def del_note(self, id):
        notes, search_index = self.check_index(id)
        notes.pop(search_index)
        self.update_notes(notes)

    def edit_note(self, id, text, title):  # Возможно стоит перебрать именно объект класса Note
        notes, search_index = self.check_index(id)
        notes[search_index]['text'] = text
        notes[search_index]['title'] = title
        notes[search_index]['time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.update_notes(notes)

    def check_index(self, id):
        notes = self.read_notes()
        for i, j in enumerate(notes):
            if j['id'] == id:
                return notes, i
        raise Exception('Неверный ID')

    def last_index_note(self):
        notes = self.read_notes()
        return notes[len(notes) - 1]['id'] + 1 if len(notes) > 0 else 1

    def update_notes(self, notes_list):
        with open(self.json, 'w') as f:
            json.dump(notes_list, f, indent=2, ensure_ascii=False)

