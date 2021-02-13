# 리트코드 316
# 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# s = 'bcabc'      # return 'abc'
s = 'cbacbcdc'     # return 'acdb'

def removeDuplicateLetters(s):
    counter = {}
    stack = []

    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    print('counter: {}'.format(counter))

    for char in s:
        # counter - 1 을 하면서 문자 stack 여부 확인
        counter[char] -= 1
        # 알파벳에 이미 stack이 되어있다면 넘어감
        if char in stack:
            continue
        # stack에 문자가 있고, 이전에 입력된 문자가 새로 입력될 문자보다 고, 이전에 입력된 문자의 counter가 0 보다 크면,
        while stack and (char < stack[-1]) and (counter[stack[-1]] > 0):
            stack.pop()
        stack.append(char)

    return ''.join(stack)

print(removeDuplicateLetters(s))