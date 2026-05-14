import fitz
from PySide6.QtGui import QImage, QPixmap


class Renderer:
    def render_page(self, page: fitz.Page, zoom: float = 1.5) -> QPixmap:
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(img)
