num = int(input())
n = str(num)
count = 0

while True:
    if len(n) == 1:
        n = "0" + n

    n = list(n)
    
    N = int(n[0]) + int(n[1])
    N = str(N)
    if len(N) == 1:
        N = "0" + N
    n[0], n[1] = n[1], N[1]

    count += 1
    New_n = int("".join(n))
    
    if New_n == num:
        print(count)
        break
