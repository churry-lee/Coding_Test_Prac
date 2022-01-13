N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

New_sum = 0

for score in scores:
    New_score = score/M * 100
    New_sum += New_score

New_avg = New_sum / N

print(New_avg)
