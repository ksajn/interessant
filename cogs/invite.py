import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands

class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'invite', description = "sends interessant's invite link")
    async def invite(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = 'invite interessant', 
            description = 'https://discord.com/oauth2/authorize?client_id=1112338579461525504&permissions=8&scope=bot%20applications.commands', # useless,
            color = 0x2b2d31
        )

        await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(invite(bot))
