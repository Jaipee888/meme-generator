from typing import List

from docx import Document

from ingestor_Interface import IngestorInterface
from quote_engine import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['.docx']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest File")

        dog_docx = []
        docx = Document(path)
        for para in docx.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                dog_text = QuoteModel(parse[0], parse[1])
                dog_docx.append(dog_text)

        return dog_docx
