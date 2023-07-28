import discord
from discord import app_commands
from discord.ext import commands
from functions import embedColor
from random import randint

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name='dice', description = 'rolls dice')
    async def dice(self, interaction: discord.Interaction):
        roll = randint(1,6)
        embed = discord.Embed(
            title='interessant',
            description=f'you threw the dice and... got {roll}',
            color=embedColor()
        )

        await interaction.response.send_message(embed=embed)
            

async def setup(bot):
    await bot.add_cog(dice(bot))