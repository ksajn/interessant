import discord
from discord import app_commands
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description = 'sends basic info about the bot and the command list')
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = 'interessant.', 
            description = 'interessant is a multi-purpose bot with many unique features', # useless,
            color = 0x2b2d31
        )
        
        embed.add_field(name = 'prefix:', value = 'bot only uses slash commands')
        embed.add_field(name = 'general commands:', value = '`help`, `ping`, `say`, `serverinfo`, `whoami`')
        interaction.response.send(embed = embed)

async def setup(bot):
    await bot.add_cog(help(bot))