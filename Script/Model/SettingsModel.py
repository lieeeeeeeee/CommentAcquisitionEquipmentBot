import os
import json

"""
sampleSettingsJson = {
    "liveURL": "https://www.xxx.com/sample",
    "filePaths": {
        "commentSoundPath": [
            {"path": "C:\\sample.mp3", "probability": 29},
        ],
        "commentMoviePath": [
            {"path": "C:\\sample.mp4", "probability": 29},
        ], str
        "followerSoundPath": [
            {"path": "C:\\sample.mp3", "probability": 29},
        ],
        "followerMoviePath": [
            {"path": "C:\\sample.mp4", "probability": 29},
        ]
    }
}
"""
#設定ウィンドウのモデル
class SettingsModel:
    stringValue = ""
    stringKey = stringValue.__class__.__name__
    boolValue = False
    boolKey = boolValue.__class__.__name__
    intValue = 0
    intKey = intValue.__class__.__name__
    floatValue = 0.0
    floatKey = floatValue.__class__.__name__
    listValue = []
    listKey = listValue.__class__.__name__
    dictValue = {}
    dictKey = dictValue.__class__.__name__


    settingsFilePath = "DataBase/settings.json"
    
    settingsJsonContents = [
        {"key": "liveURL", "type": stringKey},
        {"key": "filePaths", "type": dictKey, "contents": [
            {"key": "commentSoundPath", "type": listKey, "contents": [
                {"key": "path", "type": stringKey},
                {"key": "probability", "type": floatKey},
                {"key": "volume", "type": intKey}
            ]},
            {"key": "commentMoviePath", "type": listKey, "contents": [
                {"key": "path", "type": stringKey},
                {"key": "probability", "type": floatKey},
                {"key": "volume", "type": intKey}
            ]},
            {"key": "followerSoundPath", "type": listKey, "contents": [
                {"key": "path", "type": stringKey},
                {"key": "probability", "type": floatKey},
                {"key": "volume", "type": intKey}
            ]},
            {"key": "followerMoviePath", "type": listKey, "contents": [
                {"key": "path", "type": stringKey},
                {"key": "probability", "type": floatKey},
                {"key": "volume", "type": intKey}
            ]}
        ]}
    ]

    def __init__(self):
        self.defaultSettingJson = self.initialize_defaultSettings(self.settingsJsonContents)
        self.settings = self.load_settingsFile()


    #defaultSettingsJsonを設定する
    def initialize_defaultSettings(self, contents):
        settingsJson = {}
        for content in contents:
            if content['type'] == self.stringKey:
                settingsJson[content['key']] = ""
            elif content['type'] == self.boolKey:
                settingsJson[content['key']] = False
            elif content['type'] == self.intKey:
                settingsJson[content['key']] = 0
            elif content['type'] == self.floatKey:
                settingsJson[content['key']] = 0.0
            elif content['type'] == self.listKey:
                settingsJson[content['key']] = []
            elif content['type'] == self.dictKey:
                settingsJson[content['key']] = self.initialize_defaultSettings(content["contents"])
                
        return settingsJson

    #filePathKeyを取得する
    def get_filePathKey(self):
        filePathKeys = []
        for parentContent in self.settingsJsonContents:
            if parentContent['key'] != "filePaths": continue
            for childContent in parentContent["contents"]:
                filePathKeys.append(childContent['key'])
        return filePathKeys
    
    #ファイルタイプを取得
    def get_file_type(self, key):
        filePathKeys = self.get_filePathKey()
        if key == filePathKeys[0]: #commentSoundPath
            fileType = [('MP3', '*.mp3')]
        elif key == filePathKeys[1]: #commentMoviePath
            fileType = [('MP4', '*.mp4')]
        elif key == filePathKeys[2]: #followerSoundPath
            fileType = [('MP3', '*.mp3')]
        elif key == filePathKeys[3]: #followerMoviePath
            fileType = [('MP4', '*.mp4')]
        else:
            fileType = []
        return fileType
    
    def get_file_path_setting_frame_title(self, key):
        filePathKeys = self.get_filePathKey()
        if key == filePathKeys[0]:
            title = "コメント取得時の効果音(mp3)"
        elif key == filePathKeys[1]:
            title = "コメント取得時の演出(mp4)"
        elif key == filePathKeys[2]:
            title = "フォロワー取得時の効果音(mp3)"
        elif key == filePathKeys[3]:
            title = "フォロワー取得時の演出(mp4)"
        else:
            title = ""
        return title

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

    #settings.jsonの型をチェックする
    def check_settingsFile(self, settings):
        tempSettings = settings.copy()

        #settingsのkeyをチェックする
        for content in settings:
            #defaultSettingJsonにkeyがないとき
            if content not in self.defaultSettingJson:
                tempSettings.pop(content)
                continue

        #settingsの型をチェックする
        for content in self.settingsJsonContents:
            #settingsにkeyがないとき
            if content['key'] not in tempSettings:
                tempSettings[content['key']] = self.defaultSettingJson[content['key']]
                continue

            #settingsにkeyがあるとき
            #settingsの型が一致しないとき
            if content['type'] != tempSettings[content['key']].__class__.__name__:
                tempSettings[content['key']] = self.defaultSettingJson[content['key']]
                continue

            #settingsの型が一致するとき
            #settingsの型がdictのとき
            if content['type'] == self.dictKey:
                tempSettings[content['key']] = self.check_settingsFile(tempSettings[content['key']])
                continue

        print(f"settings: {tempSettings}")
        return tempSettings

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
    
    #liveURLを取得する
    def get_liveURL(self):
        #liveURLを取得する
        liveURL = self.settings['liveURL']
        return liveURL
    
    #FilePathsを取得する
    def get_filePaths(self):
        #FilePathsを取得する
        FilePaths = self.settings['filePaths']
        return FilePaths
