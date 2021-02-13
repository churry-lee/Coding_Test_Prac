# 큐 문제(선입선출)
# 작업이 완료되는 앞에서부터 순서대로 배포되는 코드 작성
# 앞의 작업이 완료되어야지 작업이 배포 될 수 있음
# 작업은 작업속도에 따라서 진행이 됨

# 입출력 1
# progresses = [93, 30, 55]	
# speeds = [1, 30, 5]	# return [2, 1]
# 입출력 2
progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1] # return [1, 3, 2]

def solution(progresses, speeds):
    answer = []
       
    while progresses:
        count = 0
        while progresses[0] < 100:
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    continue
                else:
                    progress = progresses[i] + speeds[i]
                    progresses[i] = progress

        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)

        answer.append(count)

    return answer

print(solution(progresses, speeds))