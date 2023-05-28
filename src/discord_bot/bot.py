from discord import Intents, Embed
from discord.ext.commands.bot import Bot
from discord.ext.commands.help import HelpCommand
from discord_bot.embeds.commands import get_commands_embed

class MyHelp(HelpCommand):
    async def send_bot_help(self, mapping):
        await self.context.send(embed=get_commands_embed())

    async def send_error_message(self, error):
        channel = self.get_destination()
        await channel.send(error)

intents = Intents.default()
intents.message_content = True
intents.members = True
bot = Bot(command_prefix="/", intents=intents, help_command=MyHelp())