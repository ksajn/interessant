import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from typing import Optional

class ship(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(member1 = 'a member to ship you with', member2 = 'the member to be shipped with the first one (optional)')
    @app_commands.command(name='ship', description = 'ships two specified users, or you with a specified user')
    async def ship(self, interaction: discord.Interaction, member1: discord.Member, member2: Optional[discord.Member] = None,):
        if member2 == None:
            member2 = interaction.user

        name1 = member1.name[:len(member1.name)//2]
        name2 = member2.name[len(member2.name)//2:len(member2.name)]
        
        description = ""
        percentage = randint(1,100)
        if percentage < 25:
            description = f'Your love might not be that strong... but it {percentage}% is still better than 0%, right?\nYou two could still be called {name1 + name2}!'
        elif percentage < 50:
            description = f'Your love is not that weak actually!\nYou two should be called {name1 + name2} for sure!'
        elif percentage < 75:
            description = f'Woah, your love is quite strong!\nYou two should be called {name1 + name2} for sure!'
        elif percentage < 100:
            description = f'You two are litereally made for each other!\nYou two should be called {name1 + name2} for sure!'
        else:
            description = f"100%?! I've never seen such strong love!\nYou two should be called {name1 + name2} for sure!"

        embed = discord.Embed(
            title = f"Percentage of love between you is... {percentage}%",
            description = description,
            color=0x2b2d31
        )
        await interaction.response.send_message(embed = embed)
        
async def setup(bot):
    await bot.add_cog(ship(bot))