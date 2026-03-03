import logging
from pypdf import PdfReader

from .count_regex import count_regex
from ..model.count_result import CountResult

def count_regex_in_pdf(regex, pdf_file) -> CountResult:
    """
    Counts the occurrences of a regex pattern in a PDF file and returns a dictionary with the count and matches.
    """
    logger = logging.getLogger("pypdf")
    logger.setLevel(logging.ERROR)
    
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return count_regex(regex, text)
