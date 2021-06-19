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
    	await bot.change_presence(activity=discord.Streaming(name="SELLING NITRO/TOKEN GEN", url=~"https://www.twitch.tv"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Streaming(name="IQ 10/10", url=~"https://www.twitch.tv"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Streaming(name="MADE BY NILA", url=~"https://www.twitch.tv"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Game(name="discord.gg/xlop", url=~"https://www.twitch.tv"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="24/7"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Game(name="PAYTM CASH"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="NILA OP"))
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
    
bot.run("NzA0ODg1NzgxOTE0ODQ1MjQ2.YDzFpA.ZVGamNEabRBev0EyQ0umxnu2o3o",bot=False)
