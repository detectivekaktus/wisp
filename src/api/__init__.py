#!/usr/bin/env python3
from typing import Any
from aiohttp import ClientSession


async def get(session: ClientSession, url: str) -> Any:
    async with session.get(url) as r:
        if r.status == 200:
            return await r.json()
        return None


async def post(session: ClientSession, url: str) -> int:
    async with session.post(url) as r:
        return r.status
