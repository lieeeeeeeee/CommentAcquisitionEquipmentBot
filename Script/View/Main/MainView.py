from Script.View.Main import MenuBar
from Script.View.Main import Menu
import tkinter as tk
from tkinter import messagebox

#メインウィンドウを作成
class MainView(tk.Tk):
    menuBarContents = {
        "ファイル": ["settings", "exit"],
        "配信": ["join", "leave"],
    }

    def __init__(self, controller=None):
        super().__init__()
        #画面サイズを指定
        self.geometry('786x432')
        self.title('Comment Acquisition Equipment Bot')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.controller = controller
        self.temporaryFrame = None

        #背景色(黄緑)を指定
        self.configure(bg='#90EE90')

        #メニューバーを作成
        self.menuBar = MenuBar.MenuBar(self, self.menuBarContents)
        #メニューバーを表示
        self.menuBar.pack(side=tk.TOP, fill=tk.X, ipadx=5)

        try :
            #クリックイベントを監視
            self.bind('<Button-1>', self.on_click_main_view)
        except:
            print("Error")

        #キー入力を監視
        self.bind('<Key>', self.on_input_key)
        #ショートカットキーを監視
        self.bind('<Control-Key>', self.on_input_ctrl_shortcut_key)

    def close(self):
        self.destroy()

    #クリックイベントを監視
    def on_click_main_view(self, event):
        self.controller.on_click_main_view(event)

    #キー入力を監視
    def on_input_key(self, event):
        self.controller.on_input_key(event.keysym)

    #ショートカットキーを監視
    def on_input_ctrl_shortcut_key(self, event):
        print(event.keysym, event.state)
        self.controller.on_input_ctrl_shortcut_key(event.keysym, event.state)

    #メニューバーのボタンを押したときのイベント
    def on_click_menu_bar_button(self, button):
        self.controller.on_click_menu_bar_button(button)

    #メニューボタンを押したときのイベント
    def on_click_menu_button(self, content):
        self.controller.on_click_menu_button(content)

    #フルスクリーンの切り替え
    def toggle_fullscreen(self):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    #メニューバーの表示・非表示を切り替える
    def toggle_menubar(self):
        self.menuBar.isVisible = not self.menuBar.isVisible
        if self.menuBar.isVisible:
            self.menuBar.pack(side=tk.TOP, fill=tk.X, ipadx=5)
        else:
            self.menuBar.pack_forget()

    #メニューを表示
    def show_menu(self, button):
        menuContents = self.menuBarContents[button.text]
        menu = Menu.Menu(self, menuContents)

        #仕切り線の幅
        separatorWidth = 2
        #メニューバーの位置を取得
        menuBarX = self.menuBar.winfo_rootx()
        #ボタンの位置を取得
        buttonX = button.winfo_rootx()
        #ボタンの高さを取得
        buttonHeight = button.winfo_height()

        #一時的なフレームを作成
        self.temporaryFrame = menu
        #一時的なフレームを表示
        menu.place(
            x=buttonX-menuBarX-separatorWidth, y=buttonHeight+separatorWidth
        )

    #一時的なフレームを削除
    def remove_temporary_frame(self):
        if self.temporaryFrame != None:
            self.temporaryFrame.destroy()
            self.temporaryFrame = None

    #ショートカットキーを取得
    def load_shortcut_keys(self):
        return self.controller.load_shortcut_keys()

    #エラーメッセージを表示
    def show_error_message(self, message):
        #エラーメッセージを表示
        messagebox.showerror('エラー', message)
