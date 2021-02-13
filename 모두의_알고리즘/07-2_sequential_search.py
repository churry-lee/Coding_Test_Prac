# 리스트안 순차적 탐색(선형 탐색)
# 리스트 안에서 찾고자 하는 값을 찾은 후 그 위치(Index)를 리턴
# 중복되는 값이 있으면 모든 위치를 리턴
# 찾고자 하는 값이 없으면 []을 리턴
list_a = [17, 92, 18, 33, 58, 5, 33, 42]

def search(list_a, x):
    list_b = []

    for i in range(len(list_a)):
        if x == list_a[i]:
            list_b.append(i)

    return list_b


print(search(list_a, 33))