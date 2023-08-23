A, B, C = map(int, input().split())

if (B <= A <= C) or (B >= A >= C):
    print(A)
elif (A <= B <= C) or (A >= B >= C):
    print(B)
else:
    print(C)
