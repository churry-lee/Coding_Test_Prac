# 최대공약수 구하기

a = 4
b = 12

def common_divisor(a, b):
    i = min(a, b) # 두 수 중 작은 수를 나눠주는 첫번째 수로 지정
    while True:  # while 반복문을 참으로 설정해 계속 돌게 만들어줌
        if a % i == 0 and b % i == 0:  # i 로 두 수가 나누어 떨어지면 i를 리턴
            return i
        i = i - 1   # 나누어 떨어지지 않을 경우 i에서 1을 뺌을 반복

print(common_divisor(a, b))