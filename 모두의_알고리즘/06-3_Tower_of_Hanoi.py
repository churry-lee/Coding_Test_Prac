# 재귀함수를 이용한 하노이의 탑 풀이
# n: 탑의 층수
# from_pos: 출발 기둥
# aux_pos: 보조 기둥
# end_pos: 도착 기둥
# 어려움 주의

def hanoi(n, from_pos, end_pos, aux_pos):  # 2, from = 1, aux = 2, end = 3
    if n == 1:
        print(from_pos, "->", end_pos)
        return

    hanoi(n-1, from_pos, aux_pos, end_pos)
    print(from_pos, "->", end_pos)
    hanoi(n-1, aux_pos, end_pos, from_pos)

print("n = 3")
hanoi(3, 1, 3, 2)