from typing import List

from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.ingestor_Interface import IngestorInterface
from QuoteEngine.quote_engine import QuoteModel


class Ingestor(IngestorInterface):
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        for ingestor in cls.importers:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
