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
