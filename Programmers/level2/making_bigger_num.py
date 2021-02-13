# 숫자의 순서는 유지한 상태로 가장 큰 수를 만들어야함
# 그러므로 앞에서부터 차례대로 요구하는 숫자의 개수 만큼 작은 숫자를 제거해 나가면 됨
# 문자열의 숫자를 차례대로 스택하며 대소 비교
# 알고리즘_베이직에서 03-1_find_max의 응용
# 초기 스택값보다 작은 수가 나올 경우 그대로 스택
# 직전에 스택된 숫자보다 큰 수가 나올 경우 앞의 숫자들을 제거하고 새로운 큰 수 스택


def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) > 0 and num > answer[-1] and k > 0:
            k -= 1
            answer.pop()
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)


print(solution('4177252841', 4))