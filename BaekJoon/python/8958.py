N = int(input())

for i in range(N):
    score = 0
    acc = 0
    OX = input()
    
    for j in OX:
        if j == "O":
            acc += 1
            score += acc
        elif j == "X":
            score += 0
            acc = 0

    print(score)
