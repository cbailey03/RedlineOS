from PySide6.QtWidgets import QMainWindow

from redlineos.ui.main_window import MainWindow


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(MainWindow(self))
        self.setWindowTitle("RedlineOS")
        self.resize(1400, 900)
