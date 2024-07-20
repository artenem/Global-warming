import discord
from main import * 
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$meaning'):
        await message.channel.send(meaning())
    if message.content.startswith('$reason'):
        await message.channel.send(reason())
    if message.content.startswith('$avoid'):
        await message.channel.send(avoid())
    if message.content.startswith('$conq'):
        await message.channel.send(conq())
    if message.content.startswith('$help'):
        await message.channel.send(help())

client.run("MTIxNzg4NDY5NzMwNTAyNjcxMw.Gea5cJ.ZyR3qYlamNjIKCQd0ISrRGG2P7A1s0B-vaG5Lw")