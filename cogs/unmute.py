import discord
from discord import app_commands
from discord.ext import commands
from functions import embedColor, checkManageMessages

class unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(member = 'select a user to unmute')
    @app_commands.command(name = 'unmute', description = 'unmute chosen member')
    async def unmute(self, interaction: discord.Interaction, member: discord.Member):
        if checkManageMessages(interaction.guild.get_member(interaction.user.id)) == True:
                try:
                    await member.edit(timed_out_until = discord.utils.utcnow())
                    embed = discord.Embed(
                        title = "interessant.",
                        color = 0x2b2d31,
                        description = f"user {member} has been unmuted"
                    )

                    await interaction.response.send_message(embed = embed)
                except Exception as e:
                    print(e)
        else:
            embed=discord.Embed(
                title='interessant.',
                color=embedColor(),
                description='you dont have enough permissions to unmute members'
            )

            await interaction.response.send_message(embed=embed)





        
async def setup(bot):
    await bot.add_cog(unmute(bot))