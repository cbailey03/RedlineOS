from PySide6.QtWidgets import QVBoxLayout, QWidget

from redlineos.canvas.pdf_canvas import PdfCanvas


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.canvas = PdfCanvas(self)
        layout.addWidget(self.canvas)
