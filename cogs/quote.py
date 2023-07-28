import discord
from discord import app_commands
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path = dotenv_path)
api_ninjas_key = os.getenv(key = 'API_NINJAS_KEY')

class quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='quote', description = 'sends a random quote')
    async def quote(self, interaction: discord.Interaction):
        apiResponse = requests.get(url = "https://api.api-ninjas.com/v1/quotes", headers = {"X-Api-Key": api_ninjas_key}).text
        decodedResponse = json.loads(apiResponse)
        if decodedResponse and decodedResponse[0].get('quote'):
            embed = discord.Embed(
                title = f"{decodedResponse[0]['author']} once said:",
                description = decodedResponse[0]['quote'],
                color=0x2b2d31
            )
            await interaction.response.send_message(embed = embed)
        else:
            embed = discord.Embed(
                title = "something went wrong when trying to get a quote",
                color=0x2b2d31
            )
            await interaction.response.send_message(embed = embed)
        
async def setup(bot):
    await bot.add_cog(quote(bot))