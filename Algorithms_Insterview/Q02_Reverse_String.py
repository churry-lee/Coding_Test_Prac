# 리트코드 344
# 리턴 없이 원래의 리스트 내부를 직접 조작 하는 방법
s = ['h', 'e', 'l', 'l', 'o']

def reverseString(s):
    s.reverse()
    return s
print(reverseString(s))


# 새로운 리스트에 반전된 값을 넣어 리턴하는 방법
def reverseString(s):
    strs = []
    for i in range(len(s)):
        strs.insert(0, s[i])
    return strs
print(reverseString(s))
