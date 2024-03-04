from Script.Model import MainModel
from Script.View.Main import MainView
from Script.API import TwitchAPI
from Script.API import YoutubeAPI
from Script import SettingsController
import threading
import asyncio
import nest_asyncio


#メインウィンドウのコントローラー
class MainController:
    def __init__(self):
        # nest_asyncioを適用
        nest_asyncio.apply()

        #設定ウィンドウコントローラーを作成
        self.settingsController = SettingsController.SettingsController(self)

        #メインウィンドウのモデルを作成
        self.model = MainModel.MainModel()
        #メインウィンドウを作成
        self.view = MainView.MainView(self)
        #メインウィンドウを表示
        self.view.mainloop()

    #クリックイベントを監視
    def on_click_main_view(self, event):
        print("click main view", event)
        self.view.remove_temporary_frame()

    #キー入力を監視
    def on_input_key(self, key):
        #入力がF11のとき
        if key == self.model.shortcut_keys['full_screen']['key']:
            #フルスクリーンの切り替え
            self.view.toggle_fullscreen()

    #ショートカットキーを監視
    def on_input_ctrl_shortcut_key(self, keysym, state):
        menuBar = self.model.shortcut_keys['menu_bar']
        settings = self.model.shortcut_keys['settings']
        exit = self.model.shortcut_keys['exit']
        join = self.model.shortcut_keys['join']
        leave = self.model.shortcut_keys['leave']

        #入力がCtrl+Shift+bのとき
        if keysym == menuBar['keysym'] and state == menuBar['state']:
            #メニューバーの表示・非表示を切り替える
            self.view.toggle_menubar()

        #入力がCtrl+`のとき
        if keysym == settings['keysym'] and state == settings['state']:
            #設定ウィンドウを表示
            self.open_settings()

        #入力がCtrl+qのとき
        if keysym == exit['keysym'] and state == exit['state']:
            #メインウィンドウを閉じる
            self.Exit()

        #入力がCtrl+jのとき
        if keysym == join['keysym'] and state == join['state']:
            #チャンネルに参加
            self.join_channel()

        #入力がCtrl+lのとき
        if keysym == leave['keysym'] and state == leave['state']:
            #チャンネルから離脱
            self.leave_channel()

    #メニューバーのボタンを押したときのイベント
    def on_click_menu_bar_button(self, button):
        #メニューを表示
        self.view.show_menu(button)

    #メニューボタンを押したときのイベント
    def on_click_menu_button(self, content):
        print("click menu button", content)
        if content == 'settings':
            #設定ウィンドウを表示
            self.open_settings()
        elif content == 'exit':
            #メインウィンドウを閉じる
            self.Exit()
        elif content == 'join':
            #チャンネルに参加
            self.join_channel()
        elif content == 'leave':
            #チャンネルから離脱
            self.leave_channel()

    #設定ウィンドウを表示
    def open_settings(self):
        self.settingsController.open()
    #メインウィンドウを閉じる
    def Exit(self):
        self.view.close()

    #ショートカットキーを取得
    def load_shortcut_keys(self):
        return self.model.shortcut_keys

    #チャンネルに参加
    def join_channel(self):
        #liveDataを取得
        liveData = self.settingsController.get_liveData()

        liveAccountID = liveData[0]

        liveMedium = liveData[1]


        #チャンネル名が空のとき
        if liveAccountID == "":
            self.show_error_message("チャンネル名が設定されていません")
            return

        #ボットが存在するとき
        if hasattr(self, 'bot'):
            self.show_error_message("既に接続しています")
            return

        #ボットを作成
        self.bot = None

        if liveMedium == "Twitch":
            self.bot = TwitchAPI.Bot(self, liveAccountID)
        elif liveMedium == "Youtube":
            self.bot = YoutubeAPI.Bot(self, liveAccountID)
        else:
            self.show_error_message("配信サービスが選択されていません")
            return
        
        try:
            #ボットを起動
            #スレッドを作成
            runThread = threading.Thread(target=self.bot.run, daemon=True) 
            #スレッドを起動
            runThread.start()  
            self.view.show_normal_message("接続しました")         
        except Exception as e:
            self.show_error_message(f"エラーが発生しました: {e}")
            #ボットを削除
            del self.bot
            return

    #チャンネルから離脱
    def leave_channel(self):
        #self.botがnullのとき
        if not hasattr(self, 'bot'):
            self.show_error_message("接続していません")
            return

        #ループを作成
        loop = asyncio.get_event_loop()
        #ボットを停止
        try:
            loop.run_until_complete(self.bot.stop())
        except Exception as e:
            print(f"エラーが発生しました: {e}")
        finally:
            #ループを停止
            if not loop.is_closed():
                loop.close()
        #メッセージを表示
        self.view.show_normal_message("切断しました")
        
        #ボットを削除
        del self.bot

    #コメントを受信時のイベント
    def on_receive_message(self, message):
        #CommentSoundFilePathsを取得
        CommentSoundFilePaths = self.settingsController.model.get_CommentSoundFilePaths()
        #CommentMovieFilePathsを取得
        CommentMovieFilePaths = self.settingsController.model.get_CommentMovieFilePaths()

        #CommentSoundFilePathsが空でないとき
        if CommentSoundFilePaths != None:
            #CommentSoundFilePathsからランダムに取得
            soundData = self.model.get_random_Path(CommentSoundFilePaths)
            #soundDataが空でないとき
            if soundData != None:
                #soundを再生
                self.view.play_sound(soundData)

        #CommentMovieFilePathsが空でないとき
        if CommentMovieFilePaths != None:
            #CommentMovieFilePathsからランダムに取得
            movieData = self.model.get_random_Path(CommentMovieFilePaths)
            #movieDataが空でないとき
            if movieData != None:
                moviePath = movieData[0]
                #movieを再生
                self.view.play_movie(moviePath)

    #エラーメッセージを表示
    def show_error_message(self, message):
        self.view.show_error_message(message)

