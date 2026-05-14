from pathlib import Path

import fitz
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import (
    QDragEnterEvent,
    QDropEvent,
    QPainter,
    QResizeEvent,
    QWheelEvent,
)
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QLabel

from redlineos.canvas.renderer import Renderer
from redlineos.io.pdf_reader import PdfReader

PAGE_GAP = 20


class PdfCanvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)

        self._renderer = Renderer()
        self._reader = PdfReader()
        self._document: fitz.Document | None = None
        self._zoom = 1.5
        self._page_items: list = []
        self._current_page: int = 0

        self.setAcceptDrops(True)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setBackgroundBrush(Qt.GlobalColor.darkGray)

        self._placeholder = QLabel("Drop a PDF here to open it", self)
        self._placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._placeholder.setStyleSheet(
            "color: #aaaaaa; font-size: 18px; background: transparent;"
        )
        self._placeholder.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self._placeholder.resize(self.size())

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._placeholder.resize(self.size())

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls() and any(
            url.toLocalFile().lower().endswith(".pdf")
            for url in event.mimeData().urls()
        ):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event) -> None:
        event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        for url in event.mimeData().urls():
            path = Path(url.toLocalFile())
            if path.suffix.lower() == ".pdf":
                self.load_document(path)
                break
        event.acceptProposedAction()

    def load_document(self, path: Path) -> None:
        if self._document is not None:
            self._document.close()
        self._document = self._reader.open(path)
        self._current_page = 0
        self._render_document()
        self._placeholder.hide()

    def close_document(self) -> None:
        if self._document is not None:
            self._document.close()
            self._document = None
        self._scene.clear()
        self._page_items = []
        self._current_page = 0
        self._placeholder.show()

    def _render_document(self) -> None:
        self._scene.clear()
        self._page_items = []
        y_offset = 0.0
        for i in range(len(self._document)):
            pixmap = self._renderer.render_page(self._document[i], self._zoom)
            item = self._scene.addPixmap(pixmap)
            item.setPos(0.0, y_offset)
            self._page_items.append(item)
            y_offset += pixmap.height() + PAGE_GAP
        self._scene.setSceneRect(QRectF(self._scene.itemsBoundingRect()))

    def zoom_in(self) -> None:
        self.scale(1.15, 1.15)

    def zoom_out(self) -> None:
        self.scale(1.0 / 1.15, 1.0 / 1.15)

    def fit_page(self) -> None:
        if self._page_items:
            self.fitInView(self._page_items[self._current_page], Qt.AspectRatioMode.KeepAspectRatio)

    def next_page(self) -> None:
        if self._page_items and self._current_page < len(self._page_items) - 1:
            self._current_page += 1
            self.centerOn(self._page_items[self._current_page])

    def previous_page(self) -> None:
        if self._page_items and self._current_page > 0:
            self._current_page -= 1
            self.centerOn(self._page_items[self._current_page])

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            factor = 1.15 if event.angleDelta().y() > 0 else 1.0 / 1.15
            self.scale(factor, factor)
        else:
            super().wheelEvent(event)
