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
    async def get_player_heroes(id: int) -> Optional[list[dict[str, int]]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/heroes")

    @staticmethod
    async def get_player_wordcloud(id: int) -> Optional[dict[str, dict[str, int]]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/wordcloud")

    @staticmethod
    async def get_player_recent_matches(id: int) -> Optional[list[dict[str, Any]]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/players/{id}/recentMatches")

    @staticmethod
    async def refresh_player(id: int) -> bool:
        async with ClientSession() as session:
            return await post(session, f"{BASE_URL}/players/{id}/refresh") == 200


    @staticmethod
    async def get_match(id: int) -> Optional[dict[str, Any]]:
        async with ClientSession() as session:
            return await get(session, f"{BASE_URL}/matches/{id}")


def is_radiant(pos: int) -> bool:
    return pos < 128


LOBBY_TYPES: Final[dict[int, str]] = {
    0: "Normal",
    1: "Practice",
    2: "Tournament",
    7: "Ranked",
}

REGIONS: Final[dict[int, str]] = {
    1: "Us west",
    2: "Us east",
    3: "Europe",
    5: "Singapore",
    6: "Dubai",
    7: "Australia",
    8: "Stockholm",
    9: "Austria",
    10: "Brazil",
    11: "Southafrica",
    12: "Pw telecom shanghai",
    13: "Pw unicom",
    14: "Chile",
    15: "Peru",
    16: "India",
    17: "Pw telecom guangdong",
    18: "Pw telecom zhejiang",
    19: "Japan",
    20: "Pw telecom wuhan",
    25: "Pw unicom tianjin",
    37: "Taiwan",
    38: "Argentina"
}

GAME_MODES: Final[dict[int, str]] = {
    0: "Unknown",
    1: "All pick",
    2: "Captains mode",
    3: "Random draft",
    4: "Single draft",
    5: "All random",
    6: "Intro",
    7: "Diretide",
    8: "Reverse captains mode",
    9: "Greeviving",
    10: "Tutorial",
    11: "Mid only",
    12: "Least played",
    13: "Limited heroes",
    14: "Compendium matchmaking",
    15: "Custom",
    16: "Captains draft",
    17: "Balanced draft",
    18: "Ability draft",
    19: "Event",
    20: "All random death match",
    21: "1v1 middle",
    22: "All pick",
    23: "Turbo",
    24: "Mutation",
    25: "Coaches challange"
}
