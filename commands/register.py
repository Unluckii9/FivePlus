from discord import app_commands, Interaction

from db.db import Db

def register(tree: app_commands.CommandTree):
    @tree.command(name="register", description="Créé ton compte")
    @app_commands.describe(
        username="Nom d'utilisateur"
    )
    async def register(interaction: Interaction, username: str):
        user = interaction.user
        roles = user.roles if hasattr(user, "roles") else []
        
        ALPHA_TESTER_ROLE_ID = 1377936299226300426

        user_have_role = False
        for role in roles:
            if role.id == ALPHA_TESTER_ROLE_ID:
                user_have_role = True
            
        if user_have_role:
            user_id = user.id

            db = Db()
            req = None
            try:
                req = db.add_user(user_id, username)
            except Exception as e:
                if str(e) == "Discord ID already used":
                    await interaction.response.send_message("Tu as déjà un compte associé avec ce Discord", ephemeral=True)
                else:
                    await interaction.response.send_message(f"Une erreur est survenue", ephemeral=True)
                return

            if req:
                await interaction.response.send_message(f"Compte créé avec succès {username}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Erreur lors de la création du compte veuillez réesayer ou contacter un administrateur", ephemeral=True)
        
        else:
            await interaction.response.send_message(f"Tu n'a pas la permission de faire cette commande !", ephemeral=True)


        
        
