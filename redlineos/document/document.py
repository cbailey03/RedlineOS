from pathlib import Path


class Document:
    """Represents an open PDF document and its annotation state."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.pages: list = []
        self.layers: list = []
