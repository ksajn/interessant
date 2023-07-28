import discord
from discord import app_commands
from discord.ext import commands

class whoami(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe()
    @app_commands.command(name='whoami', description='sends info about command author')
    async def whoami(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=f'{interaction.user.name} info',
            color=0x2b2d31
        )

        embed.set_thumbnail(url=interaction.user.avatar)
        embed.add_field(
            name='user id:',
            value=f'{interaction.user.id}',
            inline=False
        )
        embed.add_field(
            name='server nickname:',
            value=f'{interaction.user.nick}',
            inline=False
        )
        embed.add_field(
            name='display name:',
            value=f'{interaction.user.name}',
            inline=False
        )
        embed.add_field(
            name='created account at:',
            value=f'<t:{int(interaction.user.created_at.timestamp())}:D>',
            inline=False
        )
        embed.add_field(
            name='joined server at:',
            value=f'<t:{int(interaction.user.joined_at.timestamp())}:R>',
            inline=False
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(whoami(bot))