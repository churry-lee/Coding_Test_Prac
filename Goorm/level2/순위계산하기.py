import sys
input_ = sys.stdin.readline


def calculate_rank(votes_: list[tuple], scores_: list[int]) -> list[tuple[int, int, int]]:
    for vote in votes_:
        P, Q = vote
        if 1 <= P <= N and 1 <= Q <= N and P != Q:
            scores_[P] += 5
            scores_[Q] += 3
    
    teams_scores = []
    for i in range(1, N + 1):
        teams_scores.append((scores_[i], i))
    
    teams_scores.sort(key=lambda x: (-x[0], x[1]))      # score에 대해 내림차순 정렬, 팀번호에 대해 오름차순 정렬
    
    result = []
    last_rank, last_score = 0, -1   # 중복 랭크와 점수 검사
    for i, team_score in enumerate(teams_scores):
        score, team = team_score
        if last_score != score:
            last_rank = i + 1
            last_score = score
        result.append((last_rank, team, score))
    
    return result


if __name__ == '__main__':
    N, M = map(int, input_().strip().split())
    scores = [0] * (N + 1)
    
    votes = []
    for _ in range(M):
        P, Q = map(int, input_().strip().split())
        votes.append((P, Q))
        
    ranks = calculate_rank(votes, scores)
    
    for rank in ranks:
        print(*rank)
