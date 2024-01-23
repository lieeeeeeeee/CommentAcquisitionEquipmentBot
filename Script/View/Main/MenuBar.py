from Script.View.Main import MenuBarButton

import tkinter as tk

#ウィンドウのメニューバーを作成
class MenuBar(tk.Frame):
    def __init__(self, controller=None, parent=None, menuBarContents=None):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.menuBarContents = menuBarContents
        self.isVisible = True

        #メニューの色を設定
        self.configure(bg='#ffffff')
        #メニューバーのColumnを調整
        self.columnconfigure(0, weight=1)

        #仕切り線を表示
        tk.ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP)
        #仕切り線を表示
        tk.ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.BOTTOM)

        #コンテンツを作成
        self.create_contents()

    #コンテンツを作成
    def create_contents(self):
        #余白を作成
        padding = tk.Label(self, text='')
        padding.configure(bg='#ffffff')
        padding.pack(side=tk.LEFT)
        #仕切り線
        tk.ttk.Separator(self, orient='vertical').pack(fill=tk.Y, side=tk.LEFT)
        for key in self.menuBarContents.keys():
            #ボタンを作成
            button = MenuBarButton.MenuBarButton(self.controller, self, text=key)
            #ボタンを表示
            button.pack(side=tk.LEFT)

            #仕切り線
            tk.ttk.Separator(self, orient='vertical').pack(fill=tk.Y, side=tk.LEFT)

        #ショートカットキーを取得
        shortcutKeys = self.parent.load_shortcut_keys()
        #ショートカットキーラベルを作成
        shortcutKeyLabel = tk.Label(self, text=shortcutKeys['menu_bar']['display'])
        #ショートカットキーラベルの色を設定
        shortcutKeyLabel.configure(bg='#ffffff')
        shortcutKeyLabel.pack(side=tk.RIGHT, padx=10)
