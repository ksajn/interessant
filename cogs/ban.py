import discord
from discord import app_commands
from discord.ext import commands
from functions import checkBanPermission

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(member = 'select a member to ban', reason = 'reason why member will be banned')
    @app_commands.command(name='ban', description = 'bans a member')
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        if checkBanPermission(interaction.guild.get_member(interaction.user.id)) == True:
            try: 
                await member.ban(reason=reason)
                await interaction.response.send_message(f"successfully banned {member.display_name}")
            except Exception as e:
                print(e)
        else:
            await interaction.response.send_message("you don't have permission to ban members!")

        
async def setup(bot):
    await bot.add_cog(ban(bot))