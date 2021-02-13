# 삼각 달팽이

n = 10

def solution(n): 
    answer = [[] for _ in range(n)]
    for i in range(n):
        answer[i] = [0 for i in range(i+1)]
    val = 1
    x, y = 0, -1

    while n > 0:
        for _ in range(0, n):
            y += 1
            answer[y][x] = val
            val += 1
        n -= 1
        for _ in range(0, n):
            x += 1
            answer[y][x] = val
            val += 1
        n -= 1
        for _ in range(1, n+1):
            x -= 1
            y -= 1
            answer[y][x] = val
            val += 1
        n -= 1

    answer = [y for x in answer for y in x]

    return answer

print(solution(n))