import discord
import requests
from discord import app_commands
from discord.ext import commands

def checkKickPermission(member: discord.Member):
       if member.guild_permissions.kick_members and member != None:
            return True
       else:
            return False

def checkBanPermission(member: discord.Member):
       if member.guild_permissions.ban_members and member != None:
            return True
       else:
            return False
       
def checkChannelManagePermission(member: discord.Member):
       if member.guild_permissions.manage_channels and member != None:
            return True
       else:
            return False
       
def checkManageMessages(member: discord.Member):
     if member.guild_permissions.manage_messages and member != None:
          return True
     else:
          return False
     

def is_url_image(image_url):
     try:
          image_formats = ("image/png", "image/gif", "image/jpeg", "image/jpg", "image/webp")
          r = requests.head(image_url)
          if r.headers["content-type"] in image_formats:
               return True
     except Exception as e:
          print(e)
     return False

def checkManageEmojis(member: discord.Member):
       if member.guild_permissions.manage_emojis and member != None:
            return True
       else:
            return False

def embedColor():
     return 0x2b2d31