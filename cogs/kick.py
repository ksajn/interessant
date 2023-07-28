import discord
from discord import app_commands
from discord.ext import commands
from functions import checkKickPermission

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(member = 'select a member to kick')
    @app_commands.command(name='kick', description = 'kicks a member')
    async def kick(self, interaction: discord.Interaction, member: discord.Member):
        if checkKickPermission(interaction.guild.get_member(interaction.user.id)) == True:
            await member.kick()
            await interaction.response.send_message(f"successfully kicked {member.display_name}")
        else:
            await interaction.response.send_message("you don't have permission to kick members!")

        
async def setup(bot):
    await bot.add_cog(kick(bot))