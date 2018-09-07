# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NDg2OTgyMDQwMTM5NTk1Nzc4.DnHCWw.5KvZa430Hqje3i2z9pwzy0SXcWg"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='hello',
                description="Answers a yes/no question.",
                brief="Dá um 'Olá' aos caros amiguinhos",
                aliases=['ola', 'hello_ola'],
                pass_context=True)
async def hello_ola(context):
    possible_responses = [
        'Bem lindo e bem alimentado',
        'Oi Hello Ola Hola Salut',
        'Joaquim Alberto 220',
        'Kanimambo',
        'Heteros totais',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(pass_context=True)
async def enter_channel(ctx):
    voice_channel = ctx.message.author.voice.voice_channel
    voice = await client.join_voice_channel(voice_channel)
    voice.play(discord.FFmpegPCMAudio("C:\\Users\Miguel\\Documents\\Audacity\\bem_lindo_bem_alimentado.mp3"))


@client.command(pass_context=True)
async def bemalimentado(context):
    await client.say("O " + context.message.author.mention + " é gay")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with BELAS MULHERES"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)

