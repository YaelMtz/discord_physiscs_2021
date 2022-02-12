import discord
import os
import requests
import json
import random

client = discord.Client()

swords = ["sad",
"triste", 
"morirme", 
"muy dificil",
"La facu se cae"]

animos = [
   "Ánimo.",
   "Bofo.",
   "Anímese"
 ]
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
   return

  if message.content.startswith("$uaslp"):
   await message.channel.send("La mejor universidad.")

  if message.content.startswith('$problema'):
   await message.channel.send("Formidable.")

  if any(word in (message.content) for word in swords):
    await message.channel.send(random.choice(animos))



client.run(os.environ['TOKEN'])
