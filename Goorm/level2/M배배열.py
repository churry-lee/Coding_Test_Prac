import sys
input_ = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input_().strip().split())
    
    A = list(map(int, input_().strip().split()))
    print(A)
    
    for i in range(len(A)):
        if A[i] % M != 0:
            A[i] *= M
        print(A[i], end=' ')
    print()
