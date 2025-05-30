import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

    await tree.sync()
    print("Commandes synchronisées.")

from commands import ping
from commands import hello

ping.register(tree)
hello.register(tree)

from utils.token import Token

token = Token()
TOKEN = token.getToken()
client.run(TOKEN)