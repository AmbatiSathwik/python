import discord

from discord.ext import commands


client = commands.Bot(command_prefix = '.')
token = 'ODQwMTQ2MjQ4MDI2ODE2NTQy.YJT9Kg.krDvf90o1veiu9gTjgVyjdkTNjk'

@client.event
async def on_ready():
    print('Bot is on')


@client.event
async def on_member_join(member):
    channel = client.get_channel(770174010691420191)
    print('{} has joined a server'.format(member))
    await channel.send('Welcome to Server {}'.format(member))

@client.event
async def on_member_remove(member):
    channel = client.get_channel(770174010691420191)
    print('{} has left the server'.format(member))
    await channel.send('Get Lost from Server')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        hello = 'Hello'
        hello = hello + ' ' + str(message.author)
        await message.channel.send(hello)
        print(hello)
    if message.content.startswith(';;stop'):
        hello = 'Apinaduku thanks'
        hello = hello + ' ' + str(message.author)
        await message.channel.send(hello)
        print(hello)
    if message.content.startswith(';;play'):
        hello = 'Song play cheste egaresi thanta'
        hello = hello + ' ' + str(message.author)
        await message.channel.send(hello)
        print(hello)


client.run(token)
