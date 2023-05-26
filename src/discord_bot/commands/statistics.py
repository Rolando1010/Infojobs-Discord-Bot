from discord import Interaction, File
from discord.app_commands import choices, Choice
from config import STATISTICS_CHARTS_DIRECTORY
from discord_bot.bot import bot

@bot.tree.command(name="estadisticas", description="Estadísticas de distintos datos de ofertas")
@choices(estadistica=[
    Choice(name="lenguajes", value="offers_by_languages"),
    Choice(name="frontend", value="offers_by_frontend"),
    Choice(name="backend", value="offers_by_backend"),
    Choice(name="paises", value="offers_by_countries"),
    Choice(name="categorias", value="offers_by_categories")
])
async def show_statistic(interaction: Interaction, estadistica: str):
    filename = estadistica + ".png"
    file = File(STATISTICS_CHARTS_DIRECTORY + "/" + filename, filename=filename)
    await interaction.response.send_message(file=file)