import tkinter as tk
from tkinter import ttk
from tkinter import font
import pygame

class FilePathFrame(ttk.Frame):
    def __init__(self, controller=None, parentClass=None, parentFrame=None, key=None, index=None):
        super().__init__(parentFrame)

        self.controller = controller
        self.parentClass = parentClass
        self.parentFrame = parentFrame
        self.key = key
        self.index = index
        self.initVolume = 50.0
        self.volume = "50.0"

        self.isMovie = self.is_movie()

        #containerFrameを作成
        self.containerFrame = ttk.Frame(self)
        #containerFrameを表示
        self.containerFrame.pack(expand=True, fill=tk.X, side=tk.TOP)

        #isMovieがFalseのとき
        if not self.isMovie:
            #再生ボタンを作成
            self.playButton = tk.Button(self.containerFrame, text='▶', command=self.on_click_play_button)
            self.playButton.pack(expand=False, fill=tk.X, side=tk.LEFT)

        #参照テキストボックスを作成
        self.pathEntryText = tk.StringVar()
        self.pathEntry = tk.Entry(self.containerFrame, textvariable=self.pathEntryText, width=10)
        self.pathEntry.pack(expand=True, fill=tk.X, side=tk.LEFT, padx=5)
        #参照ボタンを作成
        self.referenceButton = tk.Button(self.containerFrame, text='参照', command=self.on_click_reference_button)
        self.referenceButton.pack(expand=False, fill=tk.X, side=tk.LEFT)

        #スペースを作成
        tk.Label(self.containerFrame, text='').pack(expand=False, fill=tk.X, side=tk.LEFT, padx=5)

        #確率テキストボックスを作成
        self.probabilityEntryText = tk.StringVar()
        self.probabilityEntry = tk.Entry(self.containerFrame, textvariable=self.probabilityEntryText, width=10)
        self.probabilityEntry.pack(expand=False, fill=tk.X, side=tk.LEFT)
        #"%"を作成
        self.percent = tk.Label(self.containerFrame, text='%')
        self.percent.pack(expand=False, fill=tk.X, side=tk.LEFT)

        #スペースを作成
        tk.Label(self.containerFrame, text='').pack(expand=False, fill=tk.X, side=tk.LEFT, padx=5)

        #isMovieがFalseのとき
        if not self.isMovie:
            #音量ラベルを作成
            self.volumeLabel = tk.Label(self.containerFrame, text='♪')
            self.volumeLabel.pack(expand=False, fill=tk.X, side=tk.LEFT)

            #音量スケールを作成
            self.volumeScale = ttk.Scale(
                self.containerFrame,
                from_=0,
                to=100,
                orient=tk.HORIZONTAL,
                command=self.on_change_volume_scale
            )
            self.volumeScale.set(self.volume)
            self.volumeScale.pack(expand=False, fill=tk.X, side=tk.LEFT)

            #スペースを作成
            tk.Label(self.containerFrame, text='').pack(expand=False, fill=tk.X, side=tk.LEFT, padx=5)
        
        #削除ボタンを作成
        self.deleteButton = tk.Button(self.containerFrame, text='×', command=self.on_click_delete_button)
        #削除ボタンの背景色を設定
        self.deleteButton.configure(bg='#f0908b')
        #削除ボタンを表示
        self.deleteButton.pack(expand=False, fill=tk.X, side=tk.LEFT)

        #エラーラベルを作成
        self.errorLabel = tk.Label(self, text='')
        #エラーラベルのfontを設定
        self.errorLabel.configure(font=font.Font(size=8))
        #エラーラベルの色を設定
        self.errorLabel.configure(foreground='#ff0000')
        #エラーラベルのアンカーを設定
        self.errorLabel.configure(anchor=tk.NW)
        #エラーラベルのPaddingを設定
        self.errorLabel.configure(padx=0, pady=0)
        #エラーラベルを表示
        self.errorLabel.pack(expand=True, fill=tk.X, side=tk.TOP)

    #再生ボタンを押したときのイベント
    def on_click_play_button(self):
        print('再生ボタンを押した')
        #pathを取得
        path = self.get_path()
        #pathが空のとき
        if path == '': 
            self.show_error_label('パスが空です')
            return
        
        #pathが空でないとき
        #soundを再生
        try:
            self.play_sound(path)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            self.show_error_label('ファイルが存在しません')
            return

    #参照ボタンを押したときのイベント
    def on_click_reference_button(self):
        self.controller.on_click_reference_button(self, self.key)

    #削除ボタンを押したときのイベント
    def on_click_delete_button(self):
        print('FilePathFrameを削除')
        #selfを削除
        self.parentClass.on_click_delete_button(self.index)

    #音量スケールを変更したときのイベント
    def on_change_volume_scale(self, volume):
        print(f'音量スケールを変更: {volume}')
        self.volume = volume
    
    #ファイルの種類を識別
    def is_movie(self):
        #ファイルタイプを取得
        fileType = self.controller.get_file_type(self.key)
        #ファイルタイプがmovieのとき
        if fileType == [('MP4', '*.mp4')]:
            return True
        #ファイルタイプがsoundのとき
        else:
            return False
        
    #pathを取得
    def get_path(self):
        return self.pathEntryText.get()
    
    #probabilityを取得
    def get_probability(self):
        text = self.probabilityEntryText.get()
        value = 0.0
        #self.probabilityEntryTextが空のとき
        if text == '': return 0.0
        try:
            value = float(text)
        except:
            pass
        return value
    
    #volumeを取得
    def get_volume(self):
        return int(float(self.volume))

    #soundを再生
    def play_sound(self, path):
        #pygame.mixerを初期化
        pygame.mixer.init()
        #音量を設定
        pygame.mixer.music.set_volume(self.get_volume()/100)
        #音楽を読み込む
        pygame.mixer.music.load(path)
        #音楽を再生する
        pygame.mixer.music.play(1)

    #movieを再生
    def play_movie(self):
        pass
    
    #errorCheck
    def is_Error(self):
        #pathEntryTextが空のとき
        if self.pathEntryText.get() == '':
            self.show_error_label('パスが空です')
            return True
        #probabilityEntryTextが空のとき
        if self.probabilityEntryText.get() == '':
            self.show_error_label('確率が空です')
            return True
        #probabilityEntryTextがfloatでないとき
        try:
            float(self.probabilityEntryText.get())
        except:
            self.show_error_label('確率は数値で入力してください')
            return True
        #probabilityEntryTextが0.0未満, 100.0以上のとき
        if 0.0 > float(self.probabilityEntryText.get()) or float(self.probabilityEntryText.get()) > 100.0:
            self.show_error_label('確率は0.0以上, 100.0以下で入力してください')
            return True
        
        #エラーがないとき
        self.show_error_label('')
        return False
    
    #errorLabelを表示
    def show_error_label(self, text):
        self.errorLabel.configure(text=text)

