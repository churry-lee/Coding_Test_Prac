# max() 미사용
list_a = [17, 92, 18, 33, 58, 107, 33, 42]

def find_max(list_a):
    max_v = list_a[0]
    for i in range(1, len(list_a)):
        if list_a[i] > max_v:
            max_v = list_a[i]
    return max_v

print(find_max(list_a))