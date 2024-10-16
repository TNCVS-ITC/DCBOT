from discord.ext import commands
from Logs import Log

class MessageResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # 指令日誌用
        self.logger = Log(bot)  # 創建 Log 實例

    @commands.Cog.listener()
    async def on_message(self, message):
        # 確保機器人不會回覆自己的消息
        if message.author == self.bot.user:
            return

        # 當訊息為 "???" 時，執行 ???
        if message.content == "遊戲":
            output = (
                "輸入以下名稱皆會有規則說明：\n"
                "1. 猜數字\n"
                "2. 目前開發中，請不要期待(X\n"
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        elif message.content == "猜數字":
            output = (
                '猜數字遊戲規則說明:\n'
                '1. 輸入 "!start_guess" 開始遊戲\n'
                '2. 輸入 "!guess 數字" 來猜數字\n'
                '3. 輸入 "!end_guess" 停止遊戲\n'
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        elif message.content == "目前開發中，請不要期待":
            output = (
                '目前開發中'
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        elif message.content == "died":
            user_to_mention = await self.bot.fetch_user(556398557997957139)
            output = (
                f"人活著的時候，死掉的機率為100%\n謝謝{user_to_mention.mention}提供此想法。"
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        elif message.content == "hello" or message.content == "hi" or message.content == "嗨":
            output = (
                '⣠⠛⠛⣄⣠⠶⠛⠛⠛⠶⣄⣠⠛⠛⣄'
                '⢿　 ⠋　　　　 　⠙　 ⡿'
                '　⣾　●　ᴥ　●　   ⣷'
                '　  ⠻⣄　　　　   ⣠⠟'
                '　⣠⡿   哈囉你好    ⢿⣄'
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        elif message.content == "chun為何被打":
            user_to_mention = await self.bot.fetch_user(951132233949937674)
            output = (
                f'因為{user_to_mention.mention}很欠揍，所以被打了。'
            )
            await message.channel.send(output)
            # 使用新的日誌系統
            await self.logger.log_message(message, output)
        

async def setup(bot):
    await bot.add_cog(MessageResponses(bot))