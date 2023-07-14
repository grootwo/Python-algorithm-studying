from collections import deque
def solution(plans):
    # 시작 시간 별로 정리: sort
    # 다음 시작 전까지 완료: - time
    # 남은 시간 저장: append
    # 다음 시작 전까지 완료: - time
    # 남은 과제 하기: popleft
    # 다음 시작 전까지 완료: - time
    plans.sort(key=lambda x:(x[1]))
    left_plans = deque(plans)
    unsolved_plans = deque([])
    now = left_plans[0]
    while len(left_plans) != 0 and len(unsolved_plans) != 0:
        print(hi)
        left_plans.clear()
    return 0
