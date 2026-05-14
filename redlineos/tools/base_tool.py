from abc import ABC, abstractmethod
from PySide6.QtCore import QEvent


class BaseTool(ABC):
    """All drawing/annotation tools inherit from this."""

    @abstractmethod
    def on_press(self, event: QEvent) -> None: ...

    @abstractmethod
    def on_move(self, event: QEvent) -> None: ...

    @abstractmethod
    def on_release(self, event: QEvent) -> None: ...
