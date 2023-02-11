import json


class JsonModul:

    def __init__(self, json):
        self.json = json

    def add_note(self):
        pass


    def write_json(self, note):
        try:
            notes = self.read_notes()
        except:
            notes = []
        notes.append(note)
        with open(self.json,'w') as f:
            json.dump(notes,f,indent=2,ensure_ascii=False)

    def read_notes(self):
        with open(self.json, 'r') as f:
            notes = json.load(f)
        return notes

    def del_note(self,index):
        notes=self.read_notes()
        if self.check_index(index,len(notes)):
            return notes.pop(index-1)
        raise Exception("Неверный индекс")


    def edit_note(self,index):
        pass

    def check_index(self,index,len):
        return len<index<=len



m = JsonModul('notes.json')
a={'id': 12, 'date': '12.12.12' ,'title': '12', 'text': '12'}
# a = [1, 2, 3, 4, 5, 8]
m.write_json(a)
print(m.read_notes())
