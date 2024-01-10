import tkinter as tk

#メニューのボタンを作成
class MenuButton(tk.Button):
    def __init__(self, parent=None, text=None, shortcutKey=None, shortcutKeyType=None):
        super().__init__(parent, relief=tk.FLAT, anchor=tk.W)

        self.parent = parent
        self.text = text
        self.shortcutKeyType = shortcutKeyType

        #ボタンのイベントを監視
        self.bind('<Button-1>', self.on_click_button)
        #ボタンの色を設定
        self.configure(bg='#ffffff')

        #ボタンのテキストを設定
        buttonTitle = tk.Label(self, text=text)
        buttonTitle.configure(bg='#ffffff')
        buttonTitle.pack(side=tk.LEFT, padx=20)
        buttonTitle.bind('<Button-1>', self.on_click_button)

        #余白を作成
        padding = tk.Label(self, text='')
        padding.configure(bg='#ffffff')
        padding.pack(side=tk.LEFT, padx=30)
        padding.bind('<Button-1>', self.on_click_button)

        #ボタンの色を設定
        self.configure(bg='#ffffff')

        #ショートカットキーラベルを作成
        self.shortcutKeyLabel = tk.Label(self, text=shortcutKey)
        self.shortcutKeyLabel.pack(side=tk.RIGHT, padx=20)
        self.shortcutKeyLabel.configure(bg='#ffffff')
        #ショートカットキーラベルのクリックイベントを監視
        self.shortcutKeyLabel.bind('<Button-1>', self.on_click_button)

        #ボタンのColumnを調整
        self.columnconfigure(0, weight=1)

    #ボタンを押したときのイベント
    def on_click_button(self, event=None):
        self.parent.on_click_menu_button(self.shortcutKeyType)
