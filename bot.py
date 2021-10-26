import discord
from discord import message
from discord.ext import commands
import uuid, requests, shutil, json
from extractor import extractor
import os
from googler import *
from math_methods import *
from wolfram import *
from decouple import config

client = commands.Bot(command_prefix="`")
client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CommandOnCooldown):  
    await ctx.send('to prevent spam, i have a cooldown of 15 seconds!')

@client.event
async def on_ready():
  print("im alive and working!!(logged in as {0.user})".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for `help list"))

@client.command()
async def test(ctx):
  await ctx.send("yes chef")

@client.command()
async def help(ctx,comnd):
  if comnd=="list":
    embed=discord.Embed(title="here are the list of all available commands", description="more commands coming soon!", color=0xf1c40f)
    embed.add_field(name="to solve a problem with an image", value="type **`help solve** for more info!", inline=False)
    embed.add_field(name="to solve linear questions in 2 variables", value="type **`help lin2v** for more info!", inline=False)
    embed.add_field(name="to add multiple numbers", value="type **`help add** for more info!", inline=False)
    embed.add_field(name="to multiply multiple numbers", value="type **`help mul** for more info!", inline=False)
    embed.add_field(name="to divide two numbers", value="type **`help div** for more info!", inline=False)  
    embed.add_field(name="to subtract two numbers", value="type **`help sub** for more info!", inline=False)
    embed.add_field(name="credits", value="this bot was made by [realhardik18](https://realhardik18.github.io)\nto add me in your server [click here](https://dsc.gg/maths-helper)", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/825620548771643392/585c7883ffa07cea5ad0e2b0bf48e3af.webp?size=1024")
    await ctx.send(embed=embed)
  elif comnd=="solve":
    embed=discord.Embed(title="how to use the `solve command", description="more info about the `solve feature", color=0xf1c40f)
    embed.add_field(name="basic requirments", value="attach an image with caption **`solve**\nmake sure the image is clear and readable\nif the bot takes more than 5 seconds to respond, it means it was not able to recognize the text from the image!", inline=False)
    await ctx.send(embed=embed)
  elif comnd=="lin2v":
    embed=discord.Embed(title="how to use the `lin2v command", description="more info about the `lin2v feature", color=0xf1c40f)
    embed.add_field(name="input format", value="`lin2v first_equation,second_equation", inline=False)
    embed.add_field(name="things to keep in mind", value="put equations as 2x + 5y + 2, 5x + 2y - 2(the first variable should always be x and second should always be y)")
    embed.add_field(name="usecase example",value="`lin2v 2x + 5y + 2, 5x + 2y - 2")
    await ctx.send(embed=embed)
  elif comnd=="mul":
    embed=discord.Embed(title="how to use the `mul command", description="more info about the `mul feature", color=0xf1c40f)
    embed.add_field(name="input format", value="`mul number1 number2 numbern", inline=False)
    embed.add_field(name="things to keep in mind", value="make sure the numbers are seprated by a space, the feature requires a minimum input of 2 numbers, you can add more numbers as per your requirment!")
    await ctx.send(embed=embed)
  elif comnd=="add":
    embed=discord.Embed(title="how to use the `add command", description="more info about the `add feature", color=0xf1c40f)
    embed.add_field(name="input format", value="`add number1 number2 numbern", inline=False)
    embed.add_field(name="things to keep in mind", value="make sure the numbers are seprated by a space, the feature requires a minimum input of 2 numbers, you can add more numbers as per your requirment!")
    await ctx.send(embed=embed)
  elif comnd=="div":
    embed=discord.Embed(title="how to use the `div command", description="more info about the `div feature", color=0xf1c40f)
    embed.add_field(name="input format", value="`div number1 number2", inline=False)
    embed.add_field(name="things to keep in mind", value="this will return number1/number2")
    await ctx.send(embed=embed)
  elif comnd=="sub":
    embed=discord.Embed(title="how to use the `sub command", description="more info about the `sub feature", color=0xf1c40f)
    embed.add_field(name="input format", value="`sub number1 number2", inline=False)
    embed.add_field(name="things to keep in mind", value="this will return number1-number2")
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
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
        question=extractor(imageName)
        embed=discord.Embed(title="Here are the list of possible solutions", description="taken from [google](https://www.google.com/)", color=0xe74c3c)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/825620548771643392/585c7883ffa07cea5ad0e2b0bf48e3af.webp?size=1024")
        x=1
        for result in search_google(question):
          embed.add_field(name=f"Link to solution {x}: ", value=f"{result}", inline=False)
          x+=1
        # Wolfram
        embed.add_field(name="Wolfram output: ")
        wlfParsedOut = json.load(wlfAlpha(question))
        if wlfParsedOut == 'unparsed':
          embed.add_field(name="\tWolfram Alpha could not parse this equation.")
        else:
          embed.add_field(name="Images: ")
          for i in range(len(wlfParsedOut)):
            embed.set_image(wlfParsedOut['images'][i])
          embed.add_field(name="Other Results:")
          for i in range(len(wlfParsedOut)):
            embed.add_field(name=wlfParsedOut['text'][i].split('__SUBPODS__')[0], value=wlfParsedOut['text'][i].split('__SUBPODS__')[1])
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