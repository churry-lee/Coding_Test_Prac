#!/usr/bin/env python3

# 2020 카카오 블라이든 채용 기출문제
# 주어진 문자열을 반복되는 것끼리 묶어서 표현할 수 있는 가장 짧은 문자열의 길이를 구하라
# ex)
# s = aabbaccc => 2a2ba3c return 7
# s = ababcdcdababcdcd => 2ababcdcd return 9

# s = 'aabbaccc'
s = 'ababcdcdababcdcd'

def solution(s):
    answer = []  # 일정 문자열만큼의 길이로 잘라서 압축한 문자열의 길이를 저장하기 위한 변수
    length = 1   # 문자열을 일정 길이만큼 자르기 위한 변수 설정
    # stepd이 1씩 증가하는 loop이기 때문에 for 문을 쓰는 것이 더 좋음
    while length <= len(s) // 2 + 1:   # 압축을 위한 문자열의 길이를 늘려가며 반복문 수행 
        stack = []  # 압축 가능 판별을 위한 스택
        tmp = []  # 압축된 문자열을 저장하기 위한 리스트, tmp와 같은 변수는 지양
        # 원하는 길이로 자른 문자열을 리스트로 저장
        list_s = []
        for i in range(0, len(s), length):
            list_s.append(s[i : i + length])
        
        count = 1  # 반복되는 문자열의 개수를 저장하기 위한 변수
        for char in list_s:
            if stack and stack[-1] == char: # stack된 문자와 같으면 count에 1을 더하고, stack 되어있는 문자 제거
                count += 1                  # 밑에서 다시 stack이 되므로,,,, 굳이 이렇게 해야 할까...?
                stack.pop()                 # 마지막 문자열만 알면 되기 때문에, 굳이 stack으로 관리 안해도 됨
            elif stack and stack[-1] != char:  # stack 되어 있는 문자와 다르면, 이 문자는 더 이상 반복이 없으므로,
                if count != 1:                 # count 가 1이 아니라면, count와 함께 stack 되어 있는 문자를 제거하며,
                    tmp.append(str(count) + stack.pop())  # 압축 문자열 저장 리스트인 tmp에 저장
                    # tmp += str(count) + stack.pop() # tmp는 추후 join을 통해 문자열로 만드는 것이 목적이기 때문에 바로 문자열로 관리해도 됨
                    count = 1                           # 그리고 다시 count는 1로 초기화
                else:
                    tmp.append(stack.pop())    # count가 1이라면 문자만 저장
            stack.append(char)
        if stack:        # 모든 문자 압축 후 스택에 남아있는 문자가 있다면, count 개수 확인 후 tmp에 저장
            if count != 1:
                tmp.append(str(count) + stack.pop())
            else:
                tmp.append(stack.pop())

        # print('stack', stack)
        # print('tmp', tmp)
        # answer = min(answer, len(''.join(tmp)) # answer를 굳이 list로 관리하지 않고 바로바로 갱신하는 것이 좋음
        answer.append(len(''.join(tmp))) # 압축된 문자열이 저장된 tmp 리스트를 문자열로 변환해 길이를 저장
        length += 1 # 길이를 1 늘려서 다시 반복 수행

    return min(answer) # 저장된 길이 중 최솟값을 반환

print(solution(s))


'''
# 멘토님 풀이

def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0

        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                count += 1
            else:
                compress += size + len(str(count)) if 1 < count else len(prev)
                prev = curr
                count = 1
        answer = min(answer, compress)

    return answer
'''
