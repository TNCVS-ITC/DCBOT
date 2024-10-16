import discord
from discord import app_commands
from discord.ext import commands
import csv
import os

from Logs import Log

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.students_path = os.path.join(os.getcwd(), 'data', 'students.csv')
        self.claimed_path = os.path.join(os.getcwd(), 'data', 'claimed.csv')
        # 要給的身分組ID
        self.member_role_id = 1276215659943952394

        # 指令日誌用
        self.logger = Log(bot)  # 創建 Log 實例
        self.output = ""

    async def read_csv(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return []

    async def write_csv(self, file_path, data, fieldnames):
        try:
            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            print(f"Error writing to CSV file {file_path}: {e}")

    async def check_and_claim(self, interaction, student_id, class_name, name):
        try:
            students = await self.read_csv(self.students_path)
            claimed = await self.read_csv(self.claimed_path)
            DC_ID = str(interaction.user.id)
            
            student_exists = any(student['student_id'] == student_id and 
                student['class_name'] == class_name and 
                student['name'] == name for student in students)
            
            if not student_exists:
                self.output = f"{name}，不在名單中。"
                return self.output

            already_claimed = any(claim['student_id'] == student_id or 
                claim['DC_ID'] == DC_ID for claim in claimed)
            
            if already_claimed:
                self.output = f"{interaction.user.mention}，你已經領取過身分組或有人盜用你的學號綁定身分組了。"
                return self.output

            new_claim = {
                'student_id': student_id,
                'class_name': class_name,
                'name': name,
                'DC_ID': DC_ID
            }
            await self.write_csv(self.claimed_path, [new_claim], ['student_id', 'class_name', 'name', 'DC_ID'])

            role = interaction.guild.get_role(self.member_role_id)
            if role is None:
                self.output = "找不到指定的身分組。請聯繫管理員檢查身分組設置。"
                return self.output
            
            await interaction.user.add_roles(role)
            self.output = f"{interaction.user.mention}，成功領取身分組。"
            return self.output

        except discord.Forbidden:
            self.output = "我沒有添加角色的權限。請確保機器人有管理身分組的權限。"
            return self.output
        except discord.HTTPException:
            self.output = "添加角色失敗。請稍後再試或聯繫管理員。"
            return self.output
        except Exception as e:
            print(f"Error in check_and_claim: {e}")
            self.output = "處理請求時發生錯誤。請聯繫管理員。"
            return self.output

    @app_commands.command(
        name="tncvs_itc", 
        description="領取南商第一屆社團成員身分組。請確保輸入資訊正確，否則別想拿了(X"
    )
    @app_commands.describe(
        student_id="你的學號",
        class_name="你的班級",
        name="你的姓名"
    )
    async def tncvs_itc(self, interaction: discord.Interaction, student_id: str, class_name: str, name: str):
        await interaction.response.defer(ephemeral=True)
        result = await self.check_and_claim(interaction, student_id, class_name, name)
        await interaction.followup.send(result, ephemeral=True)

        # 使用新的日誌系統
        channel_id = interaction.channel_id
        await self.logger.log_command(interaction, "tncvs_itc", self.output, channel_id, True)

async def setup(bot):
    await bot.add_cog(RoleManagement(bot))