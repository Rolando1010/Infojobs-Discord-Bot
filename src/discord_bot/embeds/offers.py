from discord import Embed, Color
from jobs.offers import Offer

def get_offers_embed(original_offers: list[Offer], total_pages: int, page: int, description: str):
    offers = original_offers[:10]
    offers_embed = Embed(
        title=f"Ofertas de trabajo ({page}/{total_pages})",
        description=f"{description} ({len(offers)})",
        color=Color.dark_blue()
    )
    for offer in offers:
        offers_embed.add_field(name="", value=f"""
            ***[{offer.title}]({offer.link})***
            [{offer.author.name}]({offer.author.link})
            ***ID***: {offer.id}
            {offer.applications} aplicaciones
            {offer.get_salary_message()}
        """, inline=False)
        offers_embed.add_field(name="", value="-"*70, inline=False)
    return offers_embed

def get_offer_embed(offer: Offer):
    offer_embed = Embed(
        title=offer.title,
        url=offer.link,
        description="",
        color=Color.dark_teal(),
    )
    offer_embed.set_thumbnail(url=offer.author.logo)
    offer_embed.add_field(name="", value=f"[{offer.author.name}]({offer.author.link})", inline=False)
    offer_embed.add_field(name="", value=offer.country)
    offer_embed.add_field(name="", value=offer.category)
    offer_embed.add_field(name="", value="", inline=False)
    offer_embed.add_field(name="", value=offer.get_salary_message())
    offer_embed.add_field(name="", value=f"{offer.applications} aplicaciones")
    offer_embed.add_field(name="", value="", inline=False)
    description = offer.description[:200] + "..." if len(offer.description) > 100 else offer.description
    offer_embed.add_field(name="", value=description, inline=False)
    return offer_embed