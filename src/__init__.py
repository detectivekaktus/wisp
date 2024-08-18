#!/usr/bin/env python3
from os import getenv
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN: Optional[str] = getenv("DISCORD_TOKEN")
