# 키패드

#numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
#hand = "right"	# "LRLLLRLLRRL"
#numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
#hand = "left"	# "LRLLRRLLLRR"
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#hand = "right"	# "LLRLLRLLRL"



numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def solution(numbers, hand):
    answer = ''

    key_pad = {
        1:(1, 1), 2:(1, 2), 3:(1, 3),
        4:(2, 1), 5:(2, 2), 6:(2, 3),
        7:(3, 1), 8:(3, 2), 9:(3, 3),
        "*":(4, 1), 0:(4, 2), "#":(4, 3),
        'left':(1, 4, 7, "*"), 'right':(3, 6, 9, "#"), 'mid':(2, 5, 8, 0)
    }

    left_pos = "*"
    right_pos = "#"

    for number in numbers:
        if number in key_pad['left']:
            answer = answer + "L"
            left_pos = number
        elif number in key_pad['right']:
            answer = answer + "R"
            right_pos = number
        elif number in key_pad['mid']:
            if (abs(key_pad[left_pos][0] - key_pad[number][0]) + abs(key_pad[left_pos][1] - key_pad[number][1])) < \
                (abs(key_pad[right_pos][0] - key_pad[number][0]) + abs(key_pad[right_pos][1] - key_pad[number][1])):
                answer = answer + "L"
                left_pos = number
            elif (abs(key_pad[left_pos][0] - key_pad[number][0]) + abs(key_pad[left_pos][1] - key_pad[number][1])) > \
                (abs(key_pad[right_pos][0] - key_pad[number][0]) + abs(key_pad[right_pos][1] - key_pad[number][1])):
                answer = answer + "R"
                right_pos = number
            elif (abs(key_pad[left_pos][0] - key_pad[number][0]) + abs(key_pad[left_pos][1] - key_pad[number][1])) == \
                (abs(key_pad[right_pos][0] - key_pad[number][0]) + abs(key_pad[right_pos][1] - key_pad[number][1])):
                if hand == "left":
                    answer = answer + "L"
                    left_pos = number
                elif hand == "right":
                    answer = answer + "R"
                    right_pos = number

        print("입력값 {} 일 때, 왼손 위치 {} / 오른손 위치 {}".format(number, left_pos, right_pos))
    return answer

print(solution(numbers, hand))