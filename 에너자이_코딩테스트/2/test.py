from typing import *
import mypy

def solution(num_to_win: int, win_ratioA: float, num_winA: int, num_winB: int):
    answer = 0.0

    a = num_to_win - num_winA
    b = num_to_win - num_winB - 1

    answer = 1 - (win_ratioA ** a) * ((1 - win_ratioA) ** b)


    return int(answer * 10000)

print(solution(5, 0.5, 4, 2))  # 8750
print(solution(7, 0.7, 2, 5))  # 4201

