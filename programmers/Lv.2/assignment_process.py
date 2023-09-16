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

# 다음 시간 전까지 남은 시간 계산
# 만약 시간이 남는다면 이전에 완료하지 못한 시간 측정
# 만약 시간이 모자라다면 완료하지 못한 시간에 추가
