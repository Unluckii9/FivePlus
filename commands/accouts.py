from discord import app_commands, Interaction
import discord

from db.db import Db

def register(tree: app_commands.CommandTree):
    @tree.command(name="accounts", description="Listes tes comptes FiveM")
    async def accounts(interaction: Interaction):
        user = interaction.user
        user_id = user.id
        
        db = Db()
        user_accounts = db.get_accounts_discord_id(user_id)

        embed = discord.Embed(
            title="Compte FiveM",
            description="",
            color=discord.Color.blue()
        )

        for user_account in user_accounts:
            mail = user_account[0]
            password = user_account[1]

            embed.description += f"{mail} | {password}\n"

        await interaction.response.send_message(embed=embed)

