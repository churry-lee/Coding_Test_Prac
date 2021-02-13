# 리트코드 561
# 배열 파티션
# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라


list_a = [1, 4, 3, 2]

list_a.sort()
# list_a = [1, 2, 3, 4]
sum_min = 0
for i in range(0, len(list_a), 2):
    sum_min = list_a[i] + sum_min

print(sum_min)