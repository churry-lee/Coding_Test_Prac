C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    N = score[0]
    score_sum = sum(score[1:])
    score_avg = score_sum / N

    count = 0
    for j in score[1:]:
        if j > score_avg:
            count += 1

    rate = 100 * count / N

    print("{}%".format('%.3f'%rate))
