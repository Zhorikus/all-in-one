import sys
import os
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout
                            , QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout
                            , QComboBox, QTextEdit, QCheckBox)
from pytube import YouTube
from pytube import Playlist
from mhmovie.code import *
import inspect
import re
import time
from moviepy.editor import *


class YoutubeDownloaderGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube Downloader')
        self.setGeometry(0,0,300,300)
        self.generalLayout = QVBoxLayout()
        # Create layout
        self._createURL()
        self._createDataType()
        self._createSaveFolder()
        self.setLayout(self.generalLayout)

    def _createURL(self):
        qhlayout = QGridLayout()
        self.url_text = QLineEdit(self)
        self.url_text.setText("Youtube URL")
        qhlayout.addWidget(self.url_text,1,0)
        self.check_button = QPushButton("Check")
        qhlayout.addWidget(self.check_button,1,1)
        self.generalLayout.addLayout(qhlayout)

    def _createDataType(self):
        qhlayout = QHBoxLayout()
        self.data_type = QComboBox(self)
        self.data_type.addItem("Video")
        self.data_type.addItem("Audio")
        qhlayout.addWidget(self.data_type)
        self.mp3_checkbox = QCheckBox("Audio als mp3")
        self.mp3_checkbox.setChecked(True)
        qhlayout.addWidget(self.mp3_checkbox)
        self.generalLayout.addLayout(qhlayout)

    def _createSaveFolder(self):
        qhlayout = QGridLayout()
        self.save_path = QLineEdit(self)
        self.save_path.setText("E:\\Musik\\")
        qhlayout.addWidget(self.save_path,0,0)
        self.start_button = QPushButton("Download")
        self.start_button.clicked.connect(lambda: self.start_prozess())
        qhlayout.addWidget(self.start_button,0,1)
        self.generalLayout.addLayout(qhlayout)

    def start_prozess(self):
        config = {
                "path"            : str(self.save_path.text().replace("\\","\\\\")).rstrip("\\") + "\\",
                "url"             : self.url_text.text(),
                "data_type"       : str(self.data_type.currentText()),
                "mp3_checkbox"    : self.mp3_checkbox.isChecked()
        }
        s_time = time.time()
        video = YoutubeDownloader(config)
        print("Zeit: ", round(time.time()-s_time,3), "sec.")
        del video

class YoutubeDownloader():
    def __init__(self, config: dict = {}, ):
        if "url" in config.keys():
            self.url = config["url"]
        if "path" in config.keys():
            self.save_path = config["path"]
        if "data_type" in config.keys():
            self.data_type = config["data_type"]
        if "mp3_checkbox" in config.keys():
            self.mp3_checked = config["mp3_checkbox"]

        self.default_audio_name = "audio"
        self.default_video_name = "video"
        self.data_name = ""
        self.video_quality = ["1080p" , "720p" , "480p"]


        if self.data_type =="Audio":
            print("Audio Datei/-en werden heruntergeladen")
            self.start_prozess_audio()
            print("Ich habe Fertitsch")
        elif self.data_type =="Video":
            print("Video Datei/-en werden heruntergeladen")
            self.start_prozess_video()
            print("Ich habe Fertitsch")
        else:
            print("Kein gültige Auswahl")

    def start_prozess_video(self):    
        if "watch" in self.url and "youtube" in self.url:
            self.create_youtube_object()
            if not self.file_exists():
                print(self.data_name)
                self.video_download()
            else:
                print(self.data_name, "--------- EXIST ---------")
        elif "playlist" in self.url and "youtube" in self.url:
            print("Es ist sogar eine Playliste...")
            play_list = self.create_youtube_playlist()
            for index, title in enumerate(play_list):
                self.create_youtube_object(title)
                
                if not self.file_exists():
                    print(index, " : " , self.data_name)
                    self.video_download()
                else:
                    print(index, " : " , self.data_name, "--------- EXIST ---------")
        else:
            print("ist kein Youtube URL")

    def start_prozess_audio(self):    
        if "watch" in self.url and "youtube" in self.url:
            self.create_youtube_object()
            if not self.file_exists():
                print(self.data_name)
                self.audio_download()
            else:
                print(self.data_name, "--------- EXIST ---------")
        elif "playlist" in self.url and "youtube" in self.url:
            print("Es ist sogar eine Playliste...")
            play_list = self.create_youtube_playlist()
            for index, title in enumerate(play_list):
                self.create_youtube_object(title)
                
                if not self.file_exists():
                    print(index, " : " , self.data_name)
                    self.audio_download()
                else:
                    print(index, " : " , self.data_name, "--------- EXIST ---------")
        else:
            print("ist kein Youtube URL")


    def create_youtube_object(self,url = None):
        self.counter = 1
        while True:
            try:
                if url is None:
                    self.ytd = YouTube(self.url)
                else:
                    self.ytd = YouTube(url)
                self.data_name = self.ytd.streams.first().default_filename[:-4]
                break
            except Exception as e:
                self.counter +=1
                print("Error by load url: {}" .format(e))
                print("URL: " + str(self.url))
                print("try it {} again...".format(self.counter))
                if self.counter > 5:
                    print("it could't be loaded")
                    self.ytd = ""
                    self.data_name = ""
                    break
                continue
    
    def create_youtube_playlist(self):
        play_list = Playlist(self.url)
        play_list._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        return play_list

    def check_quality(self):
        for x in self.ytd.streams.all():
            print(x)

    def video_download(self):
        # self.video = self.ytd.streams.filter(res="1080p", mime_type="video/mp4").first().download("video", skip_existing = False)
        if isinstance(self.ytd, YouTube):
            for res in self.video_quality:
                stream = self.ytd.streams.filter(res=res, mime_type="video/mp4").first()

                if stream is not None:
                    print("break with res = " + res)
                    break
            print("Video Qualität ist " + res)
            if stream is not None:
                self.video = stream.download(output_path = self.save_path, filename= self.default_video_name, skip_existing = False)
                self.audio_download()
                self.combine()

    def audio_download(self):
        # self.video = self.ytd.streams.filter(only_audio=True, mime_type="audio/mp4").first().download("audio", skip_existing = False)
        if isinstance(self.ytd, YouTube):
            stream = self.ytd.streams.filter(only_audio=True, mime_type="audio/mp4").first()
            if stream is not None:
                if self.data_type == "Audio":
                    self.audio = stream.download(output_path = self.save_path, filename= self.data_name, skip_existing = False)
                else:
                    self.audio = stream.download(output_path = self.save_path, filename= self.default_audio_name, skip_existing = False)
                if self.mp3_checked and self.data_type == "Audio":
                    self.mp4_to_mp3()

    def file_exists(self):
        if self.data_name is not None:
            path = self.save_path + self.data_name + ".mp4"
            return os.path.exists(path)
        else:
            return True

    def combine(self):
        import moviepy.editor as mpe
        my_clip = mpe.VideoFileClip(self.save_path + self.default_video_name + ".mp4")
        audio_background = mpe.AudioFileClip(self.save_path + self.default_audio_name + ".mp4")
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile(self.save_path + str(self.data_name) + ".mp4")
        os.remove(self.save_path + self.default_video_name + ".mp4")
        os.remove(self.save_path + self.default_audio_name + ".mp4")

    def mp4_to_mp3(self):
        os.rename(self.save_path + self.data_name + ".mp4",self.save_path + self.data_name + ".mp3")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader Class")
        self.setGeometry(300,300,400,150)
        self.y = YoutubeDownloaderGUI()
        self.setCentralWidget(self.y)


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exit(app.exec_())



