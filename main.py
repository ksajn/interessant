import discord
from discord import app_commands
from discord.ext import commands

import sqlite3

import time
from colorama import Back, Fore, Style

from dotenv import load_dotenv
import asyncio
import os

from cogs import quote

intents = discord.Intents.default()
intents.message_content = True

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path = dotenv_path)
bot_token = os.getenv(key = 'BOT_TOKEN')


class Client(commands.Bot):
    def __init__(self):
        super().__init__(intents = discord.Intents().all(), command_prefix = 'interessantisthebestbot!')
    
    async def on_ready(self):
        prfx = (Back.BLACK + Fore.RED + Style.BRIGHT + time.strftime("%H:%M:%S", time.localtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(f'{prfx} logged as {self.user}')
        activity = discord.Activity(type = discord.ActivityType.playing, name = f"On {len(self.guilds)} servers | use /help to get more information" )
        await self.change_presence(activity=activity)
        try:
            synced = await bot.tree.sync()
            print(f'{prfx} synced {len(synced)} command(s)')
        except Exception as e:
            print(f"{prfx} {e}")
        try:
            db = sqlite3.connect('db.db')
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS economy(user_id INT, balance INT)")
            cursor.execute("CREATE TABLE IF NOT EXISTS nitroboost(user_id INT, role_id INT, color STR, name STR)")
            cursor.close()
            db.close()
        except Exception as e:
            print(f'Error has been found: {e}')

bot = Client()
bot.remove_command(help)
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(load())
# bot.run(bot_token)
bot.run(os.getenv(key = '2ND_TOKEN'))