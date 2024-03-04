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
  def get_liveData(self):
    return self.model.get_liveData()
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
    #settingsの初期化
    self.model.initialize_settings()

    #liveURLを保存する
    liveURL = self.view.get_liveURL()
    self.model.save_liveURL(liveURL)

    #filePathSettingFrameの値を保存する
    filePathsSettingFrames = self.view.filePathsSettingsFrame.filePathsSettingFrames
    for filePathsSettingFrame in filePathsSettingFrames:
      try :
        self.save_filePath(filePathsSettingFrame)
      except:
        return

    #settingsを保存する
    self.model.store_settingsFile()

    #設定ウィンドウを閉じる
    self.close()

  #reference_buttonを押したときのイベント
  def on_click_reference_button(self, pathFrame, key):
    #フォルダ選択ダイアログを表示
    fileTypes = self.get_file_type(key)
    self.view.show_file_dialog(pathFrame, fileTypes)

  #addtivePathFrameButtonを押したときのイベント
  def on_click_addtive_path_frame_button(self):
    self.view.set_scrollregion()

  #fileTypesを取得
  def get_file_type(self, key):
    return self.model.get_file_type(key)
  
  #FilePathを保存する
  def save_filePath(self, filePathsSettingFrame):
    #keyを取得
    key = filePathsSettingFrame.key
    #pathsを取得
    pathFrames = filePathsSettingFrame.paths

    for pathFrame in pathFrames:
      #pathFrameのエラーチェック
      if pathFrame.is_Error(): 
        #エラーを発生させる
        raise Exception('NullErrorが発生しました')
      #pathを取得
      path = pathFrame.get_path()
      #probabilityを取得
      probability = pathFrame.get_probability()
      #volumeを取得
      volume = pathFrame.get_volume()
      #filePathを保存する
      self.model.save_filePath(key, path, probability, volume)

    print(f"settings: {self.model.settings}")
