#ファイル構成
#CommentAcquisitionEquipmentBot.py <- current
#├ Script
#│ ├ Model
#│ │ ├ MainModel.py
#│ │ ├ SettingsModel.py
#│ ├ View
#│ │ ├ Main
#│ │ │ ├ MainView.py
#│ │ │ ├ Menubar.py
#│ │ ├ Settings
#│ │ │ ├ SettingsView.py
#│ ├ MainController.py
#│ ├ SettingsController.py

from Script import SplashController
from Script import MainController

#MainControllerに処理を移譲
if __name__ == '__main__':
    SplashController.SplashController()
    #MainController.MainController()
