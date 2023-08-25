import sys
input_ = sys.stdin.readline
from collections import deque


def bfs(g, s, cache):
    if s in cache:
        return cache[s]
    
    n = len(g)
    dist = [-1] * (n + 1)
    dist[s] = 0

    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        # print(f"현재 노드: {v}")
        # print(f"현재 거리: {dist}")

        for x in g[v]:
            if dist[x] != -1:
                # print("통과")
                continue
            # print(f"다음 노드: {x}")
            dist[x] = dist[v] + 1
            # print(f"{x}까지 최단 거리: {dist[v] + 1}, 심리 거리: {abs(s - x)}")
            # print(f"갱신 거리: {dist}\n")
            q.append(x)

    # print(f"거리: {dist}")
    cache[s] = dist
    return cache[s]


def find_farthest_node(dist, s):
    for i in range(1, len(dist)):
        if dist[i] != -1:
            dist[i] = dist[i] + abs(i - s)

    # print(f"심리적 거리: {dist}")
    max_value = max(dist)
    if max_value == 0:
        return -1

    for i in reversed(range(len(dist))):
        if dist[i] == max_value:
            return i


if __name__ == '__main__':
    N, M, K = map(int, input_().strip().split())

    graph = {i: [] for i in range(1, N + 1)}
    # print(f"\n초기 그래프: {graph}")
    for _ in range(M):
        a, b = map(int, input_().strip().split())
        graph[a].append(b)
    # print(f"그래프: {graph}\n")
    
    bfs_cache = {}
    print(find_farthest_node(bfs(graph, K, bfs_cache), K))
