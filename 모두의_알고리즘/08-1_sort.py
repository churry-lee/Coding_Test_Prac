# 쉽게 설명한 선택 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트
# 원래 리스트에서 최소값을 새로운 리스트에 추가 후 원래 리스트에서의 최소값을 제거
# 이 과정을 반복하며 새로운 리스트에 순차적으로 정렬

d = [2, 4, 5, 1, 3]

def sel_sort(d):
    new_d = []

    while d:
        new_d.append(min(d))
        d.remove(min(d))

    return new_d

print(sel_sort(d))