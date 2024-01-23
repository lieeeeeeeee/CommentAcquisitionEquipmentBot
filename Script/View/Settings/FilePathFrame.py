import tkinter as tk
from tkinter import ttk
from tkinter import font

class FilePathFrame(ttk.Frame):
    def __init__(self, controller=None, parent=None, key=None, index=None):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent
        self.key = key
        self.index = index

        #参照テキストボックスを作成
        self.pathEntryText = tk.StringVar()
        self.pathEntry = tk.Entry(self, textvariable=self.pathEntryText, width=10)
        self.pathEntry.grid(row=0, column=0, sticky=tk.EW)
        #参照ボタンを作成
        self.referenceButton = tk.Button(self, text='参照', command=self.on_click_reference_button)
        self.referenceButton.grid(row=0, column=1)
        #":"を作成
        self.colon = tk.Label(self, text=':')
        self.colon.grid(row=0, column=2)
        #確率テキストボックスを作成
        self.probabilityEntryText = tk.StringVar()
        self.probabilityEntry = tk.Entry(self, textvariable=self.probabilityEntryText, width=10)
        self.probabilityEntry.grid(row=0, column=3, sticky=tk.EW)
        #"%"を作成
        self.percent = tk.Label(self, text='%')
        self.percent.grid(row=0, column=4)
        
        #削除ボタンを作成
        self.deleteButton = tk.Button(self, text='削除', command=self.on_click_delete_button)
        self.deleteButton.grid(row=0, column=5)

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
        self.errorLabel.grid(row=1, column=0, columnspan=6, sticky=tk.W)

        #フレームのColumnを調整
        self.columnconfigure(0, weight=1)
        

    #参照ボタンを押したときのイベント
    def on_click_reference_button(self):
        self.controller.on_click_reference_button(self.key, self.index)

    #削除ボタンを押したときのイベント
    def on_click_delete_button(self):
        print('FilePathFrameを削除')
        #selfを削除
        self.parent.on_click_delete_button(self.index)

