list_num = []

while len(list_num) < 9:
    N = int(input())
    list_num.append(N)

max_num = max(list_num)
print(max_num)
print(list_num.index(max_num) + 1)
