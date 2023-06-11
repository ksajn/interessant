import discord
from discord import app_commands
from discord.ext import commands
from functions import checkManageMessages

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(amount = 'amount of messages to delete')
    @app_commands.command(name='clear', description='deletes a specified amount of messages')
    async def clear(self, interaction: discord.Interaction, amount: int):
        if checkManageMessages(interaction.guild.get_member(interaction.user.id)) == True:
            await interaction.response.send_message(f'successfully deleted {amount} messages', ephemeral = True, delete_after = 4)
            await interaction.channel.purge(limit = amount)
        else: 
            await interaction.response.send_message(f'you dont have enoguh permissions', ephemeral = True)

async def setup(bot):
    await bot.add_cog(clear(bot))