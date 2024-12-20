from .document import Document

class ExcelDocument(Document):
    def create(self):
        print("Excel document created.")

    def get_property(self):
        print("Row, column, cell")
