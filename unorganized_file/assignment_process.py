def solution(plans):
    plans.sort(key=lambda x: (x[1]))
    # print(plans)
    # start
    # if stop, remember rest of time and order
    # 
    order = []
    waiting_list = deque([])
    from collections import deque
    que = deque(plans)
    while que:
        if 
    answer = []
    return answer

def get_end_time(start, runtime):
    hr = int(start[0:2])
    mi = int(start[3:5]) + int(runtime)
    if mi >= 60:
        hr += mi // 60
        mi = mi % 60
    return str(hr) + ":" + str(mi)

def get_rest_time(now, until):
    until_hr = until[3:5]
    until_mi = until[0:2]
    now_hr = now[3:5]
    now_mi = now[0:2]
    if until_mi < now_mi:
        return str(until_hr - now_hr - 1) + ":" + str(60 + until_mi - now_mi)
    else:
        return str(until_hr - now_hr) + ":" + str(until_mi - now_mi)
