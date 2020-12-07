# # import os
# # import time
# # from PyQt5.QtWidgets import (QApplication, QMainWindow, QLayout, QMdiArea 
# #                              , QVBoxLayout, QHBoxLayout, QGridLayout, QWidget 
# #                              , QPushButton, QWidget, QMenu, QLabel, QAction
# #                              , QDockWidget)
# # from PyQt5.QtCore import Qt, QSize, QThread, QTimer
# # from PyQt5.QtGui import QIcon, QPixmap, QPixmap, QImage, QColor
# # from PIL import Image, ImageGrab, ImageQt
# # from win32api import GetSystemMetrics
# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import pyqtgraph
# # from packages.gui.taschenrechner import PyCalcCtrl


# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         global mainwindow_instance
# #         mainwindow_instance = self
# #         self.layout_locked  = False
# #         self.central_widget = QWidget()
# #         self.central_widget.setFixedHeight(0)
# #         self.setDockOptions(QMainWindow.AllowTabbedDocks)
# #         self.setDockNestingEnabled(True)
# #         self.dock_object_names = set()
# #         self.setCentralWidget(self.central_widget)
# #         self._initUI()


# #         # dock = QDockWidget(parent=self,)
# #         # dock.setWidget(QWidget())
# #         # dock.setFeatures(dock.DockWidgetMovable | dock.DockWidgetClosable)



# #     def _initUI(self):
# #         #init menubar        
# #         self.calc = PyCalcCtrl()
# #         self.dockwidget = QDockWidget("Taschenrechner", self)
# #         self.dockwidget.setWidget(self.calc)
# #         self.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)

# # if __name__ == "__main__":
# #     app = QApplication([])
# #     start_window = MainWindow()
# #     start_window.show()
# #     app.exit(app.exec_())

# # print("C:\\Users\\zhorikus\\Downloads".rstrip("\\")+"\\")


# # import os

# # print(os.path.exists("C:\\Users\\zhorikus\\Downloads\\test1.txt"))


# # from pytube import YouTube
# # import inspect
# # try:
# #     x = YouTube("https://stackoverflow.com/questions/395735/how-to-check-whether-a-variable-is-a-class-or-not")
# # print(isinstance(x, YouTube))



# # from pytube import YouTube
# # y = YouTube("https://www.youtube.com/watch?v=HNvHppOnwVU")
# # for x in y.streams.all():
# #     print(x)

# # from pytube import YouTube
# # y = YouTube("https://www.youtube.com/watch?v=HNvHppOnwVU")
# # x = y.streams.filter(res="1080p", mime_type="video/mp4").first()
# # print(x)

# # quality = ["1080p", "720p","480p"]
# # for x in quality:
# #     print(x)

# # stream = y.streams.filter(only_audio=True, mime_type="audio/mp4").first().download()


# # for Firefox
# # import time
# # from selenium import webdriver
# # import geckodriver_autoinstaller
# # # geckodriver_autoinstaller.install()
# # driver = webdriver.Firefox("C:\\Users\\zhorikus\\Downloads\\geckodriver-v0.27.0-win64\\")
# # i = 100
# # while i> 0:
# #     print (driver.current_url)
# #     i -= 1
# #     time.sleep(2)



# # import time
# # from selenium import webdriver

# # driver = webdriver.Chrome('C:\\Users\\zhorikus\\Downloads\\chromedriver_win32\\chromedriver.exe')  # Optional argument, if not specified will search path.
# # driver.get('http://www.google.com/');
# # time.sleep(5) # Let the user actually see something!
# # search_box = driver.find_element_by_name('q')
# # search_box.send_keys('ChromeDriver')
# # search_box.submit()
# # time.sleep(5) # Let the user actually see something!
# # driver.quit()



# # from pywinauto import Application
# # app = Application(backend='uia')
# # app.connect(title_re=".*Chrome.*")
# # dlg = app.top_window()
# # url = dlg.child_window(title="Adreso ir paieškos juosta", control_type="Edit").get_value()
# # print(url)


# # from selenium import webdriver
# # import chromedriver_binary  # Adds chromedriver binary to path

# # driver = webdriver.Chrome()
# # driver.get("http://www.python.org")
# # assert "Python" in driver.title

# # f = open('C:\\Users\\zhorikus\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History', 'rb')
# # data = f.read()
# # f.close()
# # f = open('C:\\test\\test.db', 'w')
# # f.write(repr(data))
# # f.close()

# # import sqlite3
# # conn = sqlite3.connect('C:\\test\\test.db')

# # cur = conn.cursor()
# # # cur.execute("SELECT * FROM tasks")
# # examples = [(2, "def"), (3, "ghi"), (4, "jkl")]
# # cur.executemany("INSERT INTO samples VALUES (?, ?)", examples)
# # for row in cur.execute("SELECT * FROM samples"):
# #     print (row)

# # # rows = cur.fetchall()

# # for row in rows:
# #     print(row)

# # from os import rename
# # from os import listdir
# # from os.path import isfile, join
# # onlyfiles = [f for f in listdir("C:\\Musik\\") if isfile(join("C:\\Musik\\", f))]

# # for x in onlyfiles:
# #     y=x.replace(".mp4", ".mp3")
# #     rename("C:\\Musik\\" + x,"C:\\Musik\\" + y)

# # from pytube import YouTube, Playlist
# # import re
# # import time


# # # ytd=[]
# # url = "https://www.youtube.com/playlist?list=PLxhnpe8pN3TmcRZ8vVi2rdJRwQnw-s9ow"
# # url1 = "https://www.youtube.com/watch?v=yawbI_AyUoU"
# # play_list = Playlist(url)
# # play_list._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# # for i, url in enumerate(play_list):
# #     ytd = YouTube(url = url)
# #     # print(ytd[i].streams.first().default_filename[:-4])
# #     # print(type(url))




# # from pytube import YouTube, Playlist
# # import re
# # import time

# # url = "https://www.youtube.com/watch?v=yawbI_AyUoU"

# # for i in range(100):
# #     ytd = YouTube(url = url)
# #     print(i, " : ",ytd.streams.first().default_filename[:-4])



# # from pytube import YouTube, Playlist
# # import os
# # import time

# # url = "https://www.youtube.com/watch?v=fLexgOxsZu0"
# # i=1
# # q=0
# # max = 100
# # for i in range(max):
# #     print(i)
# #     try:
# #         ytd = YouTube(url)
# #     except Exception as e:
# #         q +=1
    
# # print(q/max*100)

    
# import sys
# from youtube_dl import YoutubeDL


# url = "https://www.youtube.com/watch?v=oiKj0Z_Xnjc"
# video_info = YoutubeDL().extract_info(url=url, download=False)
# filename = video_info["title"] + ".mp3"
# options = {
#     "format" : "bestaudio/best",
#     "keepvideo" : False,
#     "auttmpl" : filename,
#     "postprocessors" : [{
#         "key" : "FFmpegExtractAudio",
#         "preferredcodec" : "mp3",
#         "preferredquality" : "192",
#     }]
# }

# with YoutubeDL(options) as ytd:
#     ytd.download([video_info["webpage_url"]])


#
# 2 sek = 1 rep
# x sek = 15460 rep
#

# print((2*15460)/(60))
# min = 10
# print(60*min/2)

 
a="123456789"
print(a[ 0 : 3 ])
print(a[-3 : -1 ])