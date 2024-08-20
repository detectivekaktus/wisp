#!/usr/bin/env python3
from asyncio import create_task, gather
from discord import Embed, Interaction
from discord.app_commands import command, describe
from discord.ext.commands import Bot, Cog
from src.api.opendota import OpenDota
from src.utils.constants import RANKS
from src.utils.embeds import PlayerNotFoundEmbed
from src.utils.emojis import ICONS, dota_plus


class Players(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot


    @command(name="player", description="Displays general information about the player")
    @describe(id="Player's account ID")
    async def player(self, interaction: Interaction, id: int) -> None:
        results = await gather(*[create_task(OpenDota.get_player(id)), create_task(OpenDota.get_player_winrate(id)), create_task(OpenDota.get_player_heroes(id))])
        for res in results:
            if not res:
                await interaction.response.send_message(embed=PlayerNotFoundEmbed(f"Couldn't find the player with this ID: {id}"))
                return

        embed = Embed()
        embed.add_field(name="Rank", value=RANKS[results[0]["rank_tier"]], inline=False)
        embed.add_field(name="Winrate", value=f"{round(results[1]["win"] / (results[1]["win"] + results[1]["lose"]) * 100, 2)}%", inline=False)
        embed.add_field(name="Wins", value=results[1]["win"])
        embed.add_field(name="Loses", value=results[1]["lose"])
        embed.add_field(name=f"Has Dota Plus subscription {dota_plus}", value="Yes" if results[0]["profile"]["plus"] else "No", inline=False)
        embed.add_field(name="Most played heroes", value="".join([ICONS[hero["hero_id"]] for hero in results[2][:5]]), inline=False)
        embed.set_author(name=f"{results[0]["profile"]["personaname"]} on Steam", url=results[0]["profile"]["profileurl"])
        embed.set_thumbnail(url=results[0]["profile"]["avatarfull"])

        await interaction.response.send_message(embed=embed)


    @command(name="wordcloud", description="Displays the most used words the player says")
    @describe(id="Player's account ID")
    async def wordcloud(self, interaction: Interaction, id: int) -> None:
        wc = await OpenDota.get_player_wordcloud(id)
        if not wc:
            await interaction.response.send_message(embed=PlayerNotFoundEmbed(f"Couldn't find the player with this ID: {id}"))
            return

        msg = ", ".join([key for key in wc["all_word_counts"].keys()])
        await interaction.response.send_message(msg[:1024])


async def setup(bot: Bot) -> None:
    await bot.add_cog(Players(bot))
