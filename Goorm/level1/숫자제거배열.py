import sys
input_ = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(str, input_().strip().split())
    print(f"N: {N}, K: {K}")
    arr = list(map(int, input_().strip().split()))
    print(arr)
    ans = 0

    for a in arr:
        if K in str(a):
            continue
        ans += 1

    print(ans)
