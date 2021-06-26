# -*- coding: utf-8 -*-
# 증가 구간이 최대가 되도록 리스트 정렬
from typing import List, Deque
from collections import deque

def solution(p: List[int]) -> int:
    count: int = 0
    queue: Deque = deque()
    # 주어진 p list를 오름차순으로 정렬
    nums = sorted(p)
    answer: List = []

    # nums list에 원소가 있는 동안 무한 반복
    while nums:
        # 초기값으로 answer list에 현재 num list에서 가장 작은 값 추가
        answer.append(nums[0])

        # answer list에 숫자 추가
        # 현재 answer의 가장 마지막 원소가 비교 대상 num 보다 크거나 같으면, num은 queue에 저장
        # answer가 비어있거나 num이 더 크다면, 증가 순이 맞으므로, answer에 추가, 동시에 증가 구간 count+1
        for num in nums[1:]:
            if answer and answer[-1] >= num:
                queue.append(num)
                continue
            answer.append(num)
            count += 1
        # nums list를 현재 쌓인 queue로 갱신
        nums = []
        while queue:
            nums.append(queue.popleft())
        print(f'Answer: {answer}, nums: {nums}')

    return count

if __name__ ==  "__main__":
    #p = [3, 2, 1, 4, 5]
    #p = [2, 1, 1, 2]
    p = [3, 1, 3, 3, 1, 2, 0, 0, 1, 4]
    #p = [3, 2, 2, 1, 4]
    print(solution(p))
