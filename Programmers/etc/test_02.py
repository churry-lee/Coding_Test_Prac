# -*- coding: utf-8 -*-
# 기계가 좌표를 따라 움직일 때 생기는 동선에서 보이는 1*1 크기의 정사각형의 개수
from typing import List, Dict, Deque, Tuple
from collections import deque, defaultdict


class Move(object):
    def __init__(self):
        self.paths: Dict = defaultdict(tuple)

    # 이동 방향에 따라 중복되는 선을 통일되게 표시하기 위해서
    # (작은 노드) -> (큰 노드)로 key 저장
    def move_up(self, x: int, y: int):
        self.paths[(x, y), (x, y+1)] = False
        return self.paths, y+1

    def move_down(self, x: int, y: int):
        self.paths[(x, y-1), (x, y)] = False
        return self.paths, y-1

    def move_right(self, x: int, y: int):
        self.paths[(x, y), (x+1, y)] = False
        return self.paths, x+1

    def move_left(self, x: int, y: int):
        self.paths[(x-1, y), (x, y)] = False
        return self.paths, x-1

    def making_path(self, moves: List[str]):
        curr_x: int = 0
        curr_y: int = 0
        stack: List = []
        stack.append((curr_x, curr_y))

        for move in moves:
            if move == "U":
                paths, curr_y = self.move_up(curr_x, curr_y)
            elif move == "D":
                paths, curr_y = self.move_down(curr_x, curr_y)
            elif move == "R":
                paths, curr_x = self.move_right(curr_x, curr_y)
            elif move == "L":
                paths, curr_x = self.move_left(curr_x, curr_y)
            _next = (curr_x, curr_y)
            stack.append(_next)
        return stack, paths


# 한 지점으로 부터 이미 방문한 적이 있는 노드를 방문하는데,
# 새로운 경로를 이용해서 그 노드에 방문할 때까지 탐색
# 각 노드를 따라 원하는 조건의 사각형 방이 생길 때까지 각각 검사하기 위해 깊이 우선 탐색을 이용
def DFS(stack, paths):
    # 1*1 사각형 개수 변수
    room: int = 0
    # 방문한 전체 노드를 저장하기 위한 딕셔너리
    # key: node
    # value: bool
    visited: Dict = defaultdict(bool)
    curr = stack.pop()
    visited[curr] = True

    # 추출한 스택의 하나의 요소에 대한, 탐색에 의해 지나온 노드를 저장하기 위한 리스트
    # 탐색이 한 번 종료되면 초기화
    nodes: List = [curr]

    while stack:
        _next = stack.pop()

        # 탐색 종료 조건
        if visited[_next] == True:
            # 새로운 경로로 이미 방문했던 노드를 방문한고,
            # 한 탐색에서 방문한 노드의 개수가 5개 미만이라면,
            # 한 탐색에서 1*1 사각형이 만들어지려면 필요한 노드의 최대 개수는 5개이다.
            if paths[min(curr, _next), max(curr, _next)] == False and len(nodes) < 5:
                room += 1
            # 1*1 사각형이 없을 경우 초기화
            nodes = []
        else:
            # 방문했던 노드임을 표시하기 위해 visited 딕셔너리에 새로운 key로 저장을 하며, True로 갱신
            visited[_next] = True
            # 한 탐색에 대한 방문 노드 저장
            nodes.append(_next)
        # 이미 지나간 길임을 표시하기 위해 True로 갱신
        paths[min(curr, _next), max(curr, _next)] = True
        # 노드 갱신
        curr = _next
    return room


def solution(moves: List[str]) -> int:
    # agent가 격자선을 따라 움직이면서 만든 동선 정의
    move = Move()
    # stack: 움직인 노드 저장
    # paths: 움직인 경로 저장
    stack, paths = move.making_path(moves)
    return DFS(stack, paths)


if __name__ == '__main__':
    #moves = ["U", "R", "D", "L", "U", "R", "D", "L"]
    #moves = ["U", "U", "R", "D", "L", "L", "L", "U", "R",
    #         "D", "D", "D", "L", "U", "R", "R", "R", "D", "L", "U"]
    #moves = ["U", "L", "D", "R", "R", "D", "D", "L", "U", "U"]
    #moves = ["U"]
    #moves = ["U", "R", "R", "D", "L", "U"]
    #moves = ["R", "R", "R", "U", "L", "L", "D", "R", "U"]
    moves = ["U", "U", "U", "R", "D", "L"]
    print(solution(moves))
