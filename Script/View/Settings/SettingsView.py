from Script.View.Settings import FilePathsSettingsFrame
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#設定ウィンドウを作成
class SettingsView(tk.Toplevel):
    def __init__(self, controller=None):
        super().__init__()
        self.geometry('800x600')
        self.title('設定')
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.controller = controller

        #あなたのtwitch配信URL用Frameを作成
        self.urlFrame = ttk.Frame(self, padding=(10,10))
        self.urlFrame.pack(fill=tk.X, side=tk.TOP)
        #ラベルを作成
        tk.Label(self.urlFrame, text='あなたのtwitch配信URL').pack(anchor=tk.W)
        #テキストボックスを作成
        self.liveUrlEntry = ttk.Entry(self.urlFrame, width=30)
        self.liveUrlEntry.pack(expand=False, fill=tk.X, side=tk.TOP)

        #ボタン用Frameを作成
        self.buttonFrame = ttk.Frame(self, padding=(10,10))
        self.buttonFrame.pack(expand=False, fill=tk.BOTH, side=tk.BOTTOM)
        #キャンセルボタンを作成
        self.cancelButton = ttk.Button(self.buttonFrame, text='キャンセル', command=self.on_click_cancel_button)
        self.cancelButton.pack(side=tk.LEFT)
        #保存ボタンを作成
        self.saveButton = ttk.Button(self.buttonFrame, text='保存', command=self.on_click_save_button)
        self.saveButton.pack(side=tk.RIGHT)

        #仕切り線
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=0)
        

        #仕切り線
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP, padx=10, pady=0)

        #ファイルパス設定用Frameを作成
        self.filePathsSettingsFrame = FilePathsSettingsFrame.FilePathsSettingsFrame(self.controller, self)
        self.filePathsSettingsFrame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=10, pady=10)

        #settingsの値を設定
        self.liveUrlEntry.insert(tk.END, self.controller.get_liveURL())

    def close(self):
        self.destroy()

    #キャンセルボタンを押したときのイベント
    def on_click_cancel_button(self):
        self.controller.on_click_cancel_button()

    #保存ボタンを押したときのイベント
    def on_click_save_button(self):
        self.controller.on_click_save_button()

    #scrollregionを設定
    def set_scrollregion(self):
        self.filePathsSettingsFrame.set_scrollregion()

    #liveURLを取得
    def get_liveURL(self):
        return self.liveUrlEntry.get()

    #ファイル選択ダイアログを表示
    def show_file_dialog(self, pathFrame, fileTypes):
        # if fileTypes == []: return
        #初期ディレクトリを指定
        dir = 'C:\\'
        #ファイル選択ダイアログを表示
        path = filedialog.askopenfilename(filetypes=fileTypes, initialdir=dir)

        #pathが空の場合は処理を終了
        if path == '': return

        #pathを設定
        pathFrame.pathEntryText.set(path)

        #SettingsViewを最前面に表示
        self.lift()
