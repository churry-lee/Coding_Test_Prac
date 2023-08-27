import sys
input_ = sys.stdin.readline
from collections import defaultdict


def find_max_common_friends(n: int, names_: list[str], friends_: list[tuple[str, str]]) -> (tuple[str, str], int):
    # 친구 목록 저장 그래프(무향 그래프)
    graph = defaultdict(list)
    for friend1, friend2 in friends_:
        graph[friend1].append(friend2)
        graph[friend2].append(friend1)
    
    friend_pair_ = ('', '')
    max_common_ = 0
    for i in range(n):
        for j in range(i+1, n):
            friend1, friend2 = names_[i], names_[j]
            common = 0
            
            # friend1의 친구 리스트를 순환
            for f1 in graph[friend1]:
                # friend2의 친구 리스트를 순환
                for f2 in graph[friend2]:
                    # friend1과 friend2가 공통 친구를 가진 경우
                    if f1 == f2:
                        common += 1
            
            # 갱신
            if common > max_common_ and friend2 not in graph[friend1]:
                max_common_ = common
                friend_pair_ = (friend1, friend2)
    
    return friend_pair_, max_common_


if __name__ == '__main__':
    N, M = map(int, input_().strip().split())
    names = list(map(str, input_().strip().split()))
    
    friends = []
    for _ in range(M):
        a, b = map(str, input_().strip().split())
        friends.append((a, b))
        
    friend_pair, max_common = find_max_common_friends(N, names, friends)
    print(*friend_pair)
    print(max_common)
