import sys
input_ = sys.stdin.readline


if __name__ == '__main__':
    N = input_().strip()
    
    ans = [0, 0, 0, 0]
    for n in N:
        if n == '1':
            ans[0] += 1
        elif n == 'I':
            ans[1] += 1
        elif n == 'l':
            ans[2] += 1
        elif n == '|':
            ans[3] += 1

    for a in ans:
        print(a)
