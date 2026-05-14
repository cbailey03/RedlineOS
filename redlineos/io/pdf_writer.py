from pathlib import Path


class PdfWriter:
    """Writes annotations to PDF and saves the file."""

    def save(self, path: Path) -> None: ...
