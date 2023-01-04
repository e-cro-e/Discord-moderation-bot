import os
import discord
import requests
import asyncio
from keep_alive import keep_alive

my_secret = os.environ['DiscordKeyRanni']

client = discord.Client()

sad_words = ["sad", "bitches", "unhappy"]

# A dictionary to store the mute duration for each user
mute_duration = {}
# A dictionary to store the mute count for each user
mute_count = {}


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  

  if any(word in msg for word in sad_words):
    await message.channel.send(f"{message.author.mention}, is being too horny, further horny comments will result in horny jail.")

  # Check if the user is already muted
    if message.author.id in mute_duration:
            # Add 5 seconds to the existing mute duration
         mute_duration[message.author.id] += 5
    else:
            # Mute the user for the first time (for 5 seconds)
        mute_duration[message.author.id] = 5
   
         # Set the "send_messages" permission to False for the user
        await message.channel.set_permissions(message.author, send_messages=False)

        # Wait for the mute duration to expire
        await asyncio.sleep(mute_duration[message.author.id])

        # Set the "send_messages" permission to True for the user
        await message.channel.set_permissions(message.author, send_messages=True)

keep_alive()
client.run(my_secret)

