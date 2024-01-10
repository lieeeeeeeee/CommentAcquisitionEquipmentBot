from Script.Model import SplashModel
from Script.View.Splash import SplashView
from Script import MainController

#スプラッシュウィンドウのコントローラー
class SplashController:
    def __init__(self):
        #スプラッシュウィンドウのモデルを作成
        self.model = SplashModel.SplashModel()

        #スタートタイムを取得
        self.start_time = self.model.get_time()

        #スプラッシュウィンドウを作成
        self.view = SplashView.SplashView()

        #モデルのディレクトリを確認
        self.model.check_directory()

        #スプラッシュウィンドウを少なくとも3秒表示する
        self.model.wait(self.start_time)

        #スプラッシュウィンドウを閉じる
        self.close()

        #MainControllerに処理を移譲
        MainController.MainController()

    #スプラッシュウィンドウを閉じる
    def close(self):
        #スプラッシュウィンドウを閉じる
        self.view.close()
