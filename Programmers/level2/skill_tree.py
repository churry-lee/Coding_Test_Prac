def solution(skill, skill_trees):
    answer = 0
    tmp_list = [] 

    for skill_tree in skill_trees:
        tmp = ''
        for i in range(len(skill_tree)):   # 스킬 트리의 각 스킬을 순서대로 불러와
            if skill_tree[i] in skill:     # 주어진 skill에 있는 스킬이면 tmp에 저장
                tmp += skill_tree[i]       
        tmp_list.append(tmp)               # 각 스킬에 주어진 스킬에 있는 스킬만 따온 임시 스킬 문자열을 임시 리스트에 저장
    print(tmp_list)

    answer_list = []
    for tmp_str in tmp_list:               # 리스트의 각 원소들의 길이가  1 이상인 경우 새로운 리스트에 저장
        if len(tmp_str) > 0:               
            answer_list.append(tmp_str)
        elif len(tmp_str) == 0:            # 원소의 길이가 0인 경우에도 조건을 충족하는 것이므로 answer + 1
            answer += 1
    print(answer_list)

    for answer_str in answer_list:
        if (answer_str in skill) and (answer_str[0] == skill[0]):
            answer += 1

    return answer

skill = "ABC"
#skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "CDA", "DACB", "AEC", "C", "B", "D"]  # return 2
#skill = "ZE"
skill_trees = ["OPQ", "AC"]

print(solution(skill, skill_trees))