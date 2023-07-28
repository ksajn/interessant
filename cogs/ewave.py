import discord
from discord import app_commands
from discord.ext import commands


class ewave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='e_wave', description = 'e wave')
    async def ewave(self, interaction: discord.Interaction):
        await interaction.response.send_message('https://media.discordapp.net/attachments/638804174879850537/1042536903276240956/Bez_nazwy-1.gif')

async def setup(bot):
    await bot.add_cog(ewave(bot))