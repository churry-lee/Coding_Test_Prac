# 리트코드 739
# 매일의 온도 리스트를 입력 받아서, 
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

T = [73, 74, 75, 71, 69, 72, 76, 73]    # return [1, 1, 4, 2, 1, 1, 0, 0]

'''
시간 초과 

def dailyTemperatures(T):
    answer = [0] * len(T)

    for day, cur in enumerate(T):
        for i in range(day+1, len(T)):
            if cur < T[i]:
                answer[day] = i - day
                break

    return answer

print(dailyTemperatures(T))
'''

def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []

    for day, cur in enumerate(T):
        print('{}, {} 일 때'.format(day, cur))
        while stack and T[stack[-1]] < cur:
            print('T[stack[-1]] < cur => T[{}] < cur => {} < {}'.format(stack[-1], T[stack[-1]], cur))
            last = stack.pop()
            answer[last] = day - last
            print('answer[last] = day - last => answer[{}] = {} - {} = {}'.format(last, day, last, answer[last]))
        stack.append(day)
        print('stack', stack, '\n')

    return answer

print(dailyTemperatures(T))