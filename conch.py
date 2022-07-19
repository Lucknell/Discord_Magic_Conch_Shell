import random
import discord
import os
from discord.utils import find
from discord.ext import commands

prefix = "%" #prefix for the commands we will use ie. %help
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix)) #setting the bot to respond to the @bot or the predefined prefix

avatar_path = "/src/bot/avatar.png" #setting the path for the profile picture of the bot
fp = open(avatar_path, 'rb') #creating a file pointer for the profile picture of the bot
avatar = fp.read() #reading the profile picture file to later set the picture

@client.event
async def on_ready(): #discord.py event this is only called once when the bot is started and ready
    print('Can I have something to eat?')#a print message to make sure we have the console printing
    try:#this block is for when you are restarting the bot multiple times if you set the avatar each time you will get an exception so this is to surpress it.
        await client.user.edit(avatar=avatar)#setting the profile picture for the bot
    except discord.errors.HTTPException:#the execption you will receive for setting the profile picture too often
        pass
    
files = os.listdir("/src/bot/cogs/")#the directory where the different commands for the bot will be located. This directory will be made by docker
for f in files:#for every file in the directory we listed before 
    if f.endswith(".py"):#if the file end in .py
        client.load_extension("cogs." + f.replace(".py", ""))#load that file

client.run(os.getenv('TOKEN'))#begin the execution of the bot and get the token which will be an environment variable named TOKEN