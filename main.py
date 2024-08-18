#!/usr/bin/env python3
from sys import argv
from typing import cast
from src import DEBUG_TOKEN, DISCORD_TOKEN
from src.client import bot


def usage() -> None:
    print(f"Usage: {argv[0]} [run | debug]  ")
    print("  run:   run the bot             ") 
    print("  debug: debug the the bot       ")


def crash(msg: str) -> None:
    print(msg)
    usage()
    exit(1)


if __name__ == "__main__":
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
    else:
        crash(f"Unknown command {argv[ap]}")
