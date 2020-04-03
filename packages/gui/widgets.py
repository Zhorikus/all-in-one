from PyQt5.QtWidgets import QApplication, QMainWindow, QLayout, QMdiArea, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QPushButton, QWidget, QMenu, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image, ImageGrab, ImageQt, ImageFilter
# import pyqtgraph



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_wigdet = QMdiArea()
        self.setCentralWidget(self.central_wigdet)
        self.setMinimumSize(QSize(640, 480))  
        
        self.ok_button = QPushButton(text="OK")
        self.ok_button.setFixedSize(100,30)
        self.central_wigdet.addSubWindow(self.ok_button)

        self.cross = ButtonCross()
        self.central_wigdet.addSubWindow(self.cross)
        self.cross.btn_right.clicked.connect(self.shift_right)
        self.cross.btn_left.clicked.connect(self.shift_left)
        self.cross.btn_up.clicked.connect(self.shift_up)
        self.cross.btn_down.clicked.connect(self.shift_down)

        self.screen = ScreenShot()
        self.central_wigdet.addSubWindow(self.screen)

        self.ok_button.clicked.connect(self.shot_screenshot)
        self.layout = QVBoxLayout(self.central_wigdet)

    def shot_screenshot(self):
        self.screen.take_screenshot()
        self.screen.show_screenshot()

    def shift_right(self):
        self.screen.x = self.screen.x + 5
        print("ScreenShot X = "+ str(self.screen.x))
    
    def shift_left(self):
        self.screen.x = self.screen.x - 5
        print("ScreenShot X = "+ str(self.screen.x))

    def shift_up(self):
        self.screen.y = self.screen.y - 5
        print("ScreenShot Y = "+ str(self.screen.y))

    def shift_down(self):
        self.screen.y = self.screen.y + 5
        print("ScreenShot Y = "+ str(self.screen.y))
           
class ScreenShot(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 500
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),self.x,self.y,400,400)
        self.img_preview = QLabel()
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.img_preview, 0, 0, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),self.x,self.y,400,400)
        print(self.preview_screen.size())
        self.img_preview.setPixmap(self.preview_screen)

    def show_screenshot(self):
        self.show()






class ButtonCross(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.btn_up = QPushButton("Up")
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.btn_down = QPushButton("Down")

        self.grid.addWidget(self.btn_up,0,1)
        self.grid.addWidget(self.btn_left,1,0)
        self.grid.addWidget(self.btn_right,1,2)
        self.grid.addWidget(self.btn_down,2,1)
        self.setLayout(self.grid)
