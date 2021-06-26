# -*- coding: utf-8 -*-
# 로봇이 장애물을 제거하던 돌아서 가던 목적지까지 도달하는데 필요한 최소비용
# 장애물 제거 cost: c
# 로봇이 있는 위치: 2, 장애물: 1, 아무것도 없는 곳: 0, 목적지(보석): 3

from typing import List, Tuple, Any
import heapq


class Solution(object):
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.N = len(board)
        self.M = len(board[0])

    # 광물(gem)와 로봇(agent)의 위치 정의
    def define_position(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == 2:
                    agent = (agent_x, agent_y) = j, i
                elif self.board[i][j] == 3:
                    gem = (gem_x, gem_y) = j, i
        return agent, gem

    # 우선순위 큐를 이용한 너비 우선 탐색
    def BFS_heapq(self, heap: List[Any], goal: Tuple, c: int) -> int:
        # agent의 이동방향
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while heap:
            cost, curr_x, curr_y = heapq.heappop(heap)

            for i in range(4):
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]
                # 종료 조건, 이동할 예정 지점이 목적지와 같다면 종료
                if (next_x, next_y) == (goal[0], goal[1]):
                    # 아직 이동한 것은 아니므로, cost에 1을 더해서 반환
                    return cost+1
                # 탐색 조건
                elif (0 <= next_x < self.M) and (0 <= next_y < self.N) and (self.board[next_y][next_x] == 0 or 1):
                    # 다음 노드가 빈칸일 경우
                    if self.board[next_y][next_x] == 0:
                        heapq.heappush(heap, (cost+1, next_x, next_y))
                    # 다음 노드가 장애물이 있을 경우
                    elif self.board[next_y][next_x] == 1:
                        heapq.heappush(heap, (cost+1+c, next_x, next_y))
                    # 방문한 노드의 값을 2로 갱신
                    self.board[next_y][next_x] = 2
        return -1


def solution(board: List[List], c: int) -> int:
    cost: int = 0

    sol = Solution(board)
    curr, goal = sol.define_position()
    # cost가 낮은 순으로 추출하기 위해, 즉 우선순의 큐를 활용하기 위해 heap 자료 구조 사용
    heap: List = []
    heapq.heappush(heap, (cost, curr[0], curr[1]))

    return sol.BFS_heapq(heap, goal, c)


if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]
    ]
    #c = 1
    c = 2
    # board = [
    #    [0, 0, 2, 0, 0],
    #    [0, 1, 1, 1, 0],
    #    [0, 1, 0, 1, 0],
    #    [0, 1, 1, 1, 0],
    #    [0, 1, 3, 1, 0]
    # ]
    print(solution(board, c))
