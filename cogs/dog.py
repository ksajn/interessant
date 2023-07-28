import discord
from discord import app_commands
from discord.ext import commands
import requests
import json

class dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='dog', description = 'sends a random dog photo')
    async def dog(self, interaction: discord.Interaction):
        apiResponse = requests.get("https://api.thedogapi.com/v1/images/search").text
        decodedResponse = json.loads(apiResponse)
        if decodedResponse and decodedResponse[0] and decodedResponse[0]["url"]:
            embed = discord.Embed(
                title = "random dog photo",
                color=0x2b2d31
            )
            embed.set_image(url = decodedResponse[0]["url"])
            await interaction.response.send_message(embed = embed)
        
async def setup(bot):
    await bot.add_cog(dog(bot))