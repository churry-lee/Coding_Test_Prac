# 딕셔너리를 이용하여 풀이
names = ['Tom', 'Jerry', 'Mike', 'Tom', 'bob', 'bob']

def same_name(names):
    names_dict = {}
    results = []
    for name in names:
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1

    for name in names_dict:
        if names_dict[name] >= 2:
            results.append(name)

    return names_dict, results

print(same_name(names))