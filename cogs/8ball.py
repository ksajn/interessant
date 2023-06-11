import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
from random import choice

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

class eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(question = 'write a question')
    @app_commands.command(name = '8ball', description = 'widac')
    async def eightball(self, interaction: discord.Interaction, question: str):
        await interaction.response.send_message(content = choice(responses))

async def setup(bot):
    await bot.add_cog(eightball(bot))