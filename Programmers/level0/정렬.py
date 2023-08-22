from typing import *
import mypy

def solution(numlist, n):
    numlist = [num - n for num in numlist]

    print(numlist)

    for i in range(0, len(numlist)-1):
        for j in range(i+1, len(numlist)):
            if abs(numlist[i]) > abs(numlist[j]):
                numlist[i], numlist[j] = numlist[j], numlist[i]
            if abs(numlist[i]) == abs(numlist[j]) and numlist[i] < numlist[j]:
                numlist[i], numlist[j] = numlist[j], numlist[i]

    print(numlist)

    numlist = [num + n for num in numlist]

    print(numlist)



print(solution([1, 2, 3, 4, 5, 6], 4))
