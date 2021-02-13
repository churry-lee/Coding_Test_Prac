# 스택/큐 문제(이 문제는 선입선출인 큐에 관한 문제)
# 스택: 후입선출(Last In First Out)
# 큐: 선입선출(First In First Out)
# 어떻게 풀이해 나갈지, 조건문과 반복문의 조건을 어떻게 설정할 지에 따라서 
# 코드의 길이와 퀄리티가 달라질 수 있다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length  # bridge_length 만큼 빈 리스트 생성

    while bridge:        # bridge에 트럭이 있는 동안(brdige 리스트가 비어 있지 않은 동안) 반복문 실행
        bridge.pop(0)    # 먼저 bridge의 첫번째 인덱스를 제거 및 truck_weight 리스트가 비었을 경우 요소 제거
        if truck_weights:  # truck_weight 리스트 안에 요소가 있으면 조건문 실행
            if sum(bridge) + truck_weights[0] <= weight:   # bridge 리스트의 합과 truck_weight 리스트의 첫번째 인덱스 합이 weight 보다 작으면
                bridge.append(truck_weights[0])            # bridge 리스트에 요소 추가
                truck_weights.pop(0)                       # truck_weight 리스트에 요소 제거
             
            else:    # 그렇지 않으면, 
                bridge.append(0)  # bridge 리스트에 0 요소 추가
        answer += 1  
        print('{}초'.format(answer), bridge)

    return answer

bridge_length = 2
weight = 50
truck_weights = [50, 50]

print(solution(bridge_length, weight, truck_weights))