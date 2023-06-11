import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

class poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(question = 'question', choice1 = 'choice 1', choice2 = 'choice 2')
    @app_commands.command(name='poll', description = 'sends a poll with specified question and choices')
    async def poll(self, interaction: discord.Interaction, question: str, choice1: str, choice2: str, choice3: Optional[str] = None, choice4: Optional[str] = None, choice5: Optional[str] = None, choice6: Optional[str] = None, choice7: Optional[str] = None, choice8: Optional[str] = None, choice9: Optional[str] = None, choice10: Optional[str] = None):
        choices = [choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10]
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        desc = ""
        numb = -1
        for v in choices:
            if v != None:
                numb += 1
                desc = f"{desc}\n\n {emojis[numb]} {v}"
        embed = discord.Embed(
            title = question, 
            description = desc,
            color = 0x2b2d31
        )
        message = await interaction.channel.send(embed = embed)
        await interaction.response.send_message("successfully created a poll", ephemeral = True)
        if message:
                numb = -1
                for v in choices:
                    if v != None:
                        numb += 1
                        await message.add_reaction(emojis[numb])

async def setup(bot):
    await bot.add_cog(poll(bot))