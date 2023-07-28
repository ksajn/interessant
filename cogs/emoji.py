import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
import unicodedata
import aiohttp
from io import BytesIO
from functions import is_url_image
from functions import checkManageEmojis

class emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(emoji = 'paste the emoji or a link to the emoji')
    @app_commands.command(name = 'emoji', description = 'enlarges given emoji')
    async def emoji(self, interaction: discord.Interaction, emoji: str):
        try:
            if emoji.find('<:\w*:\d*>'):
                emojiId = None
                emojiname = None
                splitString = emoji.split(":")
                if len(splitString) >= 2:
                    emojiname = splitString[1]
                    emojiId = splitString[2][:-1]
                    url = f'https://cdn.discordapp.com/emojis/{emojiId}.gif'
                else:
                    splitString = emoji.split("/")
                    if len(splitString) >= 3:
                        splitString = splitString[3].split(".")
                        emojiId = splitString[0]
                        splitString = emoji.split("=")
                        emojiname = splitString[1][:-7]
                        url = f'https://cdn.discordapp.com/emojis/{emojiId}.gif'
                    elif len(emoji) == 1:
                        string = hex(ord(emoji))[2:]
                        emojiname = unicodedata.name(emoji).lower()
                        url = f'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/{string.lower()}.png'

                if emojiname == None :
                    await interaction.response.send_message("this is not a proper emoji")
                    return

                description = ""
                if emojiId != None:
                    description = f'({emojiId})'
                
                embed = discord.Embed(
                    title = 'enlarged emoji',
                    description = f'{emojiname} {description}',
                    color = 0x2b2d31
                )
                if is_url_image(url):
                    embed.set_image(url = url)
                elif is_url_image(f'https://cdn.discordapp.com/emojis/{emojiId}.png'):
                    url = f'https://cdn.discordapp.com/emojis/{emojiId}.png'
                    embed.set_image(url = url)
                else:
                    await interaction.response.send_message(content = "this is not a proper emoji")
                    return

                async def buttonCallback(interaction):
                    if checkManageEmojis:
                        async with aiohttp.ClientSession() as ses:
                            async with ses.get(url) as r:
                                
                                try:
                                    img_or_gif = BytesIO(await r.read())
                                    b_value = img_or_gif.getvalue()
                                    if r.status in range(200, 299):
                                        emoji = await interaction.guild.create_custom_emoji(image = b_value, name = emojiname)
                                        await interaction.response.send_message(content = "added the emoji", ephemeral = True)
                                        await ses.close()
                                    else:
                                        await interaction.response.send_message(content = "an erorr occured when trying to add this emoji", ephemeral = True)
                                        await ses.close()
                                        
                                except discord.HTTPException:
                                    ses.close()
                                    await interaction.response.send_message(content = "emoji's file size is too big", ephemeral = True)

                    else:
                        await interaction.response.send_message(content = "you don't have the manage emojis permission")
                
                button = Button(label = "steal emoji", style = discord.ButtonStyle.grey, emoji = "🕵️")
                button.callback = buttonCallback
                view = View()
                view.add_item(button)
                
                await interaction.response.send_message(embed = embed, view = view)

        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(emoji(bot))