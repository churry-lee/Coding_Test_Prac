# 재귀함수를 이용한 factorial 구하기
n = 4

def fact(n):
    if n <= 1:    # 종료 조건 필
        return 1
    return n * fact(n - 1)

print(fact(n))
