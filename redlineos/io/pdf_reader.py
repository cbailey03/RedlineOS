from pathlib import Path


class PdfReader:
    """Opens a PDF and loads pages via PyMuPDF."""

    def open(self, path: Path) -> None: ...
