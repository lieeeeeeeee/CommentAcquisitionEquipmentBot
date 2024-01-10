from Script.Model import SettingsModel
from Script.View.Settings import SettingsView

#設定ウィンドウのコントローラー
class SettingsController:

  def __init__(self, root=None):
    self.root = root
    #設定ウィンドウのモデルを作成
    self.model = SettingsModel.SettingsModel()
    self.settings = self.model.load_settingsFile()
    self.is_open = False

  def open(self):
    if self.is_open: return
    self.is_open = True

    #設定ウィンドウを作成
    self.view = SettingsView.SettingsView(self, self.settings)
    #windowを削除したときのイベント
    self.view.protocol('WM_DELETE_WINDOW', self.close)

    #設定ウィンドウを表示
    self.view.mainloop()

  #closeボタンを押したときのイベント
  def close(self):
    #設定ウィンドウを閉じる
    self.is_open = False
    self.view.close()

  #キャンセルボタンを押したときのイベント
  def on_click_cancel_button(self):
    #設定ウィンドウを閉じる
    self.close()

  #保存ボタンを押したときのイベント
  def on_click_save_button(self):
    #設定を取得
    self.settings['liveURL'] = self.view.liveUrlEntry.get()
    self.settings['commentSoundPath'] = self.view.commentSoundPathFrame.entry.get()
    self.settings['followerSoundPath'] = self.view.followerSoundPathFrame.entry.get()
    self.settings['followerMoviePath'] = self.view.followerMoviePathFrame.entry.get()

    #設定を書き込む
    self.model.save_settingsFile(self.settings)
    #設定ウィンドウを閉じる
    self.close()

  #reference_buttonを押したときのイベント
  def on_click_reference_button(self, type):
    #フォルダ選択ダイアログを表示
    fileType = self.model.get_file_type(type)
    self.view.show_file_dialog(type, fileType)
