def matMul(A, B):
    res = []
    m = len(A)
    n = len(B[0])
    for i in range(m):
        res.append([])
        for j in range(n):
            res[i].append(0)
            for k in range(len(B)):
                res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % 1000
    
    return res


def power(A, B):
    if B == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    else:
        tmp = power(A, B // 2)
        if B % 2 == 0:
            return matMul(tmp, tmp)
        else:
            return matMul(matMul(tmp, tmp), A)


N, B = map(int, input().split())
mat = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    ele = input().split()
    for j in range(N):
        mat[i][j] = int(ele[j])

result = power(mat, B)
for row in result:
    print(*row)
