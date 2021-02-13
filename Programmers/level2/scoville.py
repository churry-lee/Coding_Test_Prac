# 리스트 내의 모든 원소가 지정 된 수(K) 이상이 되게 하여라
# 두 수 를 섞는 조건
# 섞은 수 = 가장 낮은 수 + (두 번 째로 가장 낮은 수 * 2)

scoville = [3, 2, 10, 9, 1, 12]
K = 100

def solution(scoville, K):
    answer = 0
    new_scoville = []

    while scoville:
        scoville.sort()
        if scoville[0] < K:
            if len(scoville) > 1:
                scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
                answer += 1
            else:
                return -1
        else:
            new_scoville.append(scoville.pop(0))

    return answer

print(solution(scoville, K))