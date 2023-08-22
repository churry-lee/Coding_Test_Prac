from typing import *
import mypy
from itertools import product

def solution(num_cards, num_picked_cards, A_cards):
    answer = 0

    chul_dic = {}
    for num in range(len(A_cards)):
        chul_dic[num+1] = A_cards[num]

    print(chul_dic)
    young_dic = {}
    young_dic[num_cards] = chul_dic[num_cards] + 1
    num_picked_cards -= young_dic[num_cards]
    num = num_cards - 1
    while num:
        if num_picked_cards > chul_dic[num]:
            young_dic[num] = chul_dic[num] + 1
        else:
            break

        if num_picked_cards < young_dic[num]:
            break
        num_picked_cards -= young_dic[num]
        num -= 1

    print(num_picked_cards, num)
    young_dic[num] = num_picked_cards
    print(young_dic)

    chul_score = 0
    young_score = 0
    for num in range(1, num_cards+1):
        if chul_dic[num] < young_dic[num]:
            young_score += num
        elif chul_dic[num] > young_dic[num]:
            chul_score += num
        else:
            continue

    print(chul_score, young_score)
    if young_score > chul_score:
        return young_score - chul_score
    else:
        return -1



print(solution(4, 10, [5, 0, 2, 3]))
