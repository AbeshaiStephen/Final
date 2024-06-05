from abc import ABC,abstractmethod

class DocumentType(ABC):
    @abstractmethod
    def create_document(self):
        pass
    @abstractmethod
    def open_document(self):
        pass
    @abstractmethod
    def read_document(self):
        pass
    @abstractmethod
    def save_document(self):
        pass
class WordDocument(DocumentType):
    
    def create_document(self):
        print("Creating Word Document")
    def open_document(self):
        print("Opening Word Document")
    def read_document(self):
        print("Reading Word Document")
    def save_document(self):
        print("Saving Word Document")
class PDFDocument(DocumentType):
    
    def create_document(self):
        print("Creating PDF Document")
    def open_document(self):
        print("Opening PDF Document")
    def read_document(self):
        print("Reading PDF Document")

    def save_document(self):
        print("Saving PDF Document")
class ExcelDocument(DocumentType):
    
    def create_document(self):
        print("Creating Excel Document")
    def open_document(self):
        print("Opening Excel Document")
    def read_document(self):
        print("Reading Excel Document")
    def save_document(self):
        print("Saving Excel Document")

class DocumentFactory:
    def create_document(self,document_type):
        if document_type == "word":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        elif document_type == "excel":
            return ExcelDocument()
        else:
            return None
    def open_document(self,document_type):
        if document_type == "word":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        elif document_type == "excel":
            return ExcelDocument()
        else:
            return None
    def read_document(self,document_type):
        if document_type == "word":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        elif document_type == "excel":
            return ExcelDocument()
        else:
            return None
    def save_document(self,document_type):
        if document_type == "word":
            return WordDocument()
        elif document_type == "pdf":
            return PDFDocument()
        elif document_type == "excel":
            return ExcelDocument()
        else:
            return None

if __name__ == "__main__":
    doc_factory= DocumentFactory()
    word_document = doc_factory.create_document("word")
    word_document.create_document()
    word_document.open_document()
    word_document.read_document()
    word_document.save_document()
    pdf_document = doc_factory.create_document("pdf")
    pdf_document.create_document()
    pdf_document.open_document()
    pdf_document.read_document()
    pdf_document.save_document()
    excel_document = doc_factory.create_document("excel")
    excel_document.create_document()
    excel_document.open_document()
    excel_document.read_document()
    excel_document.save_document()