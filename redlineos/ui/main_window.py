from PySide6.QtWidgets import QVBoxLayout, QWidget

from redlineos.canvas.pdf_canvas import PdfCanvas
from redlineos.ui.ribbon.ribbon import Ribbon


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._ribbon = Ribbon(self)
        layout.addWidget(self._ribbon)

        self._canvas = PdfCanvas(self)
        layout.addWidget(self._canvas)

        self._ribbon.open_requested.connect(self._canvas.load_document)
        self._ribbon.close_requested.connect(self._canvas.close_document)
        self._ribbon.zoom_in_requested.connect(self._canvas.zoom_in)
        self._ribbon.zoom_out_requested.connect(self._canvas.zoom_out)
        self._ribbon.fit_page_requested.connect(self._canvas.fit_page)
        self._ribbon.next_page_requested.connect(self._canvas.next_page)
        self._ribbon.previous_page_requested.connect(self._canvas.previous_page)
