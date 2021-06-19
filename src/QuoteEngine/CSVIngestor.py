from typing import List
from .quote_engine import QuoteModel
from .ingestor_interface import IngestorInterface

import pandas


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest File")

        dogs_csv = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_dogs_list = QuoteModel(row['body'], row['author'])
            dogs_csv.append(new_dogs_list)

        return dogs_csv
