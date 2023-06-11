import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'help', description = 'sends basic info about the bot and the command list')
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title = 'interessant.', 
            description = 'interessant is a multi-purpose bot with many unique features', # useless,
            color = 0x2b2d31
        )
        button = Button(label = "invite interessant", url = "https://discord.com/api/oauth2/authorize?client_id=1112338579461525504&permissions=8&scope=bot%20applications.commands", style = discord.ButtonStyle.grey)
        button2 = Button(label = "github", url = "https://github.com/ksajn/interessant", style = discord.ButtonStyle.grey)
        view = View()
        view.add_item(button)
        view.add_item(button2)

        
        embed.add_field(name = 'bot authors:', value = '<@335790974091526144>, <@823830926575927326>', inline = False)
        embed.add_field(name = 'prefix:', value = 'bot only uses slash commands', inline = False)
        embed.add_field(name = 'general commands:', value = '`help`, `say`, `serverinfo`, `whoami`')
        embed.add_field(name = 'moderation commands:', value = '`ban`, `kick`, `mute`, `unmute`, `clear`')
        embed.add_field(name = 'fun commands:', value = '`8ball`, `cat`, `dog`')
        embed.add_field(name = 'utility commands:', value = '`ping`, `invite`, `poll`, `emoji`')
        await interaction.response.send_message(embed = embed, view = view)

async def setup(bot):
    await bot.add_cog(help(bot))