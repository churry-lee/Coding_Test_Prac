from typing import *
import mypy

def solution(noti_time: str, do_not_disturb: list):
    answer = ''

    noti_hour = int(noti_time.split(":")[0])
    noti_min = int(noti_time.split(":")[1])
    print(f"noti: {noti_hour}:{noti_min}")
    for disturb in do_not_disturb:
        disturb_start_hour = int(disturb.split("~")[0].split(":")[0])
        disturb_start_min = int(disturb.split("~")[0].split(":")[1])

        disturb_end_hour = int(disturb.split("~")[1].split(":")[0])
        disturb_end_min = int(disturb.split("~")[1].split(":")[1])

        if disturb_start_hour > disturb_end_hour:
            disturb_end_hour += 24

        print(disturb_start_hour, disturb_start_min, disturb_end_hour, disturb_end_min)

        if noti_hour == disturb_start_hour:
            if noti_min < disturb_start_min:
                pass
        elif noti_hour == disturb_end_hour:
            if noti_min < disturb_end_min:
                pass


        if disturb_start_hour < noti_hour <= disturb_end_hour:
            continue
        else: ## 방해 금지 시간에 포함되지 않을 경우
            # noti 시간과 방해 금지 시간을 비교해서 더 빠른 시간을 리턴
            if noti_hour < disturb_start_hour:
                return noti_time
            else:
                return disturb.split("~")[1]

    return "impossible"


# print(solution("23:00", ["22:30~23:40", "23:05~00:45"])) # "00:45"
print(solution("09:55", ["09:55~13:25", "13:25~14:01"])) # "00:45"
