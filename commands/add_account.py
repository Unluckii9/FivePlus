from discord import app_commands, Interaction

from db.db import Db

def register(tree: app_commands.CommandTree):
    @tree.command(name="add_account", description="Ajoute un compte FiveM")
    @app_commands.describe(
        mail = "mail",
        password = "mot de passe"
    )
    async def add_account(interaction: Interaction, mail: str, password: str):
        user = interaction.user
        user_id = user.id

        # A ajouter une vérification sur le mail qu'il ait un @ et qui fini par un .truc
        
        db = Db()
        discord_id_users = db.get_discord_id_users()
        
        is_register = False
        for discord_id_user in discord_id_users:
            if discord_id_user == user_id:
                is_register = True
                break

        if is_register:
            req = db.add_account(user_id, mail, password)
            if req:
                await interaction.response.send_message("Compte enregistrer avec succès !", ephemeral=True)
            else:
                await interaction.response.send_message("Erreur avec l'enregistrement du compte", ephemeral=True) 