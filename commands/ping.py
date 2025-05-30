from discord import app_commands, Interaction

def register(tree: app_commands.CommandTree):
    @tree.command(name="ping", description="Affiche le ping du bot")
    async def ping(interaction: Interaction):
        client = interaction.client
        latency = round(client.latency * 1000)
        await interaction.response.send_message(f"{latency} ms")
