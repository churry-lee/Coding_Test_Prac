
n, m = 1, 100
#n, m = 100, 300

def solution(n, m):
    answer = 0

    for num in range(n, m+1):
        rev_num = list(str(num))
        rev_num.reverse()
        rev_num = ''.join(rev_num)

        if num == int(rev_num):
            answer += 1

    return answer

print(solution(n, m))
