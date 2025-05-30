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

        user_mails = []
        user_passwords = []

        for user_account in user_accounts:
            mail = user_account[0]
            password = user_account[1]

            user_mails.append(mail)
            user_passwords.append(password)
        
        account = Account()
        await interaction.response.send_message(embed=embed, view=account)

class Account(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.index_user_account = 0

    @discord.ui.button(label="Précédent", style=discord.ButtonStyle.danger, custom_id="precedent_btn")
    async def valider(self, interaction: Interaction, button: discord.ui.Button):
        await interaction.response.send_message("✅ Tu as cliqué sur Valider !", ephemeral=True)

    @discord.ui.button(label="Suivant", style=discord.ButtonStyle.success, custom_id="suivant_btn")
    async def annuler(self, interaction: Interaction, button: discord.ui.Button):
        await interaction.response.send_message("❌ Action annulée.", ephemeral=True)

    