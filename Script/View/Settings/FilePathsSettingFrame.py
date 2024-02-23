from Script.View.Settings import FilePathFrame
import tkinter as tk
from tkinter import ttk
from tkinter import font


class FilePathsSettingFrame(ttk.Frame):
    def __init__(self, controller=None, parent=None, key=None, title=None, pathsData=None):
        super().__init__(parent, padding=(0,5))

        self.controller = controller
        # self.parent = parent
        self.key = key
        self.title = title
        self.pathsData = pathsData
        self.paths = []
        self.maxPathsCount = 6

        self.set_title_frame()
        self.set_paths_frame()
        self.set_path_frame()

        self.columnconfigure(0, weight=1)

    #タイトルラベルを設置
    def set_title_frame(self):
        #タイトルのフレームを作成
        titleFrame = ttk.Frame(self)
        #タイトルラベルを作成
        self.titleLabel = tk.Label(titleFrame, text=self.title)
        #タイトルラベルの色を設定 (グレー)
        self.titleLabel.configure(bg='#e6e6e6')
        #タイトルラベルを表示
        self.titleLabel.pack(expand=True, fill=tk.X, side=tk.LEFT)
        #addtivePathFrameButtonを作成
        self.addtivePathFrameButton = tk.Button(titleFrame, text='+', command=self.on_click_addtive_path_frame_button)
        #addtivePathFrameButtonを右に寄せる
        self.addtivePathFrameButton.pack(side=tk.RIGHT)
        #タイトルのフレームを表示
        titleFrame.pack(expand=True, fill=tk.X, side=tk.TOP)
        #errorLabelを作成
        self.errorLabel = tk.Label(self, text='')
        #errorLabelの色を設定 (赤)
        self.errorLabel.configure(foreground='#ff0000')
        #errorLabelのサイズを設定
        self.errorLabel.configure(font=font.Font(size=8))
        #errorLabelを表示
        self.errorLabel.pack(expand=True, fill=tk.X, side=tk.TOP)

    #pathsFrameを設置
    def set_paths_frame(self):
        #pathsFrameを作成
        self.pathsFrame = ttk.Frame(self)
        #pathsFrameを表示
        self.pathsFrame.pack(expand=True, fill=tk.X, side=tk.TOP)

    #pathFrameを設置
    def set_path_frame(self):
        #pathsDataの数だけpathFrameを作成
        for index, dict in enumerate(self.pathsData):
            self.add_path_frame(index)
            pathFrame = self.paths[index]
            #pathFrameのpathEntryTextを設定
            pathFrame.pathEntryText.set(dict['path'])
            #pathFrameのpobabilityEntryTextを設定
            pathFrame.probabilityEntryText.set(dict['probability'])

            #pathFrameのisMovieがFalseの場合
            if pathFrame.isMovie == False:
                #pathFrameのvolumeScaleを設定
                pathFrame.volumeScale.set(dict['volume'])
         
    #pathFrameを追加
    def add_path_frame(self, index):
        #pathFrameを作成
        pathFrame = FilePathFrame.FilePathFrame(self.controller, self, self.pathsFrame, self.key, index)
        #pathFrameを表示
        pathFrame.pack(expand=True, fill=tk.X, side=tk.TOP)
        #pathFrameをpathsに追加
        self.paths.append(pathFrame)

    #addtivePathFrameButtonを押したときのイベント
    def on_click_addtive_path_frame_button(self):
        print(f"FilePathsSettingFrame.on_click_addtive_path_frame_button: index={len(self.paths)}")
        pathsCount = len(self.paths)
        #pathsCountが6以上の場合
        if pathsCount >= self.maxPathsCount:
            #エラーラベルを表示
            self.errorLabel.configure(text='これ以上追加できません')
            return
        #pathFrameを追加
        self.add_path_frame(pathsCount)
        #その他の処理をcontrollerに任せる
        self.controller.on_click_addtive_path_frame_button()

    #pathFrameの削除ボタンを押したときのイベント
    def on_click_delete_button(self, index):
        print(f"FilePathsSettingFrame.on_click_delete_button: index={index}")
        #エラーラベルを非表示
        self.errorLabel.configure(text='')
        #pathFrameを削除
        self.paths[index].destroy()
        #pathsからpathFrameを削除
        self.paths.pop(index)
        #pathFrameのindexを設定
        for index, path in enumerate(self.paths):
            path.index = index
