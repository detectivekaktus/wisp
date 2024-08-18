#!/usr/bin/env python3
from asyncio import create_task, gather
from os import mkdir, path
from typing import Optional
from aiohttp import ClientSession
from aiofiles import open


async def get_hero_names() -> Optional[list[str]]:
    async with ClientSession() as session:
        async with session.get("https://api.opendota.com/api/heroes") as r:
            if r.status != 200:
                return None
            return [hero["name"][14:] for hero in await r.json()]


async def download_hero_icon(name: str) -> None:
    async with ClientSession() as session:
        async with session.get(f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/heroes/icons/{name}.png") as r:
            if r.status != 200:
                return
            async with open(f"imgs/icons/{name}_icon.png", "wb") as f:
                await f.write(await r.read())


async def download_hero_icons() -> None:
    names: Optional[list[str]] = await get_hero_names()
    if not names:
        exit(1)
    if not path.exists("imgs/icons/"):
        mkdir("imgs/icons/")
    await gather(*[create_task(download_hero_icon(name)) for name in names])
    
