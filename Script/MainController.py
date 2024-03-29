from Script.Model import MainModel
from Script.View.Main import MainView
from Script.API import TwitchAPI
from Script import SettingsController


#メインウィンドウのコントローラー
class MainController:
    def __init__(self):
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
        #チャンネル名を取得
        channelName = self.settingsController.model.get_accountID()
        #チャンネル名が空のとき
        if channelName == "":
            self.show_error_message("チャンネル名が設定されていません")
            return

        #ボットが存在するとき
        if hasattr(self, 'bot'):
            self.show_error_message("既に接続しています")
            return

        #ボットを作成
        self.bot = TwitchAPI.Bot(self, channelName)
        try:
            #ボットを起動
            self.bot.run()
        except Exception as e:
            self.show_error_message(f"エラーが発生しました: {e}")
            #ボットを削除
            del self.bot
            return

    #チャンネルから離脱
    def leave_channel(self):
        #ボットが存在しないとき
        if not hasattr(self, 'bot'):
            self.show_error_message("接続しているチャンネルがありません")
            return

        #ボットを停止
        self.bot.stop()
        #ボットを削除
        del self.bot

    #コメントを受信時のイベント
    def on_receive_message(self, message):
        #コメントを表示
        print(f"{message.author.name}: {message.content}")

    #エラーメッセージを表示
    def show_error_message(self, message):
        self.view.show_error_message(message)
