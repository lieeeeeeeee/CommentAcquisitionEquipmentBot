import random

#メインウィンドウのモデル
class MainModel:
    shortcut_keys = {
        "full_screen": {
            "name": "フルスクリーン",
            "display": "F11",
            "key": "F11",
            "state": 0
        },
        "menu_bar": {
            "name": "メニューバー",
            "display": "Ctrl + Shift + b",
            "keysym": "B",
            "state": 5
        },
        "settings": {
            "name": "設定",
            "display": "Ctrl + `",
            "keysym": "grave",
            "state": 4
        },
        "exit": {
            "name": "終了",
            "display": "Ctrl + q",
            "keysym": "q",
            "state": 4
        },
        "join": {
            "name": "参加",
            "display": "Ctrl + j",
            "keysym": "j",
            "state": 4
        },
        "leave": {
            "name": "離脱",
            "display": "Ctrl + l",
            "keysym": "l",
            "state": 4
        },
    }

    def __init__(self):
        pass

    #FilePathsからランダムにSoundDataPathを取得
    def get_random_Path(self, filePaths):
        probability = 0.0
        #0.0~100.0の範囲で乱数を生成
        randomValue = random.uniform(0.0, 100.0)
        print(f"randomValue: {randomValue}")
        #filePathsをループ
        for filePath in filePaths:
            n = probability + filePath['probability']
            #nが100.0を超えたとき
            if n > 100.0: continue
            #nがrandomValueを超えたとき
            if n > randomValue:
                #pathを返す
                return (filePath['path'], filePath['volume'])
            #probabilityにfilePath['probability']を加算
            probability = n

        #filePathsが空のときNoneを返す
        return None
        