#!/usr/bin/env python3
from typing import Any, Final, Optional
from aiohttp import ClientSession
from src.api import get, post


BASE_URL: Final[str] = "https://api.opendota.com/api"


class OpenDota:
    # TODO: Use Steam Web API to check whether an account with the
    # given ID exists or not.
    @staticmethod
    async def get_player(id: int) -> Optional[dict[str, Any]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}")


    @staticmethod
    async def get_player_winrate(id: int) -> Optional[dict[str, int]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/wl")


    @staticmethod
    async def get_player_heroes(id: int) -> Optional[dict[str, int]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/heroes")


    @staticmethod
    async def get_player_wordcloud(id: int) -> Optional[dict[str, dict[str, int]]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/wordcloud")


    @staticmethod
    async def refresh_player(id: int) -> bool:
        async with ClientSession() as session:
            return await post(session, f"{BASE_URL}/players/{id}/refresh") == 200
