import discord
from discord import app_commands
from discord.ext import commands
import requests
import json

class cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='cat', description = 'sends a random cat photo')
    async def cat(self, interaction: discord.Interaction):
        apiResponse = requests.get("https://api.thecatapi.com/v1/images/search").text
        decodedResponse = json.loads(apiResponse)
        if decodedResponse and decodedResponse[0] and decodedResponse[0]["url"]:
            embed = discord.Embed(
                title = "random cat photo",
                color=0x2b2d31
            )
            embed.set_image(url = decodedResponse[0]["url"])
            await interaction.response.send_message(embed = embed)
        
async def setup(bot):
    await bot.add_cog(cat(bot))