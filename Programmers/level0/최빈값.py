def solution(array):
    num_dic = {}

    for num in array:
        if num not in num_dic:
            num_dic.setdefault(num, 1)
        else:
            num_dic[num] += 1

    max_list = []
    for key, value in num_dic.items():
        if value == max(num_dic.values()):
            max_list.append(key)

    if len(max_list) >= 2:
        return -1
    else:
        return max_list[0]

# print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 1, 2, 2, 2]))
