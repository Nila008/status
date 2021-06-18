import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import platform
import time
import colorsys
import random
prefix = "§"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print("Created by Captain Cool")
    print("Trivia Savage Pro:")
    print("https://discord.gg/cKQGjsS")
    print("Everything's all ready to go~")
    while True:
    	await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="MADE BY NILA"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="Discord.gg/xlop"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="NILA OP OR WOT"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="JOIN XL NOW 25K OP FAM"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="SELLING THIS"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="DM ME"))
    	await asyncio.sleep(5)
    	
    
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(5)

@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py 
    # Send it to the user
    await ctx.send(latency)
    
bot.run("mfa.0Aij4oZ9iF8852Yy8e96dz9pTz7lPk0AawelMMib8tYFtliPn2TEfWfme9pF_vVi2E1gD5a6Gfpdpm70PrcA",bot=False)
