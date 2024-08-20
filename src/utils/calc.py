#!/usr/bin/env python3
from typing import Optional


def calculate_winrate(wins: int, loses: Optional[int] = None, total: Optional[int] = None) -> float:
    if loses:
        total_matches = wins + loses
        return 0.0 if total_matches == 0 else round(wins / total_matches * 100, 2)
    elif total:
        return 0.0 if total == 0 else round(wins / total * 100, 2)
    return 0.0
