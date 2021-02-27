import discord
import requests
import asyncio
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("*")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "*"
    name = "*"
    channel = client.get_channel(*)
    a = 0
    while True:
        headers = {'Client-ID': 'Client-ID'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "*")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("무야호")

    if message.content.startswith("!말해줘"):
        channel = message.content[5:23]
        msg = message.content[24:]
        await client.get_channel(int(channel)).send(msg)


client.run("*")
