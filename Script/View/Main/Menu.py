from Script.View.Main import MenuButton
import tkinter as tk

#ウィンドウのメニューを作成
class Menu(tk.Frame):
    def __init__(self, controller=None, parent=None, contents=None):
        super().__init__(parent, relief=tk.GROOVE, bd=2)
        self.controller = controller
        self.parent = parent
        self.contents = contents
        self.buttons = []

        #コンテンツを作成
        self.create_contents()

    #コンテンツを作成
    def create_contents(self):
        #ショートカットキーを取得
        shortcutKeys = self.parent.load_shortcut_keys()

        for content in self.contents:
            buttonTitle = shortcutKeys[content]["name"]
            shortcutKey = shortcutKeys[content]["display"]
            #ボタンを作成
            button = MenuButton.MenuButton(self.controller, self, buttonTitle, shortcutKey,content)
            button.pack(fill=tk.X, side=tk.TOP)

            #ボタンを追加
            self.buttons.append(button)

            #コンテンツが最後の場合は仕切り線を表示しない
            if content == self.contents[-1]: return

            #仕切り線
            tk.ttk.Separator(self, orient='horizontal').pack(fill=tk.X, side=tk.TOP, padx=5)
