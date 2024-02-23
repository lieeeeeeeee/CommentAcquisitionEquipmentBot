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
        #アプリ名を設定
        self.title = tk.Label(self, text='CAEBot for Twitch', font=("Helvetica", 20, "bold"))
        #アプリ名を画面の上部に配置
        self.title.pack(expand=True, fill=tk.X, side=tk.TOP)

        #コピーライトを設定
        self.copyRight = tk.Label(self, text='© 2020 CAEBot', font=("Helvetica", 10, "italic"))
        #コピーライトをアプリ名の下に配置
        self.copyRight.pack(expand=True, fill=tk.X, side=tk.TOP)

        #バージョンを設定
        self.version = tk.Label(self, text='Version 0.0.1', font=("Helvetica", 10))
        #バージョンをコピーライトの下に配置
        self.version.pack(expand=True, fill=tk.X, side=tk.TOP)

        #ロード中のラベルを作成
        self.label = tk.Label(self, text='Loading...')
        #ロード中のラベルを画面の左下に配置
        self.label.pack(side=tk.LEFT, anchor=tk.SW)
        #ウィンドウを表示
        self.update()

    #ウィンドウを閉じる
    def close(self):
        self.destroy()
