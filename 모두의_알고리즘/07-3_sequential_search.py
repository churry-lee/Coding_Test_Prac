# 학생 번호에 해당하는 이름을 순차적으로 찾아 주는 함수
# 번호가 없으면 ?를 리턴

stu_no = [39, 14, 67, 105]
stu_name = ['Justin', 'John', 'Mike', 'Summer']

def stu_search(x):
    stu = {}
    for i in range(len(stu_no)):
        stu[stu_no[i]] = stu_name[i]

    if x in stu:
        return stu[x]
    else:
        return '?'

print(stu_search(14))