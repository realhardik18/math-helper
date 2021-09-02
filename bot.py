import discord
from discord.ext import commands
import uuid
import requests
import shutil
from extractor import extracter
import os
from googler import search_google

client = commands.Bot(command_prefix="`")
client.remove_command('help')

@client.event
async def on_ready():
  print("im alive and working!!(logged in as {0.user})".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For `help"))

@client.command()
async def test(ctx):
  await ctx.send("yes chef")

@client.command()
async def solve(ctx):
  try:
    url = ctx.message.attachments[0].url           
  except IndexError:
    await ctx.send("you need to attach a file in order for this command to work")
  else:
    if url[0:26] == "https://cdn.discordapp.com":   
      r = requests.get(url, stream=True)
      imageName = str(uuid.uuid4()) + '.jpg'      
      with open(imageName, 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file) 
        await ctx.send("processing image...\nnote:\nif you dont get a response in 5 seconds the following could be the reason:\nour bot coudn't recognize the text because the image is too small or blurry\nthere is no text in the image at all\n**if any of the issues arise,please retry clicking the image!**")
        question=extracter(imageName)
        embed=discord.Embed(title="Here are the list of possible solutions", description="taken from [google](https://www.google.com/)", color=0xe74c3c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/825620548771643392/585c7883ffa07cea5ad0e2b0bf48e3af.webp?size=1024")
        for result in search_google(question):
          embed.add_field(name=f"solution number {x} link:", value=f"{result}", inline=False)
        await ctx.send(embed=embed)
        os.remove(imageName)
client.run("bot token goes here")