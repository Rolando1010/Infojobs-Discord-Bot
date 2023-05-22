from discord import Intents
from discord.ext.commands.bot import Bot

intents = Intents.default()
intents.message_content = True
bot = Bot(command_prefix="/", intents=intents)