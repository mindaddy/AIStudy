from .document import Document

class WordDocument(Document):
    def create(self):
        print("Word document created.")

    def get_property(self):
        print("Font, size, color")
