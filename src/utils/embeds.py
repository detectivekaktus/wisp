#!/usr/bin/env python3
from discord import Color, Embed


class PlayerNotFoundEmbed(Embed):
    def __init__(self, id: int):
        super().__init__(title="Couldn't find the player",
                         description=f"Couldn't find the player with this ID: {id}",
                         color=Color.red())


class MatchNotFoundEmbed(Embed):
    def __init__(self, id: int):
        super().__init__(title="Couldn't find the match",
                         description=f"Couldn't find the match with this ID: {id}",
                         color=Color.red())
