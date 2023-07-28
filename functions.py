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


# spotify


from dotenv import load_dotenv
import base64
import os
import json
from requests import post, get

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path = dotenv_path)

client_id = os.getenv(key = 'CLIENT_ID')
client_secret = os.getenv(key = 'CLIENT_SECRET')


def get_token():
     auth_string = client_id + ":" + client_secret
     auth_bytes = auth_string.encode("utf-8")
     auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

     url = "https://accounts.spotify.com/api/token"
     headers = {
          "Authorization": "Basic " + auth_base64,
          "Content-Type": "application/x-www-form-urlencoded"
     }
     data = {"grant_type": "client_credentials"}
     result = post(url, headers=headers, data=data)
     json_result = json.loads(result.content)
     token = json_result["access_token"]
     return token

def get_auth_header(token):
     return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
     url = "https://api.spotify.com/v1/search"
     headers = get_auth_header(token)
     query = f"?q={artist_name}&type=artist&limit=1"

     query_url = url + query
     result = get(query_url, headers=headers)
     json_result = json.loads(result.content)["artists"]["items"]
     if len(json_result) == 0:
          print("No artist with tis name exists")
          return None

     return json_result[0]

def get_albums_by_artist(token, artist_id):
     url = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
     headers = get_auth_header(token)
     result = get(url, headers = headers)
     json_result = json.loads(result.content)['items']
     return json_result


def get_songs_by_artist(token, artist_id):
     url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
     headers = get_auth_header(token)
     result = get(url, headers=headers)
     json_result = json.loads(result.content)["tracks"]
     return json_result

token = get_token()
result = search_for_artist(token, "ACDC")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)