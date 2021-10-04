import discord
from discord.ext import commands
from colorama import Fore, Style
import random
import asyncio
import requests
import os
import json
import time
import uuid
import praw
import random
import aiohttp





def cls():
    os.system('cls' if os.name=='nt' else 'clear')





with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
randnumbers = config.get('numbers')


snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
bot = commands.Bot(command_prefix="!",self_bot=True)

@bot.event
async def on_connect():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your mothers Bedroom nigga "))


@bot.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None





@bot.listen()
async def on_message(message):
  if message.content == ('!xd'):
    await message.channel.send(uuid.uuid4())
    time.sleep(4)
    await bot.process_commands(message) 
    
  elif message.content == ('!help'):
    embed = discord.Embed(description=f''' !xd - sends a random number and some other tings \n!gayrate - tells u how gay u are faggot\n!av - sends ur avatar\n!snipe - sends the last deleted message xd \n!dog - sends a dog pic ''', color=3092790)
    embed.set_author(name= f"Help Page (by mert)")
    await message.channel.send(embed=embed)

    time.sleep(4)
  
  elif message.content == ('!gayrate'):
    embed = discord.Embed(color=3092790)
    embed.set_author(name=f'''You are {random.randint(1,101)}% gay!''')
    await message.channel.send(embed=embed)
    time.sleep(4)
  
  elif message.content == ('!av'):
    author = message.author
    await message.channel.send(author.avatar_url)
  
  elif message.content == ('!snipe'):
    author = message.author
    if snipe_message_content==None:
        await message.channel.send("nothing to snipe u stupid mf")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}", color=3092790)
        embed.set_author(name= f"sniped:")
        await message.channel.send(embed=embed)
        await message.channel.send(f'The sniped message was sent by: <@{snipe_message_author}>')
        return 
  elif message.content == ('!dog'):
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

        embed = discord.Embed(title="what da dog doin", color=3092790)
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=factjson['fact'])
        await message.channel.send(embed=embed)
  elif message.content == ('!pussy'):
    await message.channel.send('')







bot.run(token,bot=False)
