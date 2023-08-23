import datetime

A, B, C = map(int, input().split())
D = int(input())

# datetime 객체 생성
current_time = datetime.datetime.combine(datetime.date.today(), datetime.time(A, B, C))
# 요리 시간 추가
end_time = current_time + datetime.timedelta(seconds=D)

# 결과 출력
print(end_time.time().hour, end_time.time().minute, end_time.time().second)
