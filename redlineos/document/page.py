class Page:
    """Represents a single PDF page and the annotations on it."""

    def __init__(self, index: int) -> None:
        self.index = index
        self.annotations: list = []
