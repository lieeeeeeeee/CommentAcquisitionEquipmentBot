from Script.View.Settings import FilePathsSettingFrame
import tkinter as tk
from tkinter import ttk

class FilePathsSettingsFrame(ttk.Frame):
    def __init__(self, controller=None, parent=None):
        super().__init__(parent, padding=(10,0))

        self.controller = controller
        self.parent = parent
        self.filePathsSettingFrames = []

        #スクロールフレームを設置
        # self.set_scroll_frame()
        #filePathFrameを設置
        self.set_file_paths_setting_frame()
        
    #スクロールフレームを設置
    def set_scroll_frame(self):
        #スクロールキャンバスを作成
        self.scrollCanvas = tk.Canvas(self)
        #スクロールフレームを作成
        self.scrollFrame = ttk.Frame(self.scrollCanvas)
        #スクロールバーを作成
        self.scrollBar = ttk.Scrollbar(self.scrollCanvas, orient=tk.VERTICAL, command=self.scrollCanvas.yview)
        #スクロールキャンバスにスクロールバーを設定
        self.scrollCanvas.configure(yscrollcommand=self.scrollBar.set)
        #スクロールキャンバスを表示
        self.scrollCanvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        #スクロールバーを表示
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        #スクロールフレームを表示
        self.scrollCanvas.create_window((0,0), window=self.scrollFrame, anchor=tk.NW)


    #filePathsSettingFrameを設置
    def set_file_paths_setting_frame(self):
        filePaths = self.controller.get_filePaths()
        #filePathFrameを作成
        for key in filePaths:
            filePathsSettingFrame = FilePathsSettingFrame.FilePathsSettingFrame(
                self.controller, 
                # self.scrollFrame, 
                self,
                key, 
                self.get_file_path_setting_frame_title(key),
                filePaths[key]
            )
            filePathsSettingFrame.pack(expand=False, fill=tk.X, side=tk.TOP)
            self.filePathsSettingFrames.append(filePathsSettingFrame)
    
    #FilePathSettingFrameTitleを取得
    def get_file_path_setting_frame_title(self, key):
        return self.controller.get_file_path_setting_frame_title(key)
    
    #scrollregionを現在のscrollCanvasの2倍に設定
    def set_scrollregion(self):
        print('set_scrollregion')
        return
        # self.scrollCanvas.configure(scrollregion=self.scrollCanvas.bbox('all'))