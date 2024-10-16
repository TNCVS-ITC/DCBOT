import discord
from discord import app_commands
from discord.ext import commands

from Logs import Log

class InfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # 指令日誌用
        self.logger = Log(bot)  # 創建 Log 實例

    @app_commands.command(name="info", description="顯示相關信息")
    @app_commands.describe(
        target="選擇要顯示的信息類型",
        user="選擇要顯示信息的用戶（如果選擇用戶類型）"
    )
    
    # 輸入info時，可選擇的選項
    @app_commands.choices(target=[
        app_commands.Choice(name="伺服器", value="server"),
        app_commands.Choice(name="用戶", value="user"),
        app_commands.Choice(name="Bot info", value="Bot_info")
    ])
    async def info(self, interaction: discord.Interaction, target: str, user: discord.User = None):
        
        # 伺服器
        if target == "server":
            server = interaction.guild
            info_message = f"伺服器名稱: {server.name}\n"
            info_message += f"成員數量: {server.member_count}\n"
            info_message += f"我們是南商資訊研究社的官方Discord伺服器。"
            
            # 使用新的日誌系統
            channel_id = interaction.channel_id
            await self.logger.log_command(interaction, "info server", info_message, channel_id, True)
        # 用戶
        elif target == "user":
            if user is None:
                user = interaction.user
            info_message = f"用戶名稱: {user.name}\n"
            info_message += f"用戶ID: {user.id}\n"
            info_message += f"帳號創建時間: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            info_message += f"加入伺服器時間: {user.joined_at.strftime('%Y-%m-%d %H:%M:%S')}"

            # 使用新的日誌系統
            channel_id = interaction.channel_id
            await self.logger.log_command(interaction, "info user", info_message, channel_id, True)
        # Bot info
        elif target == "Bot_info":
            info_message = f"機器人: {self.bot.user.name}\n"
            info_message += f"版本: 2.4.0\n"
            info_message += f"製作人: Oscar, kkallen\n"
            info_message += f"語言: Python\n"
            info_message += f"若有任何相關的想法，請聯繫 Oscar 或 kkallen。\n"

            # 使用新的日誌系統
            channel_id = interaction.channel_id
            await self.logger.log_command(interaction, "info Bot_info", info_message, channel_id, True)
        # 沒有選任何選項
        else:
            info_message = "請選擇任何一個選項，不然就不要問(X"

            # 使用新的日誌系統
            channel_id = interaction.channel_id
            await self.logger.log_command(interaction, "info none", info_message, channel_id, True)

        await interaction.response.send_message(info_message, ephemeral=True)

    # 其他指令
    @app_commands.command(name="hello", description="機器人會向你問好")
    async def hello(self, interaction: discord.Interaction, ephemeral: bool = True):
        output = f"你好，{interaction.user.mention}！很高興見到你！"
        await interaction.response.send_message(output, ephemeral=ephemeral)
        # 使用新的日誌系統
        channel_id = interaction.channel_id
        await self.logger.log_command(interaction, "hello", output, channel_id, ephemeral)

""" 測試01
    # 看自己有甚麼身分組(ID)
    @app_commands.command(name="test", description="see your role_id")
    async def test_command(self, interaction: discord.Interaction):
        # 確保互動來自服務器，而非個人群組或聊天室
        if not interaction.guild:
            await interaction.response.send_message("這個命令只能在伺服器中使用。", ephemeral=True)
            return

        # 獲取使用者的身分組 ID，並排除 everyone 身分組
        role_ids = [role.id for role in interaction.user.roles if role.id != interaction.guild.id]
        # 將身分組 ID 轉換為字符串，並用逗號分隔
        all_roles = ", ".join(map(str, role_ids))

        if role_ids:
            all_roles = ", ".join(map(str, role_ids))
            message = f"您擁有的身分組 ID 是（不包括 everyone 身分組）: {all_roles}"
        else:
            message = "您沒有任何身分組（除了 everyone 身分組）。"
        await interaction.response.send_message(message)
"""

async def setup(bot):
    await bot.add_cog(InfoCommands(bot))