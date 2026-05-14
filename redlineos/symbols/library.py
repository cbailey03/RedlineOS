from pathlib import Path


class SymbolLibrary:
    """Loads and manages CAD symbol collections from assets/symbols."""

    def __init__(self) -> None:
        self.symbols: dict = {}

    def load(self, path: Path) -> None: ...
