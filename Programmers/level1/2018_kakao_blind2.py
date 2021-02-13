# 다트게임
# 예제	dartResult	answer	
# 1	     1S2D*3T	37	
# 2	     1D2S#10S	9	
# 3	     1D2S0T	    3	
# 4	     1S*2T*3S	23	
# 5	     1D#2S*3S	5	
# 6	     1T2D3D#	-4	
# 7	     1D2S3T*	59	

dartResult = '1S*2T*3S'

def solution(dartResult):
    answer = 0
    tmp = ''
    score = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            tmp = tmp + dartResult[i]
            print('tmp', tmp)
        elif dartResult[i].isalpha():
            if dartResult[i] == 'S':
                score.append(int(tmp) ** 1)
            elif dartResult[i] == 'D':
                score.append(int(tmp) ** 2)
            elif dartResult[i] == 'T':
                score.append(int(tmp) ** 3)
            tmp = ''
        elif dartResult[i] == '*':
            score[-1] = score[-1] * 2
            if len(score) > 1:
                score[-2] = score[-2] * 2
        elif dartResult[i] == '#':
            score[-1] = score[-1] * -1

    print('score', score)
    answer = sum(score)

    return answer

print(solution(dartResult))