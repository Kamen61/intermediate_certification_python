from Descriptor import Descriptor


class Note:
    id = Descriptor()
    time = Descriptor()
    title = Descriptor()
    text = Descriptor()

    def __init__(self, id, time, title, text):
        self.id = id
        self.time = time
        self.title = title
        self.text = text

