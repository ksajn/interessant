import discord
from discord import app_commands
from discord.ext import commands

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(say = 'write here what should bot say')
    @app_commands.command(name='say', description='bot says what you tell it to')
    async def say(self, interaction: discord.Interaction, say: str):
        await interaction.response.send_message(f'User {interaction.user.name} says: `{say}`')

async def setup(bot):
    await bot.add_cog(say(bot))