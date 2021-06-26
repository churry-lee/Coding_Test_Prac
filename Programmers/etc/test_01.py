# -*- coding: utf-8 -*-
# 행렬의 시계방향 회전 알고리즘
from typing import List


class Rotation(object):
    def __init__(self, matrix: List[List[int]], rot_matrix: List[List[int]], N: int):
        self.matrix = matrix
        self.rot_matrix = rot_matrix
        self.N = N

    def rotation_90(self):
        for col in range(self.N):
            for row in range(self.N):
                self.rot_matrix[row][(self.N-1)-col] = self.matrix[col][row]
        return self.rot_matrix

    def rotation_180(self):
        for col in range(self.N):
            for row in range(self.N):
                self.rot_matrix[(self.N-1)-row][(self.N-1)-col] = self.matrix[col][row]
        return self.rot_matrix

    def rotation_270(self):
        for col in range(self.N):
            for row in range(self.N):
                self.rot_matrix[(self.N-1)-row][col] = self.matrix[col][row]
        return self.rot_matrix

    def rotation_360(self):
        return self.matrix


def solution(matrix: List[List], r: int) -> List[List]:
    N = len(matrix)
    rot_matrix: List = [[0] * N for _ in range(N)]
    rot = Rotation(matrix, rot_matrix, N)

    if r % 4 == 1:
        print('--- 90 degree rotation ---')
        return rot.rotation_90()
    elif r % 4 == 2:
        print('--- 180 degree rotation ---')
        return rot.rotation_180()
    elif r % 4 == 3:
        print('--- 270 degree rotation ---')
        return rot.rotation_270()
    else:
        print('--- 3600 degree rotation ---')
        return rot.rotation_360()


if __name__ == '__main__':
    #matrix = [[1, 2], [3, 4]]
    #r = 1
    #matrix = [[1, 2], [3, 4]]
    #r = 2
    matrix = [[4, 1, 2], [7, 3, 4], [3, 5, 6]]
    r = 3
    print(solution(matrix, r))
