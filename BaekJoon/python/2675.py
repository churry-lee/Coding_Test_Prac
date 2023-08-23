T = int(input())    # 테스트 케이스 개수

cases = []
for _ in range(T):
    case = input().split()
    case[0] = int(case[0])
    cases.append(case)

results = []
for case in cases:
    result = ''
    iter = case[0]
    str = case[1]
    for s in str:
        result += (iter * s)
        
    results.append(result)
    
for res in results:
    print(res)
