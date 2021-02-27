import discord
import requests
import asyncio
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("똘똘똘이 감시")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "jungtaejune"
    name = "똘삼"
    channel = client.get_channel(815144378817052713)
    a = 0
    while True:
        headers = {'Client-ID': '9pntjil5qu35etgb4b50ve0xsap8tu'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "@F31YX#4849")
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


client.run("ODE1MTI3NzAyMDc5MDEyOTM3.YDn41A.DKnkVpmGz7lrexwumOegnrr-hm8")
