from datetime import datetime

from Descriptor import Descriptor


class Note:
    time = Descriptor()
    title = Descriptor()
    text = Descriptor()

    def __init__(self, title, text):
        self.time = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.title = title
        self.text = text
