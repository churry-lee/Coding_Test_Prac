list_a = [17, 92, 18, 33, 58, 7, 33, 42]

def find_min(list_a):
    min_v = list_a[0]
    for i in range(1, len(list_a)):
        if list_a[i] < min_v:
            min_v = list_a[i]
    return min_v

print(find_min(list_a))