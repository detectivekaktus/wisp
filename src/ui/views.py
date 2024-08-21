#!/usr/bin/env python3
from abc import ABC, abstractmethod
from time import gmtime, strftime
from typing import Any, Final, Optional, cast, override
from discord import ButtonStyle, Embed, Interaction, Message
from discord.ui import Button, View, button
from src.api.opendota import GAME_MODES, LOBBY_TYPES, REGIONS, is_radiant
from src.constants import HERO_NAMES
from src.utils.calc import calculate_winrate
from src.emojis import ICONS
from src.utils.string import display_hero_name


class Pager(ABC, View):
    def __init__(self, interaction: Interaction, data: Any, timeout: Optional[float] = 180):
        super().__init__(timeout=timeout)
        self.interaction = interaction
        self.data: Any = data
        self.current: int = 0
        self.msg: Optional[Message] = None
        self.embed: Optional[Embed] = None


    async def render_msg(self, edit: bool = False) -> None:
        self.update_buttons()
        await self.update_msg()
        if edit:
            await cast(Message, self.msg).edit(view=self, embed=cast(Embed, self.embed))
        else:
            await self.interaction.response.send_message(view=self, embed=cast(Embed, self.embed))

    
    @abstractmethod
    async def update_msg(self) -> None:
        pass


    def update_buttons(self) -> None:
        self.prev.disabled = self.current == 0
        self.next.disabled = self.current == len(self.data) - 1


    @button(label="<", style=ButtonStyle.blurple, disabled=True)
    @abstractmethod
    async def prev(self, interaction: Interaction, button: Button) -> None:
        pass


    @button(label=">", style=ButtonStyle.blurple, disabled=True)
    @abstractmethod
    async def next(self, interaction: Interaction, button: Button) -> None:
        pass


class HeroesPager(Pager):
    @override
    async def update_msg(self) -> None:
        hero = self.data[self.current]
        self.embed = Embed(title=f"{ICONS[hero["hero_id"]]}{display_hero_name(HERO_NAMES[hero["hero_id"]])}")
        self.embed.set_author(name=self.interaction.user.name, icon_url=self.interaction.user.avatar)
        self.embed.set_thumbnail(
            url=f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/heroes/{HERO_NAMES[hero["hero_id"]]}.png?"
        )
        self.embed.add_field(name="Winrate", value=f"{calculate_winrate(hero["win"], total=hero["games"])}%", inline=False)
        self.embed.add_field(name="Total games", value=hero["games"], inline=False)
        self.embed.add_field(name="Wins", value=hero["win"])
        self.embed.add_field(name="Loses", value=hero["games"] - hero["win"])
        self.embed.add_field(name="Winrate against this hero",
                             value=f"{calculate_winrate(hero["against_win"], total=hero["against_games"])}%",
                             inline=False)


    @button(label="<", style=ButtonStyle.blurple, disabled=True)
    @override
    async def prev(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current > 0:
            self.current -= 1
        await self.render_msg(edit=True)


    @button(label=">", style=ButtonStyle.blurple, disabled=True)
    @override
    async def next(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current != len(self.data) - 1:
            self.current += 1
        await self.render_msg(edit=True)


class MatchesPager(Pager):
    def __init__(self, interaction: Interaction, data: Any, timeout: Optional[float] = 180):
        super().__init__(interaction, data, timeout)


    @override
    async def update_msg(self) -> None:
        match = self.data[self.current]
        self.embed = Embed(title=f"Match {match["match_id"]}")
        self.embed.set_thumbnail(
            url=f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/heroes/{HERO_NAMES[match["hero_id"]]}.png?"
        )
        self.embed.add_field(name="Type", value=LOBBY_TYPES[match["lobby_type"]])
        self.embed.add_field(
            name="Result",
            value="Win" if (is_radiant(match["player_slot"]) and match["radiant_win"]) or
            (not is_radiant(match["player_slot"]) and not match["radiant_win"]) else "Lose",
            inline=False
        )
        self.embed.add_field(name="Played at UTC", value=strftime("%H:%M:%S", gmtime(match["start_time"])))
        self.embed.add_field(name="Duration", value=strftime("%H:%M:%S", gmtime(match["duration"])), inline=False)
        self.embed.add_field(name="Kills", value=match["kills"])
        self.embed.add_field(name="Deaths", value=match["deaths"])
        self.embed.add_field(name="Assists", value=match["assists"])
        self.embed.add_field(name="GMP", value=match["gold_per_min"])
        self.embed.add_field(name="Hero damage", value=match["hero_damage"])
        self.embed.add_field(name="Tower damage", value=match["tower_damage"])
        self.embed.add_field(name="Healing", value=match["hero_healing"])


    @button(label="<", style=ButtonStyle.blurple, disabled=True)
    @override
    async def prev(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current > 0:
            self.current -= 1
        await self.render_msg(edit=True)


    @button(label=">", style=ButtonStyle.blurple, disabled=True)
    @override
    async def next(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current != len(self.data) - 1:
            self.current += 1
        await self.render_msg(edit=True)


class MatchPager(Pager):
    OVERALL: Final[int] = 0
    HEROES: Final[int]  = 1
    MAP: Final[int]     = 2

    
    @override
    async def update_msg(self) -> None:
        match self.current:
            case self.OVERALL:
                self.embed = Embed(title=f"Match {self.data["match_id"]}")
                self.embed.add_field(name="Lobby type", value=LOBBY_TYPES[self.data["lobby_type"]])
                self.embed.add_field(name="Region", value=REGIONS[self.data["region"]])
                self.embed.add_field(name="Game mode", value=GAME_MODES[self.data["game_mode"]])
                self.embed.add_field(name="Duration", value=strftime("%H:%M:%S", gmtime(self.data["duration"])))
                self.embed.add_field(name="Played at UTC", value=strftime("%H:%M:%S", gmtime(self.data["start_time"])))
                self.embed.add_field(
                    name="Result",
                    value="Radiant win" if self.data["radiant_win"] else "Dire win",
                    inline=False
                )
                self.embed.add_field(name=f"Radiant {self.data["radiant_score"]}", value="".join([ICONS[hero["hero_id"]] for hero in self.data["players"] if hero["isRadiant"]]))
                self.embed.add_field(name=f"Dire {self.data["dire_score"]}", value="".join([ICONS[hero["hero_id"]] for hero in self.data["players"] if not hero["isRadiant"]]))
            case self.HEROES:
                self.embed = Embed(
                    title=f"Match {self.data["match_id"]}",
                    description="To be done."
                )
            case self.MAP:
                self.embed = Embed(
                    title=f"Match {self.data["match_id"]}",
                    description="To be done."
                )



    @override
    def update_buttons(self) -> None:
        self.prev.disabled = self.current == 0
        self.next.disabled = self.current == self.MAP


    @button(label="<", style=ButtonStyle.blurple, disabled=True)
    @override
    async def prev(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current > self.OVERALL:
            self.current -= 1
        await self.render_msg(edit=True)


    @button(label=">", style=ButtonStyle.blurple, disabled=True)
    @override
    async def next(self, interaction: Interaction, button: Button) -> None:
        await interaction.response.defer()
        if self.current < self.MAP:
            self.current += 1
        await self.render_msg(edit=True)

