from typing import *
import mypy
from itertools import product

def solution(histogram: list) -> int:
    answer = 1
    rows = len(histogram)
    cols = len(histogram[0])

    hist_height = {}
    for col in range(cols):
        hist_height[col] = []


    for col in range(cols):
        for row in range(rows-1, -1, -1):
            print(histogram[row][col])
            if histogram[row][col] == 0:
                break
            elif histogram[row][col] == 1:
                hist_height[col] = rows - row - 1
            elif histogram[row][col] == 2:
                if row != rows-1 and histogram[row+1][col] == 1:
                    hist_height[col] = [rows - row - 1]
                else:
                    hist_height[col].append(rows - row - 1)


    print(hist_height)

    for key in hist_height:
        if type(hist_height[key]) == type(1):
            continue
        else:
            answer = answer * (len(hist_height[key]) + 1)

    return answer



# print(solution([[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1], [1, 1, 2, 2, 1, 0, 1], [2, 2, 2, 2, 1, 2, 2], [2, 2, 1, 1, 1, 2, 2, ], [2, 2, 1, 1, 1, 2, 2]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2, 2, 0, 0, 0], [1, 0, 1, 0, 0], [2, 1, 2, 2, 2], [2, 1, 2, 2, 2]]))
