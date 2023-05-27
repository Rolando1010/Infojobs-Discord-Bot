from discord import Interaction
from discord_bot.embeds.commands import get_commands_embed
from discord_bot.bot import bot

@bot.tree.command(name="comandos", description="Muestra una lista de comandos que puedes ejecutar")
async def show_commands(interaction: Interaction):
    await interaction.response.send_message(embed=get_commands_embed())