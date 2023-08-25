import sys
input_ = sys.stdin.readline


def sort_event(event_):
    event_items = list(event_.items())
    n = len(event_)
    
    for i in range(n):
        for j in range(0, n-1-i):
            if event_items[j][1] < event_items[j + 1][1]:    # 요소 비교
                event_items[j], event_items[j + 1] = event_items[j + 1], event_items[j]    # 요소 교환
    
    return dict(event_items)


def find_max_event(event_):
    # print(event_)
    
    idx_list = []
    max_ = 0
    for key, value in event_.items():
        if max_ <= value:
            max_ = value
            idx_list.append(key)
    
    return ' '.join(str(n) for n in sorted(idx_list, reverse=True))


if __name__ == '__main__':
    N, M = map(int, input_().strip().split())
    
    event = {i+1: 0 for i in range(M)}
    for i in range(M):
        a = list(map(int, input_().strip().split()))
        for j in range(1, len(a)):
            event[a[j]] += 1
            
    print(find_max_event(sort_event(event)))
    # print(find_max_event(event))

"""
# ai가 작성해준 최적화된 알고리즘
import sys
from collections import Counter
input_ = sys.stdin.readline

def find_max_event(counter):
    max_val = counter.most_common(1)[0][1]  # 가장 많이 등장하는 원소의 빈도수
    max_keys = [k for k, v in counter.items() if v == max_val]
    return ' '.join(str(k) for k in sorted(max_keys, reverse=True))


if __name__ == '__main__':
    N, M = map(int, input_().strip().split())
    
    event = Counter()
    for _ in range(M):
        a = list(map(int, input_().strip().split()))
        for j in a[1:]:
            event[j] += 1
    print(find_max_event(event))
"""
