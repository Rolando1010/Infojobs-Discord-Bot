from discord import Member
from discord_bot.embeds.commands import get_commands_embed
from discord_bot.bot import bot
from config import DISCORD_BOT_TOKEN
import discord_bot.commands.offers
import discord_bot.commands.commands
import discord_bot.commands.categories
import discord_bot.commands.skills
import discord_bot.commands.countries
import discord_bot.commands.statistics

@bot.event
async def on_member_join(member: Member):
    await member.send(f"Bienvenido {member.name} al bot de infojobs", embed=get_commands_embed())

@bot.event
async def on_ready():
    print("discord bot running")
    await bot.tree.sync()
    print("synchronized in ready")

bot.run(DISCORD_BOT_TOKEN)