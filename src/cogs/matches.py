#!/usr/bin/env python3
from discord import Interaction
from discord.app_commands import command, describe
from discord.ext.commands import Bot, Cog
from src.api.opendota import OpenDota
from src.ui.views import MatchPager
from src.utils.embeds import MatchNotFoundEmbed


class Matches(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot


    @command(name="match", description="Provides information about the played match")
    @describe(id="DotA match ID")
    async def match(self, interaction: Interaction, id: int) -> None:
        match = await OpenDota.get_match(id)
        if not match:
            await interaction.response.send_message(embed=MatchNotFoundEmbed(id))
            return

        pager = MatchPager(interaction, match)
        await pager.render_msg(edit=False)
        pager.msg = await interaction.original_response()


async def setup(bot: Bot) -> None:
    await bot.add_cog(Matches(bot))
