from abc import ABC, abstractmethod
from .word_document.py import WordDocument
from .excel_document.py import ExcelDocument

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
