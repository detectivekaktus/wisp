#!/usr/bin/env python3
from os import listdir
from typing import Final, override
from discord import Activity, ActivityType, Intents, Status
from discord.ext.commands import Bot
from src.utils.logging import LOGGER


INTENTS: Final[Intents] = Intents.default()
INTENTS.message_content = True
class Wisp(Bot):
    def __init__(self, intents: Intents) -> None:
        super().__init__(command_prefix='?',
                         intents=intents,
                         owner_id=692305905123065918,
                         activity=Activity(type=ActivityType.playing, name="3/2/2 on Pudge"),
                         status=Status.idle)


    @override
    async def setup_hook(self) -> None:
        LOGGER.info("Loading modules from `src.cogs`.")
        await load_cogs()
        LOGGER.info(f"Successfully syncronized {len(await self.tree.sync())} commands globally.")


bot = Wisp(INTENTS)
bot.remove_command("help")


async def load_cogs():
    for filename in listdir("src/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"src.cogs.{filename[:-3]}")


@bot.event
async def on_ready() -> None:
    LOGGER.info("Bot instance is ready to handle requests.")
