# 리트코드 20
# 유효한 괄호
# 괄호로 된 입력값이 올바른지 판별하라.

def isValid(s: str) -> bool:
    stack = []
    table ={
        ')': '(',
        '}': '{',
        ']': '['
    }
    answer = 0
    for char in s:
        print(char)
        if char not in table:
            stack.append(char)
            print(stack)
        elif not stack or table[char] != stack.pop():
            return False
    if len(stack) == 0:
        answer += 1

    return answer

s = '(){}[]'
print(isValid(s))
