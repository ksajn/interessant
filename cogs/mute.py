import discord
from discord import app_commands
from discord.ext import commands
import datetime
from functions import checkManageMessages, embedColor

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.describe(member = 'select a user to mute', time = 'mute duration in seconds')
    @app_commands.command(name='mute', description = 'mute chosen member')
    async def mute(self, interaction: discord.Interaction, member: discord.Member, time: int):
        if checkManageMessages(interaction.guild.get_member(interaction.user.id)) == True:
            try:
                newtime = datetime.timedelta(seconds=int(time))
                await member.edit(timed_out_until = discord.utils.utcnow() + newtime)
                embed = discord.Embed(
                    title = "interessant.",
                    color = embedColor(),
                    description = f"user {member} has been timeouted for {time}s"
                )

                await interaction.response.send_message(embed = embed)
            except Exception as e:
                print(e)
        else:
            embed=discord.Embed(
                title='interessant.',
                color=embedColor(),
                description='you dont have enough permissions to mute members'
            )

            await interaction.response.send_message(embed=embed)
            

async def setup(bot):
    await bot.add_cog(mute(bot))