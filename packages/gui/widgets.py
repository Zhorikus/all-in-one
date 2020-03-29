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

        self.screen = ScreenShot()
        self.central_wigdet.addSubWindow(self.screen)

        self.ok_button.clicked.connect(self.screen.take_screenshot)







        self.layout = QVBoxLayout(self.central_wigdet)

           
class ScreenShot(QWidget):
    def __init__(self):
        super().__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.settings()
        self.create_widgets()
        self.set_layout()

    def settings(self):
        self.resize(200, 200)
        self.setWindowTitle("Screenshoter")
        
    def create_widgets(self):
        self.img_preview = QLabel()
        # self.img_preview.setPixmap(self.preview_screen.scaled(600,60,Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.img_preview.setPixmap(self.preview_screen.scaled(self.width(),self.height(),Qt.IgnoreAspectRatio, Qt.SmoothTransformation))

    def set_layout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.img_preview, 0, 0, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)



    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),100,100,600,600)
        self.img_preview.setPixmap(self.preview_screen.scaled(self.width(),self.height(),
                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
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


