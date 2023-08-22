from typing import *
import mypy
from itertools import product

def solution(change: int, coins: list[int]) -> int:
    for coin in coins:
        if change % sum(coins) == coin:
            return 1
    if change % sum(coins) == 0:
        return 1
    elif change % sum(coins) < max(coins):
        if (change % sum(coins)) % min(coins) == 0:
            return 1
        else:
            return 0
    else:
        return 0




print(solution(11, [3, 5]))
