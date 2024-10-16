import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

from Logs import Log

class Announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # 設定區 - 權限
        # 帳號 ID : kkallen, kkallen1
        self.can_use_command_person_id = ['719877612373016717', '1013772814978928730']
        # 身分組ID : 網管, 第一屆幹部
        self.can_use_command_role_id = ['1275817313844723884', '1276233421592461503']
        
        # 指令日誌用
        self.logger = Log(bot)  # 創建 Log 實例

    """ 指令介紹
    none: 指令名稱
    channel_id: 頻道ID
    person_id: 人/身分組的ID(可同時@多人，以" "分隔)
    txt1: 自訂文字(@user的前面)
    txt2: 自訂文字(@user的後面)
    """
    # 公告 - 特定的人/身分組才能使用此指令
    @app_commands.command(name="announce", description="發送官方公告")
    async def announce(self, interaction: discord.Interaction, output_channel_id: Optional[str], person_ids: Optional[str], txt1: Optional[str] = None, txt2: Optional[str] = None, use_markdown: bool = False):

        # 獲取使用者的身分組 ID，並排除 everyone 身分組
        role_ids = [role.id for role in interaction.user.roles if role.id != interaction.guild.id]
        # 判斷使用者是否有權限使用此指令
        user_id = str(interaction.user.id)
        if user_id in self.can_use_command_person_id:
            pass
        elif any(int(role_id) in self.can_use_command_role_id for role_id in role_ids):
            pass
        else:
            await interaction.response.send_message("你沒有權限使用此指令！", ephemeral=True)
            return

        # 若無輸入則以目前的頻道 & 自己為主
        if output_channel_id == None:
            output_channel_id = interaction.channel_id
        # 獲取指定的頻道(output_channel_id)
        output_channel = self.bot.get_channel(int(output_channel_id))
        # 檢查頻道是否存在
        if output_channel is None:
            output = "無效的頻道 ID！"
            await interaction.response.send_message(output, ephemeral=True)
            return

        # 處理多個用戶 ID
        user_mentions = []
        if person_ids:
            for user_id in person_ids.split():
                try:
                    user = await self.bot.fetch_user(int(user_id))
                    user_mentions.append(user.mention)
                except discord.NotFound:
                    await interaction.response.send_message(f"無法找到 ID 為 {user_id} 的用戶", ephemeral=True)
                    return
                except ValueError:
                    await interaction.response.send_message(f"無效的用戶 ID: {user_id}", ephemeral=True)
                    return
        else:
            # 如果沒有指定用戶，默認為發送消息的用戶
            user_mentions = [interaction.user.mention]

        # 處理換行符和Markdown
        def process_text(text):
            if text:
                text = text.replace("\\n", "\n")
                # 預設不使用 Markdown 語法
                if not use_markdown:
                    text = discord.utils.escape_markdown(text)
            return text

        txt1 = process_text(txt1)
        txt2 = process_text(txt2)

        # 組合消息
        mentions = " ".join(user_mentions)
        output = f"{txt1 or ''} {mentions} {txt2 or ''}".strip()
        # 發送消息到指定頻道
        await output_channel.send(output)
        # 回應用戶
        await interaction.response.send_message(f"消息已發送到 {output_channel.mention}！", ephemeral=True)


        # 使用新的日誌系統
        send_channel_id = str(interaction.channel_id)
        try:
            await self.logger.log_announce(interaction, "announce", output, send_channel_id, output_channel_id, False)
        except Exception as e:
            print(f"發送日誌時出錯: {e}")


async def setup(bot):
    await bot.add_cog(Announce(bot))