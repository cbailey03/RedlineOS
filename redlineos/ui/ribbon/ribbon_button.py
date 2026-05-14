from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QToolButton


class RibbonButton(QToolButton):
    LARGE = "large"
    SMALL = "small"

    def __init__(
        self,
        text: str,
        icon: QIcon | None = None,
        size: str = LARGE,
        parent=None,
    ):
        super().__init__(parent)
        self.setText(text)
        self.setAutoRaise(True)

        has_icon = icon is not None and not icon.isNull()
        if has_icon:
            self.setIcon(icon)

        if size == self.LARGE:
            self.setIconSize(QSize(32, 32))
            self.setToolButtonStyle(
                Qt.ToolButtonStyle.ToolButtonTextUnderIcon
                if has_icon
                else Qt.ToolButtonStyle.ToolButtonTextOnly
            )
            self.setMinimumSize(QSize(54, 62))
        else:
            self.setIconSize(QSize(16, 16))
            self.setToolButtonStyle(
                Qt.ToolButtonStyle.ToolButtonTextBesideIcon
                if has_icon
                else Qt.ToolButtonStyle.ToolButtonTextOnly
            )
            self.setFixedHeight(22)
            self.setMinimumWidth(60)
