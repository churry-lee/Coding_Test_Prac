from typing import *
import mypy

def solution(n: int, m: int) -> int:
    answer = 0
    tmp_str: str = ""
    tmp_list: list = []

    reverse_num: int = 0
    for num in range(n, m+1):
        tmp_list = list(str(num))
        reverse_list: list = []

        for i in tmp_list[::-1]:
            reverse_list.append(i)
            reverse_num = int(''.join(reverse_list))
            if num == reverse_num:
                answer += 1

    return answer


# print(solution("aaabbaccccabba"))
# print(solution("banana"))
print(solution(1, 100))
