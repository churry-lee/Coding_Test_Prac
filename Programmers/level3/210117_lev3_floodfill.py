#!/usr/bin/env python3

# bfs 알고리즘 사

n = 2
m = 3
images = [[1, 2, 3], [3, 2, 1]]

def bfs(i, j, n, m, images):
    q = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q.append([i, j, images[i][j]])
    images[i][j] = 0

    while q:
        i, j, area = q.pop(0)

        for x in range(4):
            nx = i + dx[x]
            ny = j + dy[x]

            if (0 <= nx) and (nx < n) and (0 <= ny) and (ny < m):
                if images[nx][ny] == area:
                    images[nx][ny] = 0
                    q.append([nx, ny, area])


def solution(n, m, images):
    answer = 0

    for i in range(n):
        for j in range(m):
            if images[i][j] != 0:
                bfs(i, j, n, m, images)
                answer += 1

    return answer

print(solution(n, m, images))
