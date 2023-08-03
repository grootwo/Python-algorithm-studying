# Lv.1
# 실패율
def solution(N, stages):
    failure_rate = {}
    stages_len = len(stages)
    for i in range(1, N+1):
        if stages_len != 0:
            stage_count = stages.count(i)
            failure_rate[i] = stage_count/stages_len # 실패율 계산
            stages_len -= stage_count # 다음 단계에 도달한 사람들 수
        else:
            failure_rate[i] = 0 # 사람이 없는 단계들은 일괄 처리
    answer = sorted(failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True) # 실패율로 정렬
    return answer
