import sys
from PySide6.QtWidgets import QApplication
from redlineos.app import Application


def main():
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
