import os
import discord
import requests
import json
import random
from keep_alive import keep_alive

my_secret = os.environ['DiscordKeyRanni']

client = discord.Client()

sad_words = ["sad", "bitches", "unhappy"]


starter_maiden = [
  "You are Maidenless",
  "No Bitches?",
  "No Maidens?"
]

response = requests.get("https://www.googleapis.com/youtube/v3/videos")
#  json_data = json.loads(response.text)
#  quote = json_data[0]['q'] + " -" + json_data[0]['a']
#  return(quote)
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_maiden))

keep_alive()
client.run(my_secret)

