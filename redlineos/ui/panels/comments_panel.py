from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QScrollArea,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class CommentsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Scrollable comment list
        self._list_container = QWidget()
        self._list_layout = QVBoxLayout(self._list_container)
        self._list_layout.setContentsMargins(8, 8, 8, 8)
        self._list_layout.setSpacing(6)
        self._list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._empty_label = QLabel("No comments yet.")
        self._empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._empty_label.setStyleSheet("color: #999999; font-size: 9pt; border: none;")
        self._list_layout.addWidget(self._empty_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        scroll.setWidget(self._list_container)
        layout.addWidget(scroll)

        # Add comment input area
        add_area = QWidget()
        add_area.setStyleSheet("background: white; border-top: 1px solid #dddddd;")
        add_layout = QVBoxLayout(add_area)
        add_layout.setContentsMargins(8, 8, 8, 8)
        add_layout.setSpacing(6)

        self._input = QTextEdit()
        self._input.setPlaceholderText("Add a comment…")
        self._input.setFixedHeight(72)
        self._input.setStyleSheet(
            "border: 1px solid #cccccc; border-radius: 3px; font-size: 9pt; background: white;"
        )
        add_layout.addWidget(self._input)

        add_btn = QPushButton("Add Comment")
        add_btn.setStyleSheet("""
            QPushButton {
                background: #2c5f8a;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px;
                font-size: 9pt;
            }
            QPushButton:hover { background: #3a7ab8; }
            QPushButton:pressed { background: #1e4a6e; }
        """)
        add_btn.clicked.connect(self._add_comment)
        add_layout.addWidget(add_btn)
        layout.addWidget(add_area)

    def _add_comment(self) -> None:
        text = self._input.toPlainText().strip()
        if not text:
            return
        self._empty_label.hide()
        self._list_layout.addWidget(self._make_card(text))
        self._input.clear()

    def _make_card(self, text: str) -> QWidget:
        card = QWidget()
        card.setStyleSheet(
            "QWidget { background: white; border: 1px solid #dddddd; border-radius: 4px; }"
        )
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(8, 6, 8, 6)

        label = QLabel(text)
        label.setWordWrap(True)
        label.setStyleSheet("font-size: 9pt; color: #1a1a1a; border: none;")
        card_layout.addWidget(label)
        return card
