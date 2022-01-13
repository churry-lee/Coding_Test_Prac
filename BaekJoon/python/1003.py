N = int(input())

zero = []
one = []

def fibonacci(n):
    
    if n == 0:
        zero.append(0)
        return 0
    elif n == 1:
        one.append(1)
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(N)

print("{} {}".format(len(zero), len(one)))

