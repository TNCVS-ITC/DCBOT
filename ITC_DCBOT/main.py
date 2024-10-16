import discord
from discord.ext import commands
import os

from dotenv import load_dotenv
# 獲取當前檔案的路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, 'config.env')
# 加載環境變量
load_dotenv(env_path)
# 從環境變亮中讀取 BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    print("BOT_TOKEN is not found in .env file.")
    exit()

# 創建一個具有所有權限的 Intents 實例
intents = discord.Intents.default()
intents.message_content = True

# 命令前綴 '%'
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as --> {bot.user}")
    await bot.tree.sync()  # 同步斜線指令

# 載入 cogs
async def load_extensions():
    # 使用相對路徑
    for filename in os.listdir("cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename[:-3]}: {e}")

async def main():
    await load_extensions()
    await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())