import discord
from discord import message
from discord.ext import commands
import uuid
import requests
import shutil
from extractor import extracter
import os
from googler import search_google
from math_methods import lin_in_2_var
from decouple import config

client = commands.Bot(command_prefix="`")
client.remove_command('help')

@client.event
async def on_ready():
  print("im alive and working!!(logged in as {0.user})".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for `help"))

@client.command()
async def test(ctx):
  await ctx.send("yes chef")

@client.command()
async def help(ctx):
  embed=discord.Embed(title="here are the list of all available commands", description="more commands coming soon!", color=0xe74c3c)
  embed.add_field(name="to solve a problem with an image", value="attach an image and name the caption as **`solve**\nthis will take maximum 5 seconds to work, if you do not get any response by then, it means we had trouble processing the image!", inline=False)
  embed.add_field(name="to solve linear questions in 2 variables", value="**`lin2v first_equation,second_equation**\nhere are some things to keep in mind while using this command:\nput equations  as 2x + 5y + 2, 5x + 2y - 2(the first variable should always be x and second should always be y)", inline=False)
  embed.add_field(name="to add multiple numbers", value="**`add num1 num2 num3 num_n**", inline=False)
  embed.add_field(name="to multiply multiple numbers", value="**`mul num1 num2 num3 num_n**", inline=False)
  embed.add_field(name="to divide two numbers", value="**`div num1 num2\nthis returns num1/num2**", inline=False)  
  embed.add_field(name="to subtract two numbers", value="**`sub num1 num2\nthis returns num1-num2**", inline=False)
  embed.add_field(name="credits", value="this bot was made by [Realhardik18](https://realhardik18.github.io)\nspecial thanks to [ankushkun](https://ankushkun.github.io/) and dbamogh#2366", inline=False)
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/825620548771643392/585c7883ffa07cea5ad0e2b0bf48e3af.webp?size=1024")
  await ctx.send(embed=embed)

@client.command()
async def solve(ctx):
  #'''
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
        x=1
        for result in search_google(question):
          embed.add_field(name=f"solution number {x} link:", value=f"{result}", inline=False)
          x+=1
        await ctx.send(embed=embed)
        #os.remove(imageName)
        #'''
  #await ctx.send("this command is still under development")


@client.command()
async def lin2v(message,*,vals):
  try:
    await message.send(lin_in_2_var(vals))
  except IndexError:
    await message.send("please enter the values in the correct format!\nyou can check the formot from the help command!")

@client.command()
async def add(message,*,vals):
  try:
    sume=0
    vals_split=vals.split(" ")
    for ele in vals_split:
      ele_int=float(ele)
      sume+=ele_int
    await message.send(sume)
  except ValueError:
    await message.send("make sure all the values are integers/decimals!")

@client.command()
async def mul(message,*,vals):
  try:
    prod=1
    vals_split=vals.split(' ')
    for ele in vals_split:
      ele_int=int(ele)
      prod*=ele_int
    await message.send(prod)
  except ValueError:
    await message.send("make sure all the values are integers/decimals!")

@client.command()
async def sub(message,val1,val2):
  try:
    await message.send(float(val1)-float(val2))
  except ValueError:
    await message.send("make sure all the values are integers/decimals!")

@client.command()
async def div(message,val1,val2):
  try:
    if val2=='0':
      await message.send("you cannot divide by zero!")
    elif val2!='0':
      await message.send(f"the quotient is {float(val1)/float(val2)}\nand the remainder is {float(val1)%float(val2)}")
  except ValueError:
    await message.send("make sure all the values are integers/decimals!")

client.run(config("BOT_TOKEN"))