from pathlib import Path
import fitz


class PdfReader:
    def open(self, path: Path) -> fitz.Document:
        return fitz.open(str(path))
