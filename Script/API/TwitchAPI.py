from twitchio import Channel, Message
from twitchio.ext import commands

class Bot(commands.Bot):
    WTITCH_ACCESS_TOKEN = "***"
    COMMAND_PREFIX = "!"

    def __init__(self, parent=None, initial_channels=None):
        super().__init__(
            token=self.WTITCH_ACCESS_TOKEN,
            prefix=self.COMMAND_PREFIX,
            initial_channels=[initial_channels]
        )
        self.parent = parent

    #チャンネルにログイン
    def run(self):
        print("ログイン中...")
        super().run()

    #チャンネルからログアウト
    async def stop(self):
        await super().close()




    #チャンネルからログアウト
    async def event_channel_left(self, channel: Channel):
        print(f"ログアウトしました。チャンネル名: {channel.name}")
        await channel.send(f"{self.nick}は逃げ出した！")

    #チャンネルにログイン
    async def event_channel_joined(self, channel: Channel):
        print(f"ログインしました。チャンネル名: {channel.name}")
        for chatter in channel.chatters:
            print(f'ユーザーID: {chatter.id}')
            print(f'ユーザー名: {chatter.name}')
            print(f'表示名: {chatter.display_name}')
        await channel.send(f"{chatter.name}があらわれた！")

    #全てのチャンネルにログイン
    async def event_ready(self):
        print("全てのチャンネルにログインしました。")
        print(f'ユーザーID: {self.user_id}')
        print(f'ユーザー名: {self.nick}')

    #チャットメッセージを受信
    async def event_message(self, message: Message):
        #botのメッセージは無視
        if message.echo: return

        #parentにメッセージを送信
        self.parent.on_receive_message(message)
