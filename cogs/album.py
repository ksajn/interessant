import discord
import json
from functions import get_token, get_songs_by_artist, search_for_artist, get_albums_by_artist
from discord import app_commands
from discord.ext import commands

class albums(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(artist = 'specify spotify aritst')
    @app_commands.command(name='albums', description='sends all artist albums')
    async def albums(self, interaction: discord.Interaction, artist: str):
        
        
        token = get_token()
        result = search_for_artist(token, artist)
        artist_id = result["id"]
        songs  = get_albums_by_artist(token, artist_id)
        
        
        artist_name = result['name']
        artist_followers = result['followers']['total']
        artist_avatar = result['images'][0]['url']



        embed=discord.Embed(
                    color=0x2b2d31,
                    title=f'{artist_name.lower()} albums:'
                )    
    
        embed.set_thumbnail(url=artist_avatar)

        for idx, song in enumerate(songs):
            embed.add_field(
                name=(f"{idx + 1}."),
                value=(f"**{song['name']}**"),
                inline=True,
                )
    
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(albums(bot))