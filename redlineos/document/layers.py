class Layer:
    """A named, toggleable annotation layer."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.visible = True
        self.locked = False
        self.annotations: list = []
