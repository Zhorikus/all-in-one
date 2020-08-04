import os
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLayout, QMdiArea 
                             , QVBoxLayout, QHBoxLayout, QGridLayout, QWidget 
                             , QPushButton, QWidget, QMenu, QLabel, QAction
                             , QDockWidget)
from PyQt5.QtCore import Qt, QSize, QThread, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QPixmap, QImage, QColor
from PIL import Image, ImageGrab, ImageQt
from win32api import GetSystemMetrics
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph
from packages.gui.taschenrechner import PyCalcCtrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global mainwindow_instance
        mainwindow_instance = self
        self.layout_locked  = False
        self.central_widget = QWidget()
        self.central_widget.setFixedHeight(0)
        self.setDockOptions(QMainWindow.AllowTabbedDocks)
        self.setDockNestingEnabled(True)
        self.dock_object_names = set()
        self.setCentralWidget(self.central_widget)
        self._initUI()


        # dock = QDockWidget(parent=self,)
        # dock.setWidget(QWidget())
        # dock.setFeatures(dock.DockWidgetMovable | dock.DockWidgetClosable)



    def _initUI(self):
        #init menubar        
        self.calc = PyCalcCtrl()
        self.dockwidget = QDockWidget("Taschenrechner", self)
        self.dockwidget.setWidget(self.calc)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)

if __name__ == "__main__":
    app = QApplication([])
    start_window = MainWindow()
    start_window.show()
    app.exit(app.exec_())
