# 주어진 리스트로 가장 큰 수를 만들어라
# 숫자를 문자로 바꾼 후 정렬을 하면
# index 0 ~ 숫자의 대소를 비교하여 정렬하게 됨
# ex) 9, 12, 13, 122, 91   =>   91, 9, 13, 122, 12
# 각 숫자(문자형으로 치환된)를 늘려서 비교를 해주면(문제에서는 각 원소가 1,000 이하이므로 *3)
# 일의 자리 수인 index 0 과 다른 길이를 가진 원소들과 비교가 가능하다

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x : x * 3, reverse=True)

    answer = str(int(''.join(numbers)))   # 리스트 내 모든 원소가 0 일 경우에 
                                          # 그냥 ''.join()으로 출력하면 '0000 -' 이 되기 때문에
                                          # 숫자로 변형하여 0으로 만든 후 다시 문자열로 반환

    return answer

#numbers = [6, 10, 2]
#numbers = [3, 30, 34, 5, 9]  # return '9534330'
numbers = [0, 0]

print(solution(numbers))