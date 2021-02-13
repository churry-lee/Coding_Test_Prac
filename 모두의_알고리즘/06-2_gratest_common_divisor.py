# 유클리드 함수와, 재귀호출을 이용한 최대 공약수 풀이

a = int(input("첫 번째 입력 >> "))
b = int(input("두 번째 입력 >> "))

def Euclid(a, b):
    c = max(a, b) # 두 수 중 큰 값
    d = min(a, b) # 두 수 중 작은 값
    if d == 0:    # 작은 값이 0 이라면 종료가 되며 큰 값을 리턴
        return c
    return Euclid(d, c % d)

print(Euclid(a, b))