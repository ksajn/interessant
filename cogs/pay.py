import discord
from discord import app_commands
from discord.ext import commands
import random
import sqlite3

class pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='pay', description = 'pay someone specified amount of money')
    async def pay(self, interaction: discord.Interaction, member: discord.Member, amount: int):
        try:
            
            
            db = sqlite3.connect('db.db')
            cursor = db.cursor()
            
            cursor.execute(f'SELECT balance FROM economy WHERE user_id = {interaction.user.id}')
            balanceCheck = cursor.fetchone()
            
            if int(balanceCheck[0]) < amount:
                await interaction.response.send_message('you dont have that much money', ephermal=True)
    
            cursor.execute(f'SELECT user_id FROM economy WHERE user_id = {member.id}')
            result = cursor.fetchone()
            if result == None:
                cursor.execute(f'INSERT INTO economy(user_id, balance) VALUES({member.id}, 0)')
                
            cursor.execute(f'UPDATE economy SET balance = balance + {amount} WHERE user_id = {member.id}')


            cursor.close()
            db.commit()
            db.close()

            embed = discord.Embed(
                title='interessant',
                description=f'you have paid {member.name} {amount}$',
                color=0x2b2d31
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(pay(bot))