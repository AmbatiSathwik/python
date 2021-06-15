import discord
from discord.ext import commands

TOKEN = "ODQwMTQ2MjQ4MDI2ODE2NTQy.YJT9Kg.krDvf90o1veiu9gTjgVyjdkTNjk"

client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print('Bot is ready.')

client.run(TOKEN)
