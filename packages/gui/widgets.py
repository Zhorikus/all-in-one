import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLayout, QMdiArea, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QPushButton, QWidget, QMenu, QLabel
from PyQt5.QtCore import Qt, QSize, QThread, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QPixmap, QImage, QColor
from PIL import Image, ImageGrab, ImageQt
from win32api import GetSystemMetrics
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_wigdet = QMdiArea()
        self.setCentralWidget(self.central_wigdet)
        self.setMinimumSize(QSize(640, 480))  
        self.step = 20
        
        #init Start Button
        self.init_start_button()

        #init Start Button
        self.init_cross_button()

        self.screen1 = ScreenShot()
        self.screen2 = ScreenShot()

        self.central_wigdet.addSubWindow(self.screen1)
        self.central_wigdet.addSubWindow(self.screen2)

        self.start_button.clicked.connect(self.toggle_timer)

        # Timer start
        self.timer_enable = False
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.shot_screenshot)
        # Timer end
        self.layout = QVBoxLayout(self.central_wigdet)

    def init_start_button(self):
        # Start Button
        self.start_button = QPushButton(text="Start/Stop")
        self.start_button.setFixedSize(100,30)
        self.central_wigdet.addSubWindow(self.start_button)

    def init_cross_button(self):
        # Cross Button
        self.cross = ButtonCross()
        self.central_wigdet.addSubWindow(self.cross)
        self.cross.btn_right.clicked.connect(self.shift_right)
        self.cross.btn_left.clicked.connect(self.shift_left)
        self.cross.btn_up.clicked.connect(self.shift_up)
        self.cross.btn_down.clicked.connect(self.shift_down)
        self.cross.btn_center.clicked.connect(self.shift_center)

    def toggle_timer(self):
        if self.timer_enable:
            self.timer_enable = False
            self.timer.stop()
        else: 
            self.timer_enable = True
            self.timer.start()

    # hier wir Qpixmap in die numpy arrray umgewandelt

    def shot_screenshot(self):
        self.screen1.take_screenshot()

        image = self.screen1.preview_screen.toImage()
        s = image.bits().asstring(400 * 400 * 4)
        arr = np.fromstring(s, dtype=np.uint8).reshape((400, 400, 4))
        arr2 = cv2.cvtColor(arr,cv2.COLOR_BGR2GRAY)
        ret,image = cv2.threshold(arr2,70,255,cv2.THRESH_BINARY)
        image = cv2.adaptiveThreshold(arr2,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
        image1 = cv2.adaptiveThreshold(arr2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        image2 = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
        image3 = cv2.cvtColor(image1,cv2.COLOR_GRAY2RGB)
        qimg = QImage(image2, 400, 400, QImage.Format_RGB888)
        qimg2 = QImage(image3, 400, 400, QImage.Format_RGB888)
        self.screen1.preview_screen = QPixmap(qimg)
        self.screen2.preview_screen = QPixmap(qimg2)
       
        self.screen1.show_screenshot()
        self.screen2.show_screenshot()


    def shift_right(self):
        self.screen1.x = self.screen1.x + self.step
        print("ScreenShot X = "+ str(self.screen1.x))
    
    def shift_left(self):
        self.screen1.x = self.screen1.x - self.step
        print("ScreenShot X = "+ str(self.screen1.x))

    def shift_up(self):
        self.screen1.y = self.screen1.y - self.step
        print("ScreenShot Y = "+ str(self.screen1.y))

    def shift_down(self):
        self.screen1.y = self.screen1.y + self.step
        print("ScreenShot Y = "+ str(self.screen1.y))
    
    def shift_center(self):
        self.screen1.x = GetSystemMetrics(0)/2-200
        self.screen1.y = GetSystemMetrics(1)/2-200

           
class ScreenShot(QWidget):
    def __init__(self):
        super().__init__()
        self.x = GetSystemMetrics(0)/2-200
        self.y = GetSystemMetrics(1)/2-200
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),self.x,self.y,400,400)
        self.img_preview = QLabel()
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.img_preview, 0, 0, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),self.x,self.y,400,400)
        
    def show_screenshot(self):
        self.img_preview.setPixmap(self.preview_screen)
        self.show()

class ButtonCross(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.btn_up = QPushButton("Up")
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.btn_down = QPushButton("Down")
        self.btn_center = QPushButton("Center")

        self.grid.addWidget(self.btn_up,0,1)
        self.grid.addWidget(self.btn_left,1,0)
        self.grid.addWidget(self.btn_right,1,2)
        self.grid.addWidget(self.btn_down,2,1)
        self.grid.addWidget(self.btn_center,1,1)
        self.setLayout(self.grid)


class ImageAlgorithms(ScreenShot):
    def __init__(self, preview_screen):
        super().__init__()
        
    def threshold(self):
        img = np.array( )
        ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    