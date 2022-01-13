def maker(n):
    num = []
    result = 0

    for i in str(n):
        num.append(int(i))

    num.append(n)

    for j in num:
        result += j

    return result

def SelfNum(iter):
    list_num = []

    for i in range(1, iter):
        list_num.append(maker(i))
        if i not in list_num:
            print(i)

SelfNum(10000)
