import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading as th
import time

class MovieFrame(ttk.Frame):

    def __init__(self,parent=None, path=None):
        super().__init__(parent, padding=(0,0))
        self.lock = th.Lock()
        self.parent = parent
        self.path = path
        self.video = cv2.VideoCapture(self.path)
        self.video_thread = None
        self.playing = False
        self.create_video_button()

    def create_video_button(self):
        self.video_button = tk.Button(
            self,
            width = 100,
            height = 25,
            bg="#DDDDDD",
            relief="flat",
        )
        self.video_button.pack(expand=True,fill=tk.BOTH)

    #ビデオを再生
    def play(self):
        #動画データがない場合はエラーメッセージを表示
        if self.video == None or not self.video.isOpened():
            messagebox.showerror('エラー','動画データがありません')
            self.close()
            return

        self.playing = not self.playing
        self.startingTime = time.time()
        if self.playing:
            self.video_thread = th.Thread(target=self.video_frame_timer)
            self.video_thread.setDaemon(True)
            self.video_thread.start()            
        else:
            self.video_thread = None 

    def next_frame(self):
        self.lock.acquire()
        ret, self.frame = self.video.read()
        if not ret:
            self.close()
        else:
            rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            pil = Image.fromarray(rgb)
            x = self.video_button.winfo_width()/pil.width
            y = self.video_button.winfo_height()/pil.height
            ratio = x if x<y else y #三項演算子 xとyを比較して小さい方を代入
            pil = pil.resize((int(ratio*pil.width),int(ratio*pil.height)))
            image = ImageTk.PhotoImage(pil)
            self.video_button.config(image=image)
            self.video_button.image = image
        self.lock.release()

    def video_frame_timer(self):
        while self.playing:
            elapsedTime = (time.time() - self.startingTime)*1000
            playTime = self.video.get(cv2.CAP_PROP_POS_MSEC)
            # 経過時間が再生時間より短い場合はスリープ
            if elapsedTime < playTime:
                time.sleep((playTime-elapsedTime)/1000)
            # 経過時間が再生時間より長い場合は次のフレームを表示
            else:
                self.next_frame()

    def close(self):
        self.playing = False
        self.video.release()
        self.parent.isPlaingMovie = False
        self.destroy()
