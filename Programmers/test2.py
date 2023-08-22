from typing import *
import mypy
from itertools import product

import operator
from collections import deque

def count(queue):
    dic = {
        1: 0,
        2: 0,
        3: 0,
    }
    for num in queue:
        dic[num] += 1
    return dic

def solution(queue):
    answer = [0, 0, 0]
    queue = deque(queue)

    count_dic = count(queue)
    while True:
        if count_dic[1] == count_dic[2] == count_dic[3]:
            break
        count_dic[queue.popleft()] -= 1
        min_by_value = min(count_dic.items(), key=operator.itemgetter(1))
        queue.append(min_by_value[0])
        count_dic[min_by_value[0]] += 1
        answer[min_by_value[0]-1] += 1


    return answer



print(solution([2, 1, 3, 1, 2, 1]))
# print(solution([3, 3, 3, 3, 3, 3]))
# print(solution([1, 2, 3]))
