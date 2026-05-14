from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from redlineos.canvas.pdf_canvas import PdfCanvas
from redlineos.ui.panels.comments_panel import CommentsPanel
from redlineos.ui.ribbon.ribbon import Ribbon
from redlineos.ui.tool_panel import ToolPanel


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._ribbon = Ribbon(self)
        layout.addWidget(self._ribbon)

        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        self._canvas = PdfCanvas(self)
        content_layout.addWidget(self._canvas)

        self._panel = ToolPanel(self)
        content_layout.addWidget(self._panel)

        layout.addWidget(content)

        self._comments_panel = CommentsPanel()

        self._ribbon.open_requested.connect(self._canvas.load_document)
        self._ribbon.close_requested.connect(self._canvas.close_document)
        self._ribbon.zoom_in_requested.connect(self._canvas.zoom_in)
        self._ribbon.zoom_out_requested.connect(self._canvas.zoom_out)
        self._ribbon.fit_page_requested.connect(self._canvas.fit_page)
        self._ribbon.next_page_requested.connect(self._canvas.next_page)
        self._ribbon.previous_page_requested.connect(self._canvas.previous_page)
        self._ribbon.comment_panel_requested.connect(self._toggle_comments_panel)

    def _toggle_comments_panel(self) -> None:
        if self._panel.isVisible() and self._panel.current_widget is self._comments_panel:
            self._panel.close_panel()
        else:
            self._panel.open_panel("Comments", self._comments_panel)
