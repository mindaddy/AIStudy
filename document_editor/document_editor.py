from .document_factory import DocumentFactory, WordDocumentFactory, ExcelDocumentFactory

class DocumentEditor:
    def __init__(self, factory: DocumentFactory):
        self.factory = factory

    def new_document(self):
        return self.factory.create_document()

# Example usage:
if __name__ == "__main__":
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
