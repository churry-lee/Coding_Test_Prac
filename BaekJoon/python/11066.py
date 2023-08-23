# import sys
#
# T = int(sys.stdin.readline().strip())
#
# for _ in range(T):
#     K = int(sys.stdin.readline().strip())
#     files = list(map(int, sys.stdin.readline().strip().split()))
#
#     sum = [0 for _ in range(K+1)]
#     dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
#
#     # for i in range(K):
#     #     sum[i+1] = sum[i] + files[i]
#
#     for d in range(1, K):
#         for i in range(1, K - d + 1):
#             j = i + d
#             dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i,j)]) + sum[j] - sum[i-1]
#
#     print(dp[1][K])


# chatGPT
# O(n^3)
# def calculate_min_cost(files):
#     n = len(files)
#     dp = [[0] * n for _ in range(n)]  # dp[i][j]는 i부터 j까지의 파일을 합치는 최소비용을 저장하는 배열
#
#     for gap in range(1, n):
#         for i in range(n - gap):
#             j = i + gap
#             dp[i][j] = float('inf')  # 무한대로 초기화
#             for k in range(i, j):
#                 # 파일을 합치는 비용을 계산하고 최소값을 dp[i][j]에 저장
#                 cost = dp[i][k] + dp[k + 1][j] + sum(files[i:j + 1])
#                 dp[i][j] = min(dp[i][j], cost)
#
#     return dp[0][n - 1]
#
# # 메인 프로그램
# T = int(input())  # 테스트 케이스 수 입력
# for _ in range(T):
#     K = int(input())  # 장의 수 입력
#     file_sizes = list(map(int, input().split()))  # 파일 크기 입력
#     min_cost = calculate_min_cost(file_sizes)
#     print(min_cost)

# chatGPT
# O(n^2)
def calculate_min_cost(files):
    n = len(files)
    prefix_sum = [0] * (n + 1)  # 파일 크기의 누적 합을 저장하는 배열
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + files[i]
    
    dp = [[0] * n for _ in range(n)]  # dp[i][j]는 i부터 j까지의 파일을 합치는 최소비용을 저장하는 배열
    
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')  # 무한대로 초기화
            for k in range(i, j):
                # 파일을 합치는 비용을 계산하고 최소값을 dp[i][j]에 저장
                cost = dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

# 메인 프로그램
T = int(input())  # 테스트 케이스 수 입력
for _ in range(T):
    K = int(input())  # 장의 수 입력
    file_sizes = list(map(int, input().split()))  # 파일 크기 입력
    min_cost = calculate_min_cost(file_sizes)
    print(min_cost)

# 파이썬으로 할 경우 크누스 최적화를 써도 시간초과 됨
