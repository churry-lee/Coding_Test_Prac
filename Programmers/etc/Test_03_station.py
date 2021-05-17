# 문제 URL: https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3

# n: 아파트 개수
# station: 현재 기지국이 설치되어 있는 아파트의 위치 배열
# w: 전파의 도달 거리

#n = 11
#stations = [4, 11]
#w = 1
## answer = 3

n = 16
stations = [9]
w = 2
# answer = 3

def solution(n, stations, w):
    answer = 0

    temp = []
    coverage = []
    cover = w
    for station in stations:
        for i in range(station-w, station+w+1):
            coverage.append(i)
    print(coverage)

    temp = []
    new_cover = []
    for i in range(1, n+1):
        if i in coverage or len(temp) == ((2*w)+1):
            if temp:
                new_cover.append(temp)
                temp = []
        if i not in coverage:
            temp.append(i)
    
    if temp:
        new_cover.append(temp)

    print("new_cover: ", new_cover)

    return len(new_cover)

print(solution(n, stations, w))
