import discord
from discord import app_commands
from discord.ext import commands

class sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='sync', description = 'sync bot commands')
    async def sync(self, interaction: discord.Interaction):
        try:
            synced = await self.bot.tree.sync()
            await interaction.response.send_message(f'synced {len(synced)} command(s)')
        except Exception as e:
            print(f"{e}")

async def setup(bot):
    await bot.add_cog(sync(bot))