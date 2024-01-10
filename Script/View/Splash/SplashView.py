import tkinter as tk

#Splashウィンドウを作成
class SplashView(tk.Tk):
    def __init__(self):
        super().__init__()
        #ウィンドウを最前面に表示する
        self.attributes('-topmost', True)
        #ウィンドウのサイズを設定
        self.geometry('500x300')
        #ウィンドウの位置を画面の中央に設定
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth()/2 - 250), int(self.winfo_screenheight()/2 - 150)))
        #タイトルバーを非表示にする
        self.overrideredirect(True)
        #ロード中のラベルを作成
        self.label = tk.Label(self, text='Loading...')
        #ロード中のラベルを画面の左下に配置
        self.label.place(x=5, y=280)
        #ウィンドウを表示
        self.update()

    #ウィンドウを閉じる
    def close(self):
        self.destroy()
