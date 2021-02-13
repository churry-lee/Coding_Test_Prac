# 리트코드 125
s = input("Input>> ")

def isPalindrome(s):
    strs = []
    for char in s:
        if char.isalnum():            # 영어, 숫자, 한글 등의 언어 문자만 처리함, 특수문자를 입력하면 제외됨
            strs.append(char.lower()) # 문제에서 대,소문자 구별을 안한다고 했으므로, 알파벳을 소문자로 바꿔 strs 리스트에 추가함

    for i in range(len(strs) // 2):
        if strs[i] != strs[-i-1]:
            return False
    return True

print(isPalindrome(s))