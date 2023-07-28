import discord
from discord import app_commands
from discord.ext import commands
import sqlite3
class balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='balance', description = 'check your balance')
    async def balance(self, interaction: discord.Interaction):
        db = sqlite3.connect('db.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT balance FROM economy WHERE user_id = {interaction.user.id}')
        balance = cursor.fetchone()

        cursor.close()
        db.commit()
        db.close()

        embed = discord.Embed(
            title='interessant',
            description=f'your balance is **{balance[0]}**$',
            color = 0x2b2d31
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(balance(bot))