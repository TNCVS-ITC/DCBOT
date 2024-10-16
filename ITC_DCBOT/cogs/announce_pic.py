import discord
from discord import app_commands
from discord.ext import commands
import datetime
from typing import Optional

from Logs import Log

class AnnouncePic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = Log(bot)  # 初始化日誌記錄器

    @app_commands.command(name="公告", description="發送一個公告(附圖)")
    async def announce(self, interaction: discord.Interaction, title: str, content: str, time: Optional[str]= None, image_url_samll : Optional[str]= None, image_url_large : Optional[str]= None):
        # 創建嵌入消息
        embed = discord.Embed(title=title, color=discord.Color.from_rgb(0, 170, 255))
        
        # 添加字段
        embed.add_field(name="內容", value=content, inline=False)
        if time is None:
            pass
        else:
            embed.add_field(name="時間", value=time, inline=False)

        """
        # 設定圖片
        if image_url is None:
            # 添加主圖片
            embed.set_image(file=discord.File(r"data\pic\01.jpg"))
            # 添加縮略圖
            embed.set_thumbnail(file=discord.File(r"data\pic\01.jpg"))
        else:
        """
        if image_url_large != None:
            # 添加主圖片
            embed.set_image(url=image_url_large)
        if image_url_samll != None:
            # 添加縮略圖
            embed.set_thumbnail(url=image_url_samll)

        

        # 發送嵌入消息
        await interaction.response.send_message(embed=embed)

        # 記錄命令使用
        output_content = f"標題: {title}\n內容: {content}\n時間: {time}\n圖片URL(右上縮圖): {image_url_samll}\n圖片URL(下方大圖): {image_url_large}"
        await self.logger.log_command(interaction, "公告", output_content, str(interaction.channel_id), False)

async def setup(bot):
    await bot.add_cog(AnnouncePic(bot))