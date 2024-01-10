import os
import json

#設定ウィンドウのモデル
class SettingsModel:
    settingsFilePath = "DataBase/settings.json"
    settingsJsonKey = [
    "liveURL", "commentSoundPath", "commentMoviePath", "followerSoundPath", "followerMoviePath"
    ]

    def __init__(self):
        self.settings = None
        self.defaultSettingJson = {}

        for key in self.settingsJsonKey:
            self.defaultSettingJson[key] = ""


    #ファイルタイプを取得
    def get_file_type(self, type):
        if type == self.settingsJsonKey[1]:
            fileType = [('MP3', '*.mp3')]
        elif type == self.settingsJsonKey[2]:
            fileType = [('MP4', '*.mp4')]
        elif type == self.settingsJsonKey[3]:
            fileType = [('MP3', '*.mp3')]
        elif type == self.settingsJsonKey[4]:
            fileType = [('MP4', '*.mp4')]
        else:
            fileType = []
        return fileType

    #settings.jsonをロードする
    def load_settingsFile(self):
        #settings.jsonが存在しないとき
        if not os.path.exists(self.settingsFilePath):
            #settings.jsonを作成する
            with open(self.settingsFilePath, 'w') as f:
                json.dump(self.defaultSettingJson, f, indent=4)
                return self.defaultSettingJson
        #settings.jsonが存在するとき
        else:
            #settings.jsonを読み込む
            try:
                with open(self.settingsFilePath, 'r') as f:
                    settings = json.load(f)
                    settings = self.check_settingsFile(settings)
                    return settings
            except Exception as e:
                print(f"エラーが発生しました: {e}")
                return self.defaultSettingJson

    #settings.jsonをロードするのKeyをチェックする
    def check_settingsFile(self, settings):
        for key in self.settingsJsonKey:
            if key not in settings:
                settings[key] = ""
        return settings

    #settings.jsonを保存する
    def save_settingsFile(self, settings):
        #settings.jsonを保存する
        try:
            with open(self.settingsFilePath, 'w') as f:
                json.dump(settings, f, indent=4)
                return True
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return False

    #liveURLからaccountIDを取得する
    def get_accountID(self):
        #settings.jsonをロードする
        settings = self.load_settingsFile()
        #liveURLを取得する
        liveURL = settings['liveURL']
        #liveURLが空のとき
        if liveURL == "":
            return ""
        #liveURLが空でないとき
        else:
            #liveURLからaccountIDを取得する
            return liveURL.split('/')[-1]
