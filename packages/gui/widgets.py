from PyQt5.QtWidgets import QApplication, QMainWindow, QLayout, QMdiArea, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QPushButton, QWidget, QMenu, QLabel
from PyQt5.QtCore import Qt, QSize, QThread, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QPixmap, QImage, QColor
from PIL import Image, ImageGrab, ImageQt, ImageFilter
from win32api import GetSystemMetrics
import cv2
import numpy as np
import matplotlib.pyplot as plt
# import pyqtgraph



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_wigdet = QMdiArea()
        self.setCentralWidget(self.central_wigdet)
        self.setMinimumSize(QSize(640, 480))  
        self.step = 20
        
        self.start_button = QPushButton(text="Start/Stop")
        self.start_button.setFixedSize(100,30)
        self.central_wigdet.addSubWindow(self.start_button)

        # Cross Button
        self.cross = ButtonCross()
        self.central_wigdet.addSubWindow(self.cross)
        self.cross.btn_right.clicked.connect(self.shift_right)
        self.cross.btn_left.clicked.connect(self.shift_left)
        self.cross.btn_up.clicked.connect(self.shift_up)
        self.cross.btn_down.clicked.connect(self.shift_down)
        self.cross.btn_center.clicked.connect(self.shift_center)

        self.screen = ScreenShot()
        self.central_wigdet.addSubWindow(self.screen)

        self.start_button.clicked.connect(self.shot_screenshot)
        self.start_button.clicked.connect(self.toggle_timer)
        # Timer start
        self.timer_enable = False
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.shot_screenshot)
        
        # Timer end
        self.layout = QVBoxLayout(self.central_wigdet)


    def toggle_timer(self):
        if self.timer_enable:
            self.timer_enable = False
            self.timer.stop()
        else: 
            self.timer_enable = True
            self.timer.start()

    # hier wir Qpixmap in die numpy arrray umgewandelt

    def shot_screenshot(self):
        self.screen.take_screenshot()

        image = self.screen.preview_screen.toImage()
        s = image.bits().asstring(400 * 400 * 4)
        arr = np.fromstring(s, dtype=np.uint8).reshape((400, 400, 4))
        arr2 = cv2.cvtColor(arr,cv2.COLOR_BGR2GRAY)
        ret,image = cv2.threshold(arr2,230,255,cv2.THRESH_BINARY)
        image2 = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
        qimg = QImage(image2, 400, 400, QImage.Format_RGB888)
        self.screen.preview_screen = QPixmap(qimg)
       
        self.screen.show_screenshot()


    def shift_right(self):
        self.screen.x = self.screen.x + self.step
        print("ScreenShot X = "+ str(self.screen.x))
    
    def shift_left(self):
        self.screen.x = self.screen.x - self.step
        print("ScreenShot X = "+ str(self.screen.x))

    def shift_up(self):
        self.screen.y = self.screen.y - self.step
        print("ScreenShot Y = "+ str(self.screen.y))

    def shift_down(self):
        self.screen.y = self.screen.y + self.step
        print("ScreenShot Y = "+ str(self.screen.y))
    
    def shift_center(self):
        self.screen.x = GetSystemMetrics(0)/2-200
        self.screen.y = GetSystemMetrics(1)/2-200

           
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
        
    def threshhold(self):
        img = np.array( )
        ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    