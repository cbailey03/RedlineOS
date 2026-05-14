from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ToolPanel(QWidget):
    closed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(280)
        self.setStyleSheet("border-left: 1px solid #cccccc;")
        self.hide()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header = QWidget()
        header.setFixedHeight(32)
        header.setStyleSheet("background-color: #2c5f8a; border-left: none;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(10, 0, 6, 0)
        header_layout.setSpacing(0)

        self._title_label = QLabel()
        self._title_label.setStyleSheet("color: white; font-size: 9pt; font-weight: bold; border: none;")
        header_layout.addWidget(self._title_label)
        header_layout.addStretch()

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(22, 22)
        close_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: rgba(255, 255, 255, 0.75);
                border: none;
                font-size: 10pt;
            }
            QPushButton:hover { color: white; }
        """)
        close_btn.clicked.connect(self.close_panel)
        header_layout.addWidget(close_btn)
        layout.addWidget(header)

        self._content_area = QWidget()
        self._content_area.setStyleSheet("background-color: #f8f8f8; border: none;")
        self._content_layout = QVBoxLayout(self._content_area)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(0)
        layout.addWidget(self._content_area)

        self._current_widget: QWidget | None = None

    @property
    def current_widget(self) -> "QWidget | None":
        return self._current_widget

    def open_panel(self, title: str, widget: QWidget) -> None:
        self._title_label.setText(title)
        if self._current_widget is widget:
            self.show()
            return
        if self._current_widget is not None:
            self._content_layout.removeWidget(self._current_widget)
            self._current_widget.hide()
        self._current_widget = widget
        self._content_layout.addWidget(widget)
        widget.show()
        self.show()

    def close_panel(self) -> None:
        self.hide()
        self.closed.emit()
