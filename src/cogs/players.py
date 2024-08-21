#!/usr/bin/env python3
from asyncio import create_task, gather
from discord import Embed, Interaction
from discord.app_commands import command, describe
from discord.ext.commands import Bot, Cog
from src.api.opendota import OpenDota
from src.ui.views import HeroesPager, MatchesPager
from src.utils.calc import calculate_winrate
from src.constants import RANKS
from src.utils.embeds import PlayerNotFoundEmbed
from src.emojis import ICONS, dota_plus


class Players(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot


    @command(name="player", description="Displays general information about the player")
    @describe(id="Player's account ID")
    async def player(self, interaction: Interaction, id: int) -> None:
        generic, wl, heroes = await gather(*[create_task(OpenDota.get_player(id)), create_task(OpenDota.get_player_winrate(id)), create_task(OpenDota.get_player_heroes(id))])
        if not generic or not wl or not heroes:
            await interaction.response.send_message(embed=PlayerNotFoundEmbed(id))
            return

        embed = Embed()
        embed.add_field(name="Rank", value=RANKS[generic["rank_tier"]], inline=False)
        embed.add_field(name="Winrate", value=f"{calculate_winrate(wl["win"], loses=wl["lose"])}%", inline=False)
        embed.add_field(name="Wins", value=wl["win"])
        embed.add_field(name="Loses", value=wl["lose"])
        embed.add_field(name="Most played heroes", value="".join([ICONS[hero["hero_id"]] for hero in heroes[:5]]), inline=False)
        embed.add_field(name=f"Has Dota Plus subscription {dota_plus}",
                        value="Yes" if generic["profile"]["plus"] else "No",
                        inline=False)
        embed.set_author(name=f"{generic["profile"]["personaname"]} on Steam", url=generic["profile"]["profileurl"])
        embed.set_thumbnail(url=generic["profile"]["avatarfull"])

        await interaction.response.send_message(embed=embed)


    @command(name="wordcloud", description="Displays the most used words the player says")
    @describe(id="Player's account ID")
    async def wordcloud(self, interaction: Interaction, id: int) -> None:
        await interaction.response.defer()

        wc = await OpenDota.get_player_wordcloud(id)
        if not wc or "all_word_counts" not in wc:
            await interaction.followup.send(embed=PlayerNotFoundEmbed(id))
            return

        await interaction.followup.send(", ".join([key for key in wc["all_word_counts"].keys()])[:2000])


    @command(name="player-heroes", description="Displays the most played heroes of the player")
    @describe(id="Player's account ID")
    async def player_heroes(self, interaction: Interaction, id: int) -> None:
        data = await OpenDota.get_player_heroes(id)
        if not data:
            await interaction.response.send_message(embed=PlayerNotFoundEmbed(id))
            return

        pager = HeroesPager(interaction, data)
        await pager.render_msg(edit=False)
        pager.msg = await interaction.original_response()


    @command(name="player-matches", description="Displays the most recent matches of the player")
    @describe(id="Player's account ID")
    async def player_matches(sel, interaction: Interaction, id: int) -> None:
        matches = await OpenDota.get_player_recent_matches(id)
        if not matches:
            await interaction.response.send_message(embed=PlayerNotFoundEmbed(id))
            return
        
        pager = MatchesPager(interaction, matches)
        await pager.render_msg(edit=False)
        pager.msg = await interaction.original_response()


async def setup(bot: Bot) -> None:
    await bot.add_cog(Players(bot))
