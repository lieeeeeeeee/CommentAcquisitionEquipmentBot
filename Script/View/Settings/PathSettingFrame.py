import tkinter as tk
from tkinter import ttk

#設定ウィンドウを作成
class PathSettingFrame(ttk.Frame):
    def __init__(self, parent=None, type=None, text=None):
        super().__init__(parent, padding=(10,10))
        self.parent = parent
        self.type = type

        #ラベルを作成
        self.label = tk.Label(self, text=text)
        self.label.grid(row=0, column=0, sticky=tk.W)
        #テキストボックスを作成
        self.entryText = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entryText, width=10)
        self.entry.grid(row=1, column=0, sticky=tk.EW)
        #参照ボタンを作成
        self.referenceButton = tk.Button(self, text='参照', command=self.on_click_reference_button)
        self.referenceButton.grid(row=1, column=1)
        #フレームのColumnを調整
        self.columnconfigure(0, weight=1)

    def on_click_reference_button(self):
        self.parent.on_click_reference_button(self.type)
