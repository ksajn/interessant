import discord
from discord import app_commands
from discord.ext import commands
from functions import embedColor

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(
            choice = "choose a activity type",
            action = "status action"
    )
    @app_commands.choices(
        choice = [
            discord.app_commands.Choice(name = 'playing', value = 1),
            discord.app_commands.Choice(name = 'listening', value = 2),
            discord.app_commands.Choice(name = 'watching', value = 3),
        ]
    )
    @app_commands.command(name='status', description = 'changes bot status')
    async def status(self, interaction: discord.Interaction, choice: int, action: str):
        if interaction.user.id == 823830926575927326 or 335790974091526144:
            if choice == 1:
                activity = discord.Activity(type = discord.ActivityType.playing, name = action)
            elif choice == 2:
                activity = discord.Activity(type = discord.ActivityType.listening, name = action)
            elif choice == 3:
                activity = discord.Activity(type = discord.ActivityType.watching, name = action)

            embed = discord.Embed(
                title='interessant',
                description='bot status has been succesfully changed',
                color = embedColor()
            )
            await self.bot.change_presence(activity = activity)
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(
                title='interessant',
                description='you dont have enough permissions',
                color = embedColor()
            )
            await interaction.response.send_message(embed=embed)
        

        
async def setup(bot):
    await bot.add_cog(status(bot))