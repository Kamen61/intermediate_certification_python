import datetime
import json
from Note import Note


class JsonModul:

    def __init__(self, json):
        self.json = json

    def add_note(self, obj_note):
        notes, last_id = self.last_index_note()
        json_note = {'id': last_id, 'time': obj_note.time, 'title': obj_note.title,
                     'text': obj_note.text}
        self.write_json(json_note, notes)

    def write_json(self, note, notes):
        notes.append(note)
        self.update_notes(notes)

    def read_notes(self):
        try:
            with open(self.json, 'r') as f:
                notes = json.load(f)
            return notes
        except:
            return list()

    def sort_notes(self,notes):
        notes=sorted(notes, key=lambda dictionary: dictionary['time'])
        return notes

    def del_note(self, tuple_notes_and_id):
        notes, note_id = tuple_notes_and_id
        notes.pop(note_id)
        self.update_notes(notes)

    def del_notes(self):
        with open(self.json, 'w') as f:
            pass

    def edit_note(self, tuple_notes_and_id, text, title):
        notes, note_id = tuple_notes_and_id
        notes[note_id]['text'] = text
        notes[note_id]['title'] = title
        notes[note_id]['time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.update_notes(notes)

    def check_index(self, id):
        notes = self.read_notes()
        for i, j in enumerate(notes):
            if j['id'] == id:
                return notes, i
        raise Exception('Неверный ID')

    def last_index_note(self):
        notes = self.read_notes()
        return (notes, notes[len(notes) - 1]['id'] + 1) if len(notes) > 0 else (notes, 1)

    def update_notes(self, notes_list):
        with open(self.json, 'w') as f:
            json.dump(notes_list, f, indent=2, ensure_ascii=False)

    def return_note(self, tuple_notes_and_id):
        notes, note_id = tuple_notes_and_id
        return notes[note_id]
