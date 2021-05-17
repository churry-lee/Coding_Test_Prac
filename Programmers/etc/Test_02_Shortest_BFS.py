# 문제 URL: https://programmers.co.kr/learn/courses/30/lessons/1844

maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1], 
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

#maps = [[1, 0, 1, 1, 1],
#        [1, 0, 1, 0, 1], 
#        [1, 0, 1, 1, 1],
#        [1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 1]]

#maps = [[1, 0, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0], 
#        [1, 0, 1, 1, 1, 1],
#        [1, 0, 0, 0, 0, 1],
#        [1, 0, 0, 1, 1, 1],
#        [1, 0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1, 1]]

def solution(maps):
    answer = 1

    curr_x = 0
    curr_y = 0

    moves = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    n, m = len(maps)-1, len(maps[0])-1
    goal = [n, m]
    print(goal)

    visted = [[0, 0]]

    while True:
        curr = [curr_x, curr_y]
        print("curr: [{}, {}]".format(curr_x, curr_y), '\n')
        
        # 종료 조건
        if curr == goal:
            print("도착!!")
            break
        elif answer >= n*m:
            return -1

        for move in moves:
            next_x, next_y = 0, 0

            next_x = curr_x + move[0]
            next_y = curr_y + move[1]
            print("next: [{}, {}]".format(next_x, next_y))
        
            if 0 <= next_x <= n and 0 <= next_y <= m:
                if maps[next_x][next_y] == 0:
                    continue
                elif maps[next_x][next_y] == 1 and [next_x, next_y] not in visted:
                    visted.append([next_x, next_y])
                    curr_x, curr_y = next_x, next_y

        answer += 1

    return answer

print(solution(maps))
