import subprocess
from typing import List

from ingestor_Interface import IngestorInterface
from quote_engine import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['.csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot Ingest File")

        # Generating a subprocess call for pdftotext for conversion to text file.
        final_output = path + "\\output.txt"
        subprocess.run(["pdftotext", "-layout", path, final_output], stdout=subprocess.PIPE)

        dogs_pdf = []
        with open(final_output) as p:
            lines = p.readlines()
            for line in lines:
                final_pdf = line.split('-')
                final_dog_pdf = QuoteModel(final_pdf[0], final_pdf[1].strip('\n'))
                dogs_pdf.append(final_dog_pdf)

            p.close()

        return dogs_pdf
