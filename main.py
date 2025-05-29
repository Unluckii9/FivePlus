import discord
from discord import app_commands

from utils.token import Token


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

    await tree.sync()
    print("Commandes synchronisées.")

token = Token()
TOKEN = token.getToken()
client.run(TOKEN)