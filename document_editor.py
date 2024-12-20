from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_property(self):
        pass

class WordDocument(Document):
    def create(self):
        print("Word document created.")

    def get_property(self):
        print("Font, size, color")

class ExcelDocument(Document):
    def create(self):
        print("Excel document created.")

    def get_property(self):
        print("Row, column, cell")

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self):
        pass

class WordDocumentFactory(DocumentFactory):
    def create_document(self):
        return WordDocument()

class ExcelDocumentFactory(DocumentFactory):
    def create_document(self):
        return ExcelDocument()

class DocumentEditor:
    def __init__(self, factory: DocumentFactory):
        self.factory = factory

    def new_document(self):
        return self.factory.create_document()

# Example usage:
word_factory = WordDocumentFactory()
editor = DocumentEditor(word_factory)
word_doc = editor.new_document()
word_doc.create()
word_doc.get_property()

excel_factory = ExcelDocumentFactory()
editor = DocumentEditor(excel_factory)
excel_doc = editor.new_document()
excel_doc.create()
excel_doc.get_property()