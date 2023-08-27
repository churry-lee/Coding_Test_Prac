import sys
input_ = sys.stdin.readline


def dfs(g, node):
	seen[node] = True
	# print(seen)
	for next_v in g[node]:
		if seen[next_v]:
			continue
		dfs(g, next_v)


if __name__ == '__main__':
	N = int(input_().strip())
	M = int(input_().strip())
	
	graph = {i: [] for i in range(1, N+1)}
	for _ in range(M):
		a, b = map(int, input_().strip().split())
		# 무향으로 가정
		graph[a].append(b)
		graph[b].append(a)
	
	seen = [False] * (N+1)
	print(f"graph: \n{graph}")
	
	dfs(graph, 1)
		
	# print(seen)
	print(seen.count(True))
