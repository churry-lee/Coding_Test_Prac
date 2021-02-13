# 중요도 순서대로 인쇄되는 프린터
# 알고싶은 위치(location)에 있는 인쇄가 몇번째로 인쇄되는지 리턴
# 숫자가 높을 수록 중요도 높음

priorities = [2, 1, 3, 2]
location = 2  # return 1
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0  # return 5

def solution(priorities, location):
    answer = 0
    priorities = list(enumerate(priorities))

    while priorities:
        init = priorities[0]
        print('init', init)
        for priority in priorities[1:]:
            if init[1] < priority[1]:
                priorities.append(init)
                break
            else:
                continue
        priorities.pop(0)
        print(priorities)
        if init not in priorities:
            answer += 1
            print(answer)
            if location == init[0]:
                return answer
        

print(solution(priorities, location))