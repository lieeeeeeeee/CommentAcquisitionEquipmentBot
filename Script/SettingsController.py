from Script.Model import SettingsModel
from Script.View.Settings import SettingsView

#設定ウィンドウのコントローラー
class SettingsController:

  def __init__(self, root=None):
    self.root = root
    #設定ウィンドウのモデルを作成
    self.model = SettingsModel.SettingsModel()
    self.is_open = False

  def open(self):
    if self.is_open: return
    self.is_open = True

    #設定ウィンドウを作成
    self.view = SettingsView.SettingsView(self)
    #windowを削除したときのイベント
    self.view.protocol('WM_DELETE_WINDOW', self.close)

    #設定ウィンドウを表示
    self.view.mainloop()

  #closeボタンを押したときのイベント
  def close(self):
    #設定ウィンドウを閉じる
    self.is_open = False
    self.view.close()
  
  #settingsを保存する
  def save_settings(self, settings):
    return self.model.save_settingsFile(settings)

  #settingsを取得
  def get_settings(self):
    return self.model.settings
  #accountIDを取得
  def get_accountID(self):
    return self.model.get_accountID()
  #liveURLを取得
  def get_liveURL(self):
    return self.model.get_liveURL()
  #filePathsを取得
  def get_filePaths(self):
    return self.model.get_filePaths()
  #filePathsのtypeを取得
  def get_file_type(self, key):
    return self.model.get_file_type(key)
  #filePathSettingFrameTitleを取得
  def get_file_path_setting_frame_title(self, key):
    return self.model.get_file_path_setting_frame_title(key)

  #キャンセルボタンを押したときのイベント
  def on_click_cancel_button(self):
    #設定ウィンドウを閉じる
    self.close()

  #保存ボタンを押したときのイベント
  def on_click_save_button(self):
    print("保存ボタンを押したときのイベントを改修する")
    return
    #設定を取得
    self.settings['liveURL'] = self.view.liveUrlEntry.get()
    self.settings['commentMoviePath'] = {
      "path": self.view.commentMoviePathFrame.pathEntry.get(),
      "probability": self.view.commentMoviePathFrame.probabilityEntry.get()
    }
    self.settings['commentSoundPath'] = {
      "path": self.view.commentSoundPathFrame.pathEntry.get(),
      "probability": self.view.commentSoundPathFrame.probabilityEntry.get()
    }
    self.settings['followerMoviePath'] = {
      "path": self.view.followerMoviePathFrame.pathEntry.get(),
      "probability": self.view.followerMoviePathFrame.probabilityEntry.get()
    }
    self.settings['followerSoundPath'] = {
      "path": self.view.followerSoundPathFrame.pathEntry.get(),
      "probability": self.view.followerSoundPathFrame.probabilityEntry.get()
    }

    #設定を書き込む
    self.model.save_settingsFile(self.settings)
    #設定ウィンドウを閉じる
    self.close()

  #reference_buttonを押したときのイベント
  def on_click_reference_button(self, key, index):
    print("reference_buttonを押したときのイベントを改修する")
    return
    #フォルダ選択ダイアログを表示
    fileType = self.model.get_file_type(type)
    self.view.show_file_dialog(type, fileType)

  #addtivePathFrameButtonを押したときのイベント
  def on_click_addtive_path_frame_button(self):
    self.view.set_scrollregion()

