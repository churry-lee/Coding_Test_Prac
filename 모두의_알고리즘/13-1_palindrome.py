# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False

def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []
    # 1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        # 해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
        # 큐와 스택에 각각 그 문자를 추가
        if x.isalpha():   # 입력된 값이 알파벳으로 이루어져 있는지 확인하는 함수, 숫자, 특수문자, 공백 등일 경우 걸러
            qu.append(x.lower())
            st.append(x.lower())
    # 2단계: 큐와 스택에 들어 있는 문자를 꺼내면서 비교
    while qu:  # 큐에 문자가 남아 있는 동안 반복
        if qu.pop(0) != st.pop():  # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False

    return True

print(palindrome('wow'))
print(palindrome('abc'))
print(palindrome('가가가'))