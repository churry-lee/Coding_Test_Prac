# LIS 구하기
def LIS(arr):
    from bisect import bisect_left
    lis = []
    for num in arr:
        pos = bisect_left(lis, num)
        if len(lis) <= pos:
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

# 스탈린 정렬로 제거되는 개수 구하기
def stalin(arr):
    max_val = arr[0]
    remove_count = 0
    for num in arr:
        if num >= max_val:
            max_val = num
        else:
            remove_count += 1
    return remove_count

# 입력받기
n = int(input().strip())
sequence = list(map(int,input().strip().split()))

# 최소 제거 개수 구하기
print(min(n - LIS(sequence), stalin(sequence)))
