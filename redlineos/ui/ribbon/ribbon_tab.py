from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QWidget

from redlineos.ui.ribbon.ribbon_group import RibbonGroup


class RibbonTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(4, 2, 4, 2)
        self._layout.setSpacing(0)
        self._layout.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

    def add_group(self, group: RibbonGroup) -> RibbonGroup:
        self._layout.addWidget(group)
        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.VLine)
        sep.setStyleSheet("color: #cccccc;")
        self._layout.addWidget(sep)
        return group
