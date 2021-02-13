# 소수 찾기
# 주어진 숫자의 조합으로 만들 수 있는 소수의 개수를 반환라라
# numbers = "17", 만들 수 있는 소수: [7, 17, 71] return 3

numbers = '011' # return 3
# numbers = '011' # return 2  [11, 101]

# 메인 함수
def solution(numbers):
    answer = 0
    nums = [i for i in numbers]       

    permute = dfs(nums)
    permute = list(set([int(''.join(i)) for i in permute]))
    print(permute)
    prime = [2] + list(prime_number(max(permute)+1))
    print(prime)

    for i in permute:
        if i in prime:
            answer += 1
    return answer

# 에라토스테네스의 체 함수
def prime_number(n):
    num = set([i for i in range(3, n + 1, 2)])
    for i in range(3, n+1, 2):
        if i in num:
            num -= set([i for i in range(i * 2, n + 1, i)])
    return num

# 순열 함수
# 파이썬 알고리즘 인터뷰 p341 순열 풀이 참조
# 재귀를 이용해 요소를 삭제하고 추가하기를 반복하며 순열 도출
result = []
prev_elements = [] 
def dfs(elements):
    for e in elements:
        next_elements = elements[:]  # [:] 리스트 전체 복사 = copy()
        next_elements.remove(e)
        prev_elements.append(e)
        result.append(prev_elements[:])

        dfs(next_elements)

        prev_elements.pop()
    return result

print(solution(numbers))