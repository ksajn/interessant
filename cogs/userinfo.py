import discord
from discord import app_commands
from discord.ext import commands

class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(member = 'select the user you want information about')
    @app_commands.command(name='userinfo', description='sends info about selected user')
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(
            title=f'{member.name} info',
            color=0x2b2d31
        )
        
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(
            name='user id:',
            value=f'{member.id}',
            inline=False
        )
        embed.add_field(
            name='server nickname:',
            value=f'{member.nick}',
            inline=False
        )
        embed.add_field(
            name='display name:',
            value=f'{member.name}',
            inline=False
        )
        embed.add_field(
            name='created account at:',
            value=f'<t:{int(member.created_at.timestamp())}:R>',
            inline=False
        )
        embed.add_field(
            name='joined server at:',
            value=f'<t:{int(member.joined_at.timestamp())}:R>',
            inline=False
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(userinfo(bot))