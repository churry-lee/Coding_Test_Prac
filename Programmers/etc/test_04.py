# -*- coding: utf-8 -*-
# 주어진 퀘스트의 선 후행 순서에 맞게 퀘스트 리스트 정렬(관계가 없을 시 번호순 정렬)
from typing import List, Dict


# 깊이 우선 탐색을 이용하여 퀘스트 클리어 순서 확인
def dfs(ord_dic: Dict) -> List:
    # 순서에 맞게 clear한 퀘스트를 저장하기 위한 리스트 선언
    clear: List = []
    stack: List = [1]
    while stack:
        curr = stack.pop()
        if curr not in clear:
            clear.append(curr)
            for _next in ord_dic[curr]:
                stack.append(_next)
    return clear


def solution(n: int, quests: List[List[int]]) -> List:
    ord_dic: Dict = {}

    # 주어진 퀘스트 조건 중에 선행 퀘스트가 필요없는 퀘스트를 확인
    temp = [q for quest in quests for q in quest]
    for i in range(1, n+1):
        # 퀘스트 목록에 없는 퀘스트가 있을 시, 번호 순대로 클리어하기 위해 임의로 선행 퀘스트를 바로 앞 번호로 부여
        if i not in temp:
            quests.append([i-1, i])
    # 반복문을 이용한 깊이 우선 탐색을 하기 위해, 후행 퀘스트를 기준으로 내림차순으로 정렬
    quests = sorted(quests, key=lambda x: x[1], reverse=True)
    # key: 선행 퀘스트, value: 후행 퀘스트 리스트로 딕셔너리로 변환
    # 그래프 탐색을 위해 리스트를 그래프화하기 위함
    for quest in quests:
        if quest[0] not in ord_dic:
            ord_dic[quest[0]] = [quest[1]]
        elif quest[0] in ord_dic:
            ord_dic[quest[0]] += [quest[1]]
    # 후행 퀘스트가 없는 퀘스트는,
    # value를 빈리스트로 하여 딕셔너리에 저장
    for i in range(1, n+1):
        if i not in ord_dic:
            ord_dic[i] = []

    print(f'퀘스트 순서: {ord_dic}')

    return dfs(ord_dic)


if __name__ == "__main__":
    n = 5
    quests = [[1, 3], [1, 4], [3, 5], [5, 4]]
    print(solution(n, quests))
