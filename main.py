from distutils import cmd
from XUi import *
from PyQt5.QtCore import QThread,Qt,QPoint,QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QApplication
from tkinter import messagebox
import threading 
from pytube import YouTube
from pytube import Playlist
import sys
from tkinter import messagebox
from functools import lru_cache,cache
@cache
@lru_cache




class Window(QMainWindow,QThread):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Download_button.clicked.connect(self.thread)
        self.ui.Minimize_button.clicked.connect(self.showMinimized)
        self.ui.Exit_button.clicked.connect(self.close)
    def thread(self):
        t1=threading.Thread(target=self.Downloadvideo)
        t1.start()
    def mousePressEvent(self,event):
        self.oldPosition=event.globalPos()
    def mouseMoveEvent(self,event):
        delta=QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition=event.globalPos()
        
        
    def Downloadvideo(self):
        # playlist Download logic....................................
        url=self.ui.link_text.text()
        emp=""
        path=self.ui.Path_text.text()
        if "playlist" in self.ui.link_text.text() or "Playlist" in self.ui.link_text.text():
            if self.ui.Audio_button.isChecked()==True:
                if(url!=emp) and (path!=emp):
                    play=Playlist(url)
                    for i in play.videos:
                        self.ui.Download_button.setText("Downloading...")
                        st=i.streams.get_audio_only()
                        st.download(output_path=path)
                        self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            elif self.ui.Video_low_button.isChecked()==True:
                if(url!=emp) and (path!=emp):
                    play=Playlist(url)
                    for i in play.videos:
                        self.ui.Download_button.setText("Downloading...")
                        st=i.streams.get_lowest_resolution()
                        st.download(output_path=path)
                        self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            elif self.ui.Video_high_button.isChecked()==True:
                if(url!=emp) and (path!=emp):
                    play=Playlist(url)
                    for i in play.videos:
                        self.ui.Download_button.setText("Downloading...")
                        st=i.streams.get_highest_resolution()
                        st.download(output_path=path)
                        self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            else:
                messagebox.showwarning("ERROR","Check all the Details carefully...")
        # Single Video Download Logic............................
        else:        
            if self.ui.Video_low_button.isChecked() == True:
                if(url!=emp) and (path!=emp):
                    video=YouTube(url)
                    self.ui.Download_button.setText("Downloading...")
                    stream=video.streams.get_lowest_resolution()
                    stream.download(output_path=path)
                    self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            elif self.ui.Video_high_button.isChecked() == True:
                if(url!=emp) and (path!=emp):
                    video=YouTube(url)
                    self.ui.Download_button.setText("Downloading...")
                    stream=video.streams.get_highest_resolution()
                    stream.download(output_path=path)
                    self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            elif self.ui.Audio_button.isChecked() == True:
                if(url!=emp) and (path!=emp):
                    video=YouTube(url)
                    self.ui.Download_button.setText("Downloading...")
                    stream1=video.streams.get_audio_only()
                    stream1.download(output_path=path)
                    self.ui.Download_button.setText("Download")
                else:
                    messagebox.showwarning("ERROR","Check all the Details Carefully...")
            else:
                messagebox.showwarning("ERROR","Check all the Details Carefully...")
        
        
        
        
app = QApplication(sys.argv)
gui = Window()
gui.show()
sys.exit(app.exec_())