import discord
import datetime

class Log:
    def __init__(self, bot):
        self.bot = bot
        self.log_channel_id = 1290898809127309352  # 替換為你的日誌頻道ID

    # 公告用
    async def log_announce(self, interaction: discord.Interaction, command_name: str, output: str, send_channel_id: str, output_channel_id: str, ephemeral: bool):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if not log_channel:
            print(f"無法找到日誌頻道 (ID: {self.log_channel_id})")
            return

        send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_channel_mention = self.bot.get_channel(int(send_channel_id))
        output_channel_mention = self.bot.get_channel(int(output_channel_id))

        log_message = (
            f"輸入指令的人: {interaction.user}\n"
            f"時間: {send_time}\n"
            f"使用指令的頻道: {send_channel_mention.mention}\n"
            f"輸出頻道: {output_channel_mention.mention}\n"
            f"是否只有本人可見: {'是' if ephemeral else '否'}\n"
            f"輸入內容: /{command_name}\n"
            f"輸出內容:\n{output}\n"
        )
        
        try:
            await log_channel.send(log_message)
        except Exception as e:
            print(f"發送日誌消息時出錯: {e}")

    # /指令用
    async def log_command(self, interaction: discord.Interaction, command_name: str, output: str, send_channel_id: str, ephemeral: bool):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if not log_channel:
            print(f"無法找到日誌頻道 (ID: {self.log_channel_id})")
            return

        send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_channel_mention = self.bot.get_channel(int(send_channel_id))
        log_message = (
            f"輸入指令的人: {interaction.user}\n"
            f"時間: {send_time}\n"
            f"使用指令的頻道: {send_channel_mention.mention}\n"
            f"是否只有本人可見: {'是' if ephemeral else '否'}\n"
            f"輸入內容: /{command_name}\n"
            f"輸出內容:\n{output}\n"
        )
        
        await log_channel.send(log_message)

    # 當訊息為 "???" 時，執行 ??? 用
    async def log_message(self, message: discord.Message, output: str):
        log_channel = self.bot.get_channel(self.log_channel_id)
        if not log_channel:
            print(f"無法找到日誌頻道 (ID: {self.log_channel_id})")
            return
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = (
            f"觸發指令的人: {message.author}\n"
            f"時間: {current_time}\n"
            f"頻道: {message.channel.mention}\n"
            f"輸入內容: {message.content}\n"
            f"輸出內容:\n{output}\n"
        )
        
        await log_channel.send(log_message)


"""公告 - 範本程式碼:
from Logs import Logs

def __init__(self, bot):
    # 指令日誌用
    self.logger = Logs(bot)  # 創建 Log 實例

# 使用新的日誌系統
channel_id = interaction.channel_id
await self.logger.log_command(interaction, "指令名稱", 輸出內容, 指令輸入頻道, 指令輸出頻道, 是否只有本人可見)
"""

"""範本程式碼:
from Logs import Logs

def __init__(self, bot):
    # 指令日誌用
    self.logger = Logs(bot)  # 創建 Log 實例

# 使用新的日誌系統
channel_id = interaction.channel_id
await self.logger.log_command(interaction, "指令名稱", 輸出內容, 指令輸入頻道, 是否只有本人可見)
"""

"""範本程式碼
from Logs import Logs

def __init__(self, bot):
    # 指令日誌用
    self.logger = Logs(bot)  # 創建 Log 實例

# 使用新的日誌系統
await self.logger.log_message(message, output)
"""