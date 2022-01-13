num = []
for _ in range(10):
    n = int(input())
    remain = n % 42
    if remain not in num:
        num.append(remain)
    else:
        continue

print(len(num))
