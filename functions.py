import discord
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