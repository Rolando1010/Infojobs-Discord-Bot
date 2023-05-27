from discord import Embed, Colour

def get_list_embed(title: str, description: str, color: int | Colour, items: list[str], thumbnail: str=None):
    list_embed = Embed(title=title, description=description, color=color)
    if thumbnail: list_embed.set_thumbnail(url=thumbnail)
    for item in items:
        list_embed.add_field(name="", value=f"* {item}", inline=False)
    return list_embed