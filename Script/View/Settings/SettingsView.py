from Script.View.Settings import PathSettingFrame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


#設定ウィンドウを作成
class SettingsView(tk.Toplevel):
    def __init__(self, controller=None, settings=None):
        super().__init__()
        self.geometry('300x450')
        self.title('設定')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.controller = controller

        #あなたのtwitch配信URL用Frameを作成
        self.urlFrame = ttk.Frame(self, padding=(10,10))
        self.urlFrame.pack(fill=tk.X, side=tk.TOP)
        #ラベルを作成
        tk.Label(self.urlFrame, text='あなたのtwitch配信URL').pack(anchor=tk.W)
        #テキストボックスを作成
        self.liveUrlEntry = ttk.Entry(self.urlFrame, width=30)
        self.liveUrlEntry.pack(fill=tk.X, side=tk.TOP)

        #仕切り線
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

        #コメント取得時の効果音用Frameを作成
        self.commentSoundPathFrame = PathSettingFrame.PathSettingFrame(self, 'commentSoundPath', 'コメント取得時の効果音(mp3)')
        self.commentSoundPathFrame.pack(side=tk.TOP, fill=tk.X)

        #コメント取得時の演出用Frameを作成
        self.commentMoviePathFrame = PathSettingFrame.PathSettingFrame(self, 'commentMoviePath', 'コメント取得時の演出(mp4)')
        self.commentMoviePathFrame.pack(side=tk.TOP, fill=tk.X)

        #仕切り線
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

        #フォロワー取得時の効果音用Frameを作成
        self.followerSoundPathFrame = PathSettingFrame.PathSettingFrame(self,'followerSoundPath', 'フォロワー取得時の効果音(mp3)')
        self.followerSoundPathFrame.pack(side=tk.TOP, fill=tk.X)

        #フォロワー取得時の演出用Frameを作成
        self.followerMoviePathFrame = PathSettingFrame.PathSettingFrame(self, 'followerMoviePath', 'フォロワー取得時の演出(mp4)')
        self.followerMoviePathFrame.pack(side=tk.TOP, fill=tk.X)

        #仕切り線
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP, padx=10, pady=10)

        #ボタン用Frameを作成
        self.buttonFrame = ttk.Frame(self, padding=(10,10))
        self.buttonFrame.pack(fill=tk.X, side=tk.TOP)
        #キャンセルボタンを作成
        self.cancelButton = ttk.Button(self.buttonFrame, text='キャンセル', command=self.on_click_cancel_button)
        self.cancelButton.pack(side=tk.LEFT)
        #保存ボタンを作成
        self.saveButton = ttk.Button(self.buttonFrame, text='保存', command=self.on_click_save_button)
        self.saveButton.pack(side=tk.RIGHT)

        #settingsの値を設定
        self.liveUrlEntry.insert(tk.END, settings['liveURL'])
        self.commentSoundPathFrame.entry.insert(tk.END, settings['commentSoundPath'])
        self.commentMoviePathFrame.entry.insert(tk.END, settings['commentMoviePath'])
        self.followerSoundPathFrame.entry.insert(tk.END, settings['followerSoundPath'])
        self.followerMoviePathFrame.entry.insert(tk.END, settings['followerMoviePath'])

    def close(self):
        self.destroy()

    #キャンセルボタンを押したときのイベント
    def on_click_cancel_button(self):
        self.controller.on_click_cancel_button()

    #保存ボタンを押したときのイベント
    def on_click_save_button(self):
        self.controller.on_click_save_button()

    #参照ボタンを押したときのイベント
    def on_click_reference_button(self, type):
        self.controller.on_click_reference_button(type)

    #ファイル選択ダイアログを表示
    def show_file_dialog(self, type, fileTypes):
        if fileTypes == []: return
        #初期ディレクトリを指定
        dir = 'C:\\'
        #ファイル選択ダイアログを表示
        path = filedialog.askopenfilename(filetypes=fileTypes, initialdir=dir)

        if path:
            if type == 'commentSoundPath':
                self.commentSoundPathFrame.entry.insert(tk.END, path)
            elif type == 'commentMoviePath':
                self.commentMoviePathFrame.entry.delete(0, tk.END)
                self.commentMoviePathFrame.entry.insert(tk.END, path)
            elif type == 'followerSoundPath':
                self.followerSoundPathFrame.entry.delete(0, tk.END)
                self.followerSoundPathFrame.entry.insert(tk.END, path)
            elif type == 'followerMoviePath':
                self.followerMoviePathFrame.entry.delete(0, tk.END)
                self.followerMoviePathFrame.entry.insert(tk.END, path)
            else:
                return

        #SettingsViewを最前面に表示
        self.lift()
        self.attributes('-topmost', True)
