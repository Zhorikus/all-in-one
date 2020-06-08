import sys
import os

from PyQt5.QtWidgets import QApplication
from packages.gui.widgets import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    start_window = MainWindow()
    start_window.show()
    app.exit(app.exec_())
