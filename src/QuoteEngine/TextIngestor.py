from typing import List

from ingestor_Interface import IngestorInterface
from quote_engine import QuoteModel


class TextIngestor(IngestorInterface):
    allowed_extensions = ['.txt']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file")

        dogs_txt = []

        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                final_text = line.split('-')
                final_dog_text = QuoteModel(final_text[0], final_text[1].strip('\n'))
                dogs_txt.append(final_dog_text)

        f.close()

        return dogs_txt
