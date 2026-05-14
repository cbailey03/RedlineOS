from PySide6.QtWidgets import QMainWindow
from redlineos.ui.main_window import MainWindow


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()
        self.setCentralWidget(self.main_window)
        self.setWindowTitle("RedlineOS")
        self.resize(1400, 900)
