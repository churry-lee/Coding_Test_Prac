'''
문제 설명

자연수 num이 주어질 때, num보다 크거나 같은 자연수 중에서 다음 조건을 만족하는 가장 작은 수를 구하려 합니다.
구하는 숫자의 자릿수는 짝수여야 합니다.
숫자가 2 x n 자릿수 일 때, 앞 n 자리의 각 자릿수 곱과 뒤 n 자리의 각 자릿수 곱이 같아야 합니다.
자연수 num이 매개변수로 주어질 때, num보다 크거나 같은 수 중에서 조건을 만족하는 가장 작은 수를 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ num ≤ 50,000,000
num은 자연수
입출력예
num	return
21	22
3462	3462
235386	235516
예시 설명
예시 #1
21 이상인 자연수 중에서 조건을 만족하는 가장 작은 수는 22입니다.
예시 #2
3462는 4자리 자연수이며, 앞, 뒤 2자리의 각 자릿수 곱은 다음과 같습니다.
앞 2자리 : 34 → 3 x 4 = 12
뒤 2자리 : 62 → 6 x 2 = 12
따라서 3462를 그대로 return 하면 됩니다.
예시 #3
조건을 만족하는 수는 다음과 같이 235516입니다.
235516 → 2 x 3 x 5 = 5 x 1 x 6 = 30

'''
# num = 30
num = 447
# num = 235386

def solution(num):
    answer = 0

    while True:
        print(num)
        num = str(num)

        if len(num) % 2 == 1:
            num = int(num)
            num += 1
            continue
        elif len(num) % 2 == 0:
            length = len(num) // 2
            tmp = [num[i:i + length] for i in range(0, len(num), length)]

            tmp_1 = list(tmp[0])
            left = 1
            for i in tmp_1:
                if i == 0:
                    left = 0
                left *= int(i)

            tmp_2 = list(tmp[1])
            right = 1
            for i in tmp_2:
                if i == 0:
                    right = 0
                right *= int(i)

        if left == right:
            answer = int(''.join(tmp_1) + ''.join(tmp_2))
            break
        else:
            num = int(num)
            num += 1

    return answer

print(solution(num))