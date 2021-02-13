#!/usr/bin/python3

# x: -5 ~ 5, y: -5 ~ 5 의 크기를 갖는 좌표평면에서 캐릭터를 이동시켜,
# 처음 가본 길의 수를 구하라.

#dirs = "ULURRDLLU"  # answer = 7
#dirs = "LULLLLLLU"   # answer = 7
dirs = "LLLLLLLRRRRR"

#U = (0, 1)
#D = (0, -1)
#R = (1, 0)
#L = (-1, 0)

def solution(dirs):
    answer = []

    curr = [0, 0]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    pathes = []
    
    count = 0
    for dir in dirs:
        new = [0, 0]
        count += 1
        if dir == 'U':
            dir = move[0]
        elif dir == 'D':
            dir = move[1]
        elif dir == 'R':
            dir = move[2]
        else:
            dir = move[3]

        new[0] = curr[0] + dir[0]
        new[1] = curr[1] + dir[1]

        print("{}. curr: {} + dir: {} = new: {}".format(count, curr, dir, new))
        if (new[0] > 5 or new[0] < -5) or (new[1] > 5 or new[1] < -5):
            new = curr
        if new != curr:
            pathes.append([tuple(curr), tuple(new)])
        curr = new

    for path in pathes:
        path = sorted(path)
        print(path)
        if not answer or path not in answer:
            answer.append(path)
            print(answer)


    return len(answer)

print(solution(dirs))
