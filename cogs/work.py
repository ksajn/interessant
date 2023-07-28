import discord
from discord import app_commands
from discord.ext import commands
import random
import sqlite3
class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.checks.cooldown(1, 3600, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.command(name='work', description = 'work and earn money')
    async def work(self, interaction: discord.Interaction):
        try:
            money = random.randint(100, 200)

            db = sqlite3.connect('db.db')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM economy WHERE user_id = {interaction.user.id}')
            result = cursor.fetchone()
            if result == None:
                cursor.execute(f'INSERT INTO economy(user_id, balance) VALUES({interaction.user.id}, 0)')
                
            cursor.execute(f'UPDATE economy SET balance = balance + {money} WHERE user_id = {interaction.user.id}')

            cursor.execute(f'SELECT balance FROM economy WHERE user_id = {interaction.user.id}')
            balance = cursor.fetchone()

            cursor.close()
            db.commit()
            db.close()

            embed = discord.Embed(
                title='interessant',
                description=f'you earned **{money}**$',
                color=0x2b2d31
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(e)
    

async def setup(bot):
    await bot.add_cog(work(bot))