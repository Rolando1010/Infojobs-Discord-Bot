from discord import Interaction, Color, app_commands
from discord_bot.bot import bot
from discord_bot.views import get_list_embed, autocompletion
from jobs.skills import get_skills
from jobs.categories import get_categories, get_category_skills

class SkillCommandsGroup(app_commands.Group):
    @app_commands.command(name="todas", description="Listado de habilidades solicitadas en ofertas")
    async def all(self, interaction: Interaction):
        skills = get_skills()
        skills_embed = get_list_embed("Habilidades", "Listado de habilidades solicitadas en ofertas", Color.dark_gold(), skills)
        await interaction.response.send_message(embed=skills_embed)
    
    @app_commands.command(name="categorias", description="Ver las skills pertenecientes a cada categoría")
    @app_commands.autocomplete(categoria=autocompletion(get_categories))
    async def by_category(self, interaction: Interaction, categoria: str):
        skills = get_category_skills(categoria)
        await interaction.response.send_message(embed=get_list_embed(
            "Habilidades",
            f"Habilidades de la categoría {categoria}",
            Color.dark_gold(),
            skills
        ))

skill_commands_group = SkillCommandsGroup(name="habilidades", description="Muestra las habilidades solicitadas en ofertas")
bot.tree.add_command(skill_commands_group)