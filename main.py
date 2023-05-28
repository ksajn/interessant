import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path = dotenv_path)
bot_token = os.getenv(key = 'BOT_TOKEN')


class Client(commands.Bot):
    def __init__(self):
        super().__init__(intents = discord.Intents().all(), command_prefix='!')

    async def on_ready(self):
        print(f'logged as {self.user}')
        try:
            synced = await bot.tree.sync()
            print(f'synced {len(synced)} command(s)')
        except Exception as e:
            print(e)

bot = Client()
bot.remove_command(help)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(load())
bot.run(bot_token)