#!/usr/bin/python3

# 다익스트라 알고리즘

# N = 5
# road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
# K = 3

N = 6
road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 3], [3, 5, 2], [5, 6, 1]]
K = 4

# N = 6
# road = [[1, 2, 7], [1, 3, 9], [1, 6, 14], [2, 3, 10], [2, 4, 15], [3, 4, 11], [3, 6, 2], [6, 5, 9], [4, 5, 6]]

import heapq

def solution(N, road, K):
    routes = {}
    for i in road:
        routes[i[0]] = routes.get(i[0], []) + [(i[1], i[2])]
        routes[i[1]] = routes.get(i[1], []) + [(i[0], i[2])]
    print(routes)

    cost_dic = {1: 0}
    for i in range(2, N + 1):
        cost_dic[i] = float('inf')
    print(cost_dic, '\n')

    queue = []
    heapq.heappush(queue, [1, cost_dic[1]])
    print(queue)

    while queue:
        curr_node, dist = heapq.heappop(queue)
        for j in routes[curr_node]:
            dest, cost = j[0], j[1]
            if cost_dic[dest] > cost + dist:
                cost_dic[dest] = cost + dist
                heapq.heappush(queue, [dest, cost + dist])

    print(cost_dic)

    return len([i for i in cost_dic if cost_dic[i] <= K])

print(solution(N, road, K))
