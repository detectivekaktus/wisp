#!/usr/bin/env python3
from asyncio import run
from sys import argv
from typing import cast
from src import DEBUG_TOKEN, DISCORD_TOKEN
from src.client import bot
from src.datagen.icons import download_hero_icons
from src.datagen.items import download_item_icons


def usage() -> None:
    print(f"Usage: {argv[0]} [run | debug | gen]    ")
    print("  run:   run the bot                     ") 
    print("  debug: debug the the bot               ")
    print("  gen:   generates the data for the bot  ")
    print("    heroes: generates the hero icons     ")
    print("    items: geenrates the item icons      ")


def crash(msg: str) -> None:
    print(msg)
    usage()
    exit(1)


def main() -> None:
    if len(argv) < 2:
        crash("Not enough arguments.")

    ap: int = 1
    if argv[ap] == "run":
        if not DISCORD_TOKEN:
            crash("'DISCORD_TOKEN' environment variable is not set up properly.")
        bot.run(cast(str, DISCORD_TOKEN))
    elif argv[ap] == "debug":
        if not DEBUG_TOKEN:
            crash("'DEBUG_TOKEN' environment variable is not set up properly.")
        crash("Not implemented")
    elif argv[ap] == "gen":
        ap += 1
        if argv[ap] == "heroes":
            run(download_hero_icons())
        elif argv[ap] == "items":
            run(download_item_icons())
        else:
            crash(f"Unknown subcommand {argv[ap]} for `gen` commmand")
    else:
        crash(f"Unknown command {argv[ap]}")


if __name__ == "__main__":
    main()
