from discord import app_commands, Interaction

def register(tree: app_commands.CommandTree):
    @tree.command(name="hello", description="Dis bonjour a quelqu'un")
    @app_commands.describe(
        nom="Nom de la personne"
    )
    async def hello(interaction: Interaction, nom: str):
        await interaction.response.send_message(f"Salut {nom} !")
        
