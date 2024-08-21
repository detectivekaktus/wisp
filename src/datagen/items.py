#!/usr/bin/env python3
from asyncio import create_task, gather
from os import mkdir, path
import aiofiles
from json import load
from aiohttp import ClientSession


def get_item_names() -> list[str]:
    with open("src/api/items.json", "r") as f:
        json = load(f)
    return list(json.keys())


async def download_item_icon(name: str) -> None:
    async with ClientSession() as session:
        async with session.get(f"https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react/items/{name}.png?") as r:
            if r.status != 200:
                return
            async with aiofiles.open(f"imgs/icons/items/{name}_icon.png", "wb") as f:
                await f.write(await r.read())


async def download_item_icons() -> None:
    if not path.exists("imgs/icons/items/"):
        mkdir("imgs/icons/items/")
    await gather(*[create_task(download_item_icon(name)) for name in get_item_names()])
