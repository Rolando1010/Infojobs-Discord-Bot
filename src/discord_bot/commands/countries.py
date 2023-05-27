from discord import Interaction, Color
from discord_bot.bot import bot
from discord_bot.embeds.list import get_list_embed
from jobs.countries import get_countries

@bot.tree.command(name="paises", description="Consulta el listado de países que ofertan trabajos")
async def show_countries(interaction: Interaction):
    countries = get_countries()
    countries_embed = get_list_embed("Países", "Listado de países con ofertas de trabajo", Color.dark_magenta(), countries)
    await interaction.response.send_message(embed=countries_embed)