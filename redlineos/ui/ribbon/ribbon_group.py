from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class RibbonGroup(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(6, 4, 6, 2)
        outer.setSpacing(2)

        self._button_row = QHBoxLayout()
        self._button_row.setContentsMargins(0, 0, 0, 0)
        self._button_row.setSpacing(2)
        self._button_row.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        outer.addLayout(self._button_row, stretch=1)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setMaximumHeight(1)
        sep.setStyleSheet("background: #cccccc; border: none;")
        outer.addWidget(sep)

        label = QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 8pt; color: #555555;")
        outer.addWidget(label)

    def add_button(self, button) -> None:
        self._button_row.addWidget(button)

    def add_small_column(self, *buttons) -> None:
        """Stack small buttons vertically as a single column within the group."""
        col = QVBoxLayout()
        col.setContentsMargins(0, 0, 0, 0)
        col.setSpacing(1)
        for btn in buttons:
            col.addWidget(btn)
        col.addStretch()
        self._button_row.addLayout(col)
