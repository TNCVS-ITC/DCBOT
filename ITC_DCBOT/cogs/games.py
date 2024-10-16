from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game_start = False

        # 猜數字
        self.guess_num = None


    # 猜數字，1~100 之間的數字
    @commands.command()
    async def guess(self, ctx, num: int):
        if not self.game_start:
            await ctx.send('遊戲尚未開始，請輸入 "!StartGuess" 來開始遊戲。')
            return
        
        # 判斷區
        if num < 1 or num > 100:
            await ctx.send('請輸入一個介於 1 到 100 之間的數字。')
            return
        
        if num == self.guess_num:
            await ctx.send('恭喜！你猜對了！可惜沒獎勵(?')
            self.game_start = False
        elif num < self.guess_num:
            await ctx.send('數字太小，請再接再厲。')
        else:
            await ctx.send('數字太大，請再接再厲。')
    # 開始猜數字遊戲
    @commands.command()
    async def start_guess(self, ctx):
        if self.game_start:
            print('已經有一個遊戲在進行中，請先完成它。')
            return
        
        self.game_start = True
        self.guess_num = random.randint(1, 100)
        await ctx.send('遊戲開始！請猜數字！')
    # 結束猜數字遊戲
    @commands.command()
    async def end_guess(self, ctx):
        if not self.game_start:
            await ctx.send('遊戲尚未開始，請輸入 !StartGuess 來開始遊戲。')
            return
        
        await ctx.send(f'遊戲結束。正確的數字是 {self.guess_num}。')
        self.game_start = False

async def setup(bot):
    await bot.add_cog(Games(bot))
