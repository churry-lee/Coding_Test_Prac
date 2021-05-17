import datetime

purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]

def solution(purchase):
    answer = []

    bronze, silver, gold, platinum, diamond = 0, 0, 0, 0, 0

    dates = ['2019-01-01']
    costs = [0]

    for i in purchase:
        temp = i.split(' ')
        dates.append(temp[0].replace('/', '-'))
        costs.append(int(temp[1]))

    dates.append('2019-12-31')
    costs.append(0)
    
    for i in range(len(dates)-1):
        day1 = datetime.datetime.strptime(dates[i], "%Y-%m-%d") 
        day2 = datetime.datetime.strptime(dates[i+1], "%Y-%m-%d") 
        day_diff = (day2 - day1).days
        print(day_diff)

    # if 0 <= costs[0] < 10000:
    #     rank = "Bronze"
    # elif 10000 <= costs[0] < 20000:
    #     rank = "Silver"
    # elif 20000 <= costs[0] < 50000:
    #     rank = "Gold"
    # elif 50000 <= costs[0] < 100000:
    #     rank = "Platinum"
    # else:
    #     rank = "Diamond"
    # strpDateTime = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d") 
    # print(strpDateTime) # 2019-12-15 21:19:17+00:00

    

    return answer

print(solution(purchase))