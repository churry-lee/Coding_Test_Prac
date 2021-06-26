# -*- coding: utf-8 -*-
# 비용이 최소가 되도록 노드 방문(주어진 sequence 리스트는 순환 구조임)
from typing import List


def solution(N: int, sequence: List[int]) -> int:
    answer: int = 0
    curr: int = 1

    for visit in sequence:
        # 전체 그래프가 순회하는 구조이기 때문에 더 작은 비용을 추출하기 위해
        # 현재 위치와 방문할 위치의 순서에 따라서 다른 계산 적용
        if curr < visit:
            _min = min((visit - curr), (N - visit) + curr)
        else:
            _min = min((curr - visit), ((N - curr) + visit))
        print(f'curr {curr} visit {visit}')
        print("----", _min)
        answer += _min
        curr = visit

    return answer


if __name__ == "__main__":
    N = 5
    #sequence = [1, 2, 3, 4, 5]
    sequence = [3, 5, 4, 1, 2]
    #sequence = [5, 1, 4, 3, 2]

    print(solution(N, sequence))
