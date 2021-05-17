math_scores = [70, 65, 90, 80, 50]
english_scores = [40, 20, 30, 60, 50]

# math_scores = [90, 91, 95, 99, 100]
# english_scores = [20, 40, 60, 80, 100]

# math_scores = [80, 50, 30, 20, 10]
# english_scores = [24, 39, 47, 63, 75]


def solution(math_scores, english_scores):
    answer = 0
    
    for i in range(len(math_scores)):
        for j in range(i+1, len(math_scores)):
            if (math_scores[i] > math_scores[j]):
                if (english_scores[i] > english_scores[j]):
                    answer += 1
                else:
                    continue
            elif (math_scores[i] < math_scores[j]):
                if (english_scores[i] < english_scores[j]):
                    answer += 1
                else:
                    continue

    return answer

print(solution(math_scores, english_scores))