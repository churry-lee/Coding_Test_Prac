# 비밀지도
# 비트연산자!!!!!

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(
            bin(arr1[i] | arr2[i])[2:].zfill(n)
            .replace('1', '#')
            .replace('0', ' ')
        )

    return answer

print(solution(n, arr1, arr2))