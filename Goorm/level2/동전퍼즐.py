# 코드 분석 필요
import sys
input_ = sys.stdin.readline


def solve(h1, w1, c1, h2, w2, c2):
	# 입력을 받아 2차원 배열에 저장
	total = 0
	# 배열에서 동전이 있는 위치를 찾아 c2에 표시하고 동전의 개수를 센다
	for i in range(h2):
		row = input()
		for j in range(w2):
			c2[i + 10][j + 10] = row[j]
			total += (row[j] == 'O')
	# 모든 가능한 위치에서 겹치는 동전의 개수를 센다
	max_overlap = 0
	for i in range(31 - h1):
		for j in range(31 - w1):
			cnt = sum(c1[y][x] == c2[y + i][x + j] == 'O' for y in range(h1) for x in range(w1))
			max_overlap = max(max_overlap, cnt)
	# 동전을 움직여야 하는 최소 횟수는 total에서 겹치는 동전의 개수를 빼면 된다
	print(total - max_overlap)


if __name__ == "__main__":
	H1, W1 = map(int, input_().strip().split())
	C1 = [list(input_().strip()) for _ in range(H1)]
	# print(f"C1: {C1}")
	H2, W2 = map(int, input_().strip().split())
	C2 = [["."] * 30 for _ in range(30)]
	# print(f"C2: {C2}")
	
	solve(H1, W1, C1, H2, W2, C2)
