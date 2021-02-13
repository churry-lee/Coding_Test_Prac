# 크레인 인형뽑기

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0    
    basket = [0]

    for move in moves:
        for i in range(len(board)):
            if board[i][(move-1)] == 0:
                continue
            elif board[i][(move-1)] == basket[-1]:
                basket.pop()
                answer += 2
                break
            else:
                basket.append(board[i][(move-1)])
                break
        board[i][(move-1)] = 0
    
    return answer, basket[1:]

print(solution(board, moves))