#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Optional, cast, override
from discord import ButtonStyle, Embed, Interaction, Message
from discord.ui import Button, View, button
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
    def __init__(self, interaction: Interaction, data: list[dict[str, Any]], timeout: Optional[float] = 180):
        super().__init__(interaction, data, timeout)


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
