from discord import Embed, Color

COMMANDS = [
    ("Comandos", "Muestra la lista de comandos que puedes ejecutar", "/comandos"),
    ("Ofertas de trabajo", [
        ("Muestra todas ofertas de trabajo disponibles", "/ofertas todas"),
        ("Muestra las ofertas de trabajo de la categoría especificada", "/ofertas categorias <categoria>"),
        ("Muestra las ofertas de trabajo de la habilidad especificada", "/ofertas habilidades <habilidad>"),
        ("Muestra las ofertas de trabajo del país especificado", "/ofertas paises <pais>"),
        ("Busca ofertas de trabajo según palabras clave", "/ofertas buscar <búsqueda>"),
        ("Consulta una oferta de trabajo específica por su ID", "/ofertas id <id>"),
        ("Obtén recomendaciones de ofertas de trabajo según tu perfil en github", "/ofertas recomendaciones <github-username>")
    ]),
    ("Categorías", "Obtén las categorías de ofertas de trabajo", "/categorias"),
    ("Habilidades", [
        ("Obtén todas las habilidades de ofertas de trabajo", "/habilidades todas"),
        ("Obtén todas las habilidades asociadas a una cierta categoría", "/habilidades categorias <categoria>")
    ]),
    ("Países", "Obtén los países de ofertas de trabajo", "/paises"),
    ("Estadísticas", [
        ("Lenguajes de programación más usados", "/estadisticas lenguajes"),
        ("Tecnologías frontend más usadas", "/estadisticas frontend"),
        ("Tecnologías backend más usadas", "/estadisticas backend"),
        ("Ofertas de trabajo por país", "/estadisticas paises"),
        ("Ofertas de trabajo por categoría", "/estadisticas categorias")
    ])
]

def get_commands_embed():
    commands_embed = Embed(
        title="Lista de comandos",
        description="""
            Puedes acceder a los servicios de infojobs a través de este bot
            Utiliza el '/' para ejecutar cada comando
        """,
        color=Color.dark_red()
    )

    def add_command(put_title: bool):
        commands_embed.add_field(
            name=title if put_title else "",
            value=f"""```bash
# {description}
{command}```""",
            inline=False
        )

    for title, *data in COMMANDS:
        if type(data[0]) == list:
            for index, (description, command) in enumerate(data[0]):
                add_command(index == 0)
        else:
            description, command = data
            add_command(True)
    return commands_embed