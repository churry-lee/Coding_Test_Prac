# 리스트안 순차적 탐색(선형 탐색)
# 리스트 안에서 찾고자 하는 값을 찾은 후 그 위치(Index)를 리턴
# 찾고자 하는 값이 없으면 -1을 리턴
list_a = [17, 92, 18, 33, 58, 5, 33, 42]

def search(list_a, x):

    for i in range(len(list_a)):
        if x == list_a[i]:
            return i

    return -1


print(search(list_a, 33))