# 실패율

# 출처: https://rfriend.tistory.com/473 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]
# 딕셔너리 정렬 방법

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result = [3,4,2,1,5]

def solution(N, stages):
    answer = []
    person = len(stages)
    fail_rate = {}

    count = [stages.count(i) for i in range(1, N+1)]
    for i in range(len(count)):
        if count[i] == 0:
            fail = 0
        else:
            fail = count[i] / person
        person -= count[i]
        fail_rate[i+1] = fail     # {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0}

    fail_rate = sorted(fail_rate.items(), key = lambda item: item[1], reverse=True) # value: [1]
    for items in fail_rate:
        answer.append(items[0])

    return answer

print(solution(N, stages))