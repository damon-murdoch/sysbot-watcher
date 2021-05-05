# Operating System API
import os

# Discord Bot API
import discord

# Config.py file
import config

# Discord Secret Token
TOKEN = config.TOKEN

# Create a discord client connection
client = discord.Client()

@client.event # Bot has started
async def on_ready():
  print(f'{client.user.name} has connected to discord!')

@client.command # Check if user is online
async def status(ctx, member: discord.Member=None):
  if member is None:
    member = ctx.author
  embed=discord.Embed(title=f"{member.name} your current status is ", description= f'{member.activities[0].name}', color=0xcd32a7)
  await ctx.send(embed=embed)

client.run(TOKEN)