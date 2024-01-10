import tkinter as tk

#メニューバーのボタンを作成
class MenuBarButton(tk.Button):
    def __init__(self, parent=None, text=None):
        super().__init__(parent, text=text, command=self.on_click_button, width=3+len(text), height=1, relief=tk.FLAT)
        self.parent = parent
        self.text = text

        #ボタンの色を設定
        self.configure(bg='#ffffff')

    #ボタンを押したときのイベント
    def on_click_button(self):
        self.parent.on_click_menu_bar_button(self)
