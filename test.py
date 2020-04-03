# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
#                             QGridLayout, QFileDialog)
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt, QTimer
# import sys


# class MainWindow(QWidget):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__()
#         self.preview_screen = QApplication.primaryScreen().grabWindow(0)
#         print(QApplication.screens())
#         self.settings()
#         self.create_widgets()
#         self.set_layout()

#     def settings(self):
#         self.resize(370, 270)
#         self.setWindowTitle("Screenshoter")
        
#     def create_widgets(self):
#         self.img_preview = QLabel()
#         self.img_preview.setPixmap(self.preview_screen.scaled(350,350,
#                                     Qt.KeepAspectRatio, Qt.SmoothTransformation))
#         self.btn_save_screenshot = QPushButton("Save screenshot")
#         self.btn_new_screenshot = QPushButton("New screenshot")

#         # signals connections
#         self.btn_save_screenshot.clicked.connect(self.save_screenshot)
#         self.btn_new_screenshot.clicked.connect(self.new_screenshot)

#     def set_layout(self):
#         self.layout = QGridLayout(self)
#         self.layout.addWidget(self.img_preview, 0, 0, alignment=Qt.AlignCenter)
#         self.layout.addWidget(self.btn_save_screenshot, 2,0, alignment=Qt.AlignLeft)
#         self.layout.addWidget(self.btn_new_screenshot, 2, 0, alignment=Qt.AlignRight)
#         self.setLayout(self.layout)



#     def take_screenshot(self):
#         self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),100,100,600,600)
#         self.img_preview.setPixmap(self.preview_screen.scaled(350,350,
#                                     Qt.KeepAspectRatio, Qt.SmoothTransformation))
#         self.show()


# root = QApplication(sys.argv)
# app = MainWindow()
# app.show()
# sys.exit(root.exec_())


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time

class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
    
        self.counter = 0
    
        layout = QVBoxLayout()
        
        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)
    
        layout.addWidget(self.l)
        layout.addWidget(b)
    
        w = QWidget()
        w.setLayout(layout)
    
        self.setCentralWidget(w)
    
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    
    def oh_no(self):
        time.sleep(5)

    def recurring_timer(self):
        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)
    
    
app = QApplication([])
window = MainWindow()
app.exec_()