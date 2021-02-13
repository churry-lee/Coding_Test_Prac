"""
탐욕법
이름을 완성하기 위한 최단 거리 탐색
대문자 알파벳 아스키코드
A(065) B(066) C(067) D(068) E(069) F(070) G(071) H(072) I(073) J(074) K(075) L(076) M(077) N(078)
O(079) P(080) Q(081) R(082) S(083) T(084) U(085) V(086) W(087) X(088) Y(089) Z(090) A(065)
"""

# name = "JEROEN"   # return 56
# name = 'JAN'      # return 23
# name = 'JAZ'      # return 11
# name = 'BBBAAAB'  # return 9
# name = 'JABZ'     # return 13
# name = 'JBAZ'     # return 14
# name = 'JE'
name = 'ABABAAAAABA' # return 11


def solution(name):
    answer = 0
    name = list(name)
    # 알파벳 이동 수
    for i in name:
        answer += min(ord(i) - 65, 90 - ord(i)+1)
    # 이름에 'A'가 들어 있지 않을 때 이동 수
    if 'A' not in name:
        answer += len(name) - 1
    # 이름에 'A'가 들어 있을 때 이동 수
    elif 'A' in name:
        if name.index('A') >= len(name) / 2:
            answer += len(name) - 1
        else:
            name = list(name)
            left, right = 0, 0
            idx = 0
            while True:
                if name[idx] != 'A':
                    right += 1
                    idx += 1
                elif name[idx] == 'A':
                    idx = -1
                    left += right - 1
                    while True:
                        idx -= 1
                        if name[idx] == 'A':
                            break
                        left += 1

                    break
            answer += (right+left)

    return answer

print(solution(name))