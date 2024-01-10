import os
import time

#Splashウィンドウのモデル
class SplashModel:
    #DBディレクトリのパス
    dbPath = "DataBase"
    #RowMaterialディレクトリのパス
    rowMaterialPath = dbPath + "/RowMaterial"
    #Imageディレクトリのパス
    imagePath = rowMaterialPath + "/Image"
    #Soundディレクトリのパス
    soundPath = rowMaterialPath + "/Sound"

    #すべてのパス
    allPath = [dbPath, rowMaterialPath, imagePath, soundPath]

    #最小の待機時間
    minWaitTime = 1

    def __init__(self):
        pass

    #スタートタイムを取得
    def get_time(self):
        return time.time()

    #三秒経過するまで待機する
    def wait(self, start_time):
        #経過時間を取得
        elapsed_time = self.get_time() - start_time
        #三秒経過するまで待機する
        if elapsed_time < self.minWaitTime:
            time.sleep(self.minWaitTime - elapsed_time)

    #ディレクトリの存在を確認する
    def check_directory(self):
        #すべてのパスを確認する
        for path in self.allPath:
            #ディレクトリが存在しないとき
            if not os.path.exists(path):
                #ディレクトリを作成する
                os.mkdir(path)
