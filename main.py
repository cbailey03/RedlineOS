import sys
import fitz
from PySide6.QtWidgets import QApplication
from redlineos.app import Application

# MuPDF logs non-fatal structural warnings (e.g. malformed accessibility trees)
# to stderr. Suppress display and let callers inspect via fitz.TOOLS.mupdf_warnings().
fitz.TOOLS.mupdf_display_errors(False)


def main():
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
