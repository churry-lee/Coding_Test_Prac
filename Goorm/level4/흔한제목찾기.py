import sys
input_ = sys.stdin.readline


# 알파벳 빈도수 계산
def get_popular_alphabets(sum__: list, ranges_: list[tuple[int, int]]) -> list[str]:
    answers = []
    for l, r in ranges_:
        counts = [r_ - l_ for r_, l_ in zip(sum__[r], sum__[l - 1])]
        popular_alphabet = chr(counts.index(max(counts)) + ord('A'))
        # 가장 빈도수 높은 알파벳 저장
        answers.append(popular_alphabet)
    return answers


if __name__ == '__main__':
    N, Q = map(int, input_().strip().split())
    books = input()
    
    ranges = []
    for _ in range(Q):
        L, R = map(int, input_().strip().split())
        ranges.append((L, R))
    
    # 알파벳 빈도수 저장
    sum_ = [[0] * 26]
    for i in range(N):
        current = sum_[-1][:]
        for c in books[i]:
            current[ord(c) - ord('A')] += 1
        sum_.append(current)
    
    alphabet = get_popular_alphabets(sum_, ranges)
    for c in alphabet:
        print(c)
