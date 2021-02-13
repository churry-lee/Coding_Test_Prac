from collections import deque
# 주식가격 배열을 보고 가격이 떨어지지 않은 시간(초)를 구하라

prices = [1, 2, 3, 2, 3]  #  초 단위로 입력된 주식 가격
# 1초 - 1원은 배열이 끝날 때까지 4초간 가격이 떨어지지 않음
# 2초 - 2원도 3초간 가격이 안 떨어짐
# 3초 - 3원은 1초동안 가격이 떨어지고 다음 2초에 가격 상승
# 4초 - 2원은 1초간 가격이 안떨어짐
# 5초 - 3원은 0초간 가격이 안떨어짐
# return = [4, 3, 1, 1, 0]


# 이중 구문 풀이
# answer = [0 for i in range(len(prices))]

#     for i in range(len(prices)-1):
#         for j in range(i+1, len(prices)):
#             answer[i] += 1
#             if prices[i] > prices[j]:
#                 break

# 스택/큐 풀이
def solution(prices):
    answer = []
    prices_q = deque(prices)

    while prices_q:
        time = 0
        tmp = prices_q[0]
        prices_q.popleft()

        for price in prices_q:
            time += 1
            if tmp > price:
                break
        answer.append(time)

    return answer

print(solution(prices))