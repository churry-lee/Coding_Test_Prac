T = int(input())
for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = list(map(int, input().split()))
    d = ((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2)
    r_sum = (r_1 + r_2) ** 2
    r_diff = (r_1 - r_2) ** 2

    # 좌표가 같은 경우
    if(d == 0):
        # 원이 겹칠때
        if(r_1 == r_2):
            print(-1)
        # 한 원이 다른 원을 포함하고 있는 경우
        else:
            print(0)
    # 좌표가 달라 원이 서로 떨어져 있는 경우
    else:
        # 한점만 겹치는 경우
        if((d == r_sum) or (d == r_diff)):
            print(1)
        # 겹치는 점이 2개인 경우
        elif((d < r_sum) and (d > r_diff)):
            print(2)
        # 아예 떨어져 있는 경우
        else:
            print(0)
