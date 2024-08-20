#!/usr/bin/env python3
from discord import Color, Embed


class PlayerNotFoundEmbed(Embed):
    def __init__(self, msg: str):
        super().__init__(title="Couldn't find the player",
                         description=msg,
                         color=Color.red())
