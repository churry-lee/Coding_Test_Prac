A = int(input())
B = int(input())
C = int(input())

D = A * B * C

D = list(str(D))
count_dic = {}

for i in D:
    I = int(i)
    if I not in count_dic:
        count_dic[I] = 1
    else:
        count_dic[I] += 1

for i in range(10):
    if i in count_dic:
        print(count_dic[i])
    else:
        print(0)
