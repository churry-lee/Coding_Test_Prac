#!/usr/bin/python3

# level 2. 주사위 게임
# 몬스터가 있는 위 배열: monster
# 각 주사위 당 나올 수 있는 최대 수: S1, S2, S3
# 세 개의 주사위를 던진 수의 합만큼 전진해 monster가 없을 확률을 구하라
# return = monster가 없을 확률 * 1000 (소수부 제외)

'''
from itertools import product

def solution(monster, S1, S2, S3):
    p = product(range(S1), range(S2), range(S3))
    case = len([x for x in p if sum(x) + 4 not in monster])
    return int(case / (S1 * S2 * S3) * 1000)
'''



monster = [4, 9, 5, 8]
S1, S2, S3 = 2, 3, 4    # return 500

def solution(monster, S1, S2, S3):
    success = 0
    all_case_num = S1 * S2 * S3

    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                if i+j+k+1 not in monster:
                    success += 1
                else:
                    continue
    # print(success)
    # print(all_case_num)
    # print(success/all_case_num)

    return int(success/all_case_num * 1000)

print(solution(monster, S1, S2, S3))
