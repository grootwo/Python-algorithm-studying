def solution(plans):
    # 할 일을 시간이 이른 순으로 정리
    plans.sort(key=lambda x: (x[1]))
    print(plans)
    from collections import deque
    que_plans = deque(plans)
    que_left = deque([])
    answer = []
    while que_plans:
        now = que_plans.popleft()
        now_finish = get_end_time(now[1], now[2])
        if que_plans: # 만약 다음 할 일이 있다면
            next_start = que_plans[0][1]
            if now_finish == next_start: # 지금 일이 끝나고 다음 일이 바로 실행된다면
                print('finish: ', now[0])
                answer.append(now[0])
                continue
            elif now_finish < next_start: # 지금 일이 끝나고 다음 일까지 시간이 남으면
                left_time = get_left_time(now_finish, next_start)
                print('left time: ', left_time, ' until: ', next_start)
                if que_left: # 만약 하다 만 할 일이 있다면
                    while left_time > 0: # 남은 시간에
                        if que_left[0][2] > left_time:
                            que_left[0][2] -= left_time
                            left_time = 0
                        elif que_left[0][2] == left_time:
                            answer.append(que_left.popleft()[0])
                            left_time = 0
                        elif que_left[0][2] < left_time:
                            left_time -= que_left[0][2]
                            answer.append(que_left.popleft()[0])
        else: # 만약 다음 할 일이 없다면
            answer.append(now[0])
    while que_left: # 하다 만 일이 있다면
        answer.append(que_left.popleft()[0])
    return answer

def get_end_time(start, runtime):
    hr = int(start[0:2])
    mi = int(start[3:5]) + int(runtime)
    if mi >= 60:
        hr += mi // 60
        mi = mi % 60
    return str(hr) + ":" + str(mi)

def get_left_time(start, end):
    hr = int(end[0:2]) - int(start[0:2])
    mi = int(end[3:5]) - int(start[3:5])
    result = mi + hr * 60
    if result >= 0:
        return result
    else:
        return -1

plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
print(solution(plans))

# [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]	["korean", "english", "math"]
# [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	["science", "history", "computer", "music"]
# [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	["bbb", "ccc", "aaa"]