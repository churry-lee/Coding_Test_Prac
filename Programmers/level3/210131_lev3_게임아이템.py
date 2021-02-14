healths = [200, 120, 150]
items = [[30, 100], [500, 30], [100, 400]]
# return [1, 2]

#healths = [300, 200, 500]
#items = [[1000, 600], [400, 500], [300, 100]]
# return [3]

from heapq import heappush, heappop


def solution(healths, items):
    answer = []
    candi = []

    healths = sorted(healths) # [120, 150, 200]
    items = sorted([(item[1], item[0], i+1) for i, item in enumerate(items)])
    # [(30, 500, 2), (100, 30, 1), (400, 100, 3)]

    for health in healths:
        while items:
            debuff, buff, index = items[0]
            if health - items[0][0] < 100:
                break
            items.pop(0)
            heappush(candi, (-buff, index))
        if candi:
            _, index = heappop(candi)
            answer.append(index)

    return sorted(answer)


print(solution(healths, items))
