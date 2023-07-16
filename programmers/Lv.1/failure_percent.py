def solution(N, stages):
    stage_score = [0] * (N + 2)
    for stage in stages:
        stage_score[stage] += 1 
    stage_failure = []
    for i in range(1, N + 2):
        stage_failure.append(stage_score[i] / sum(stage_score[i:N + 2]))
    print(stage_failure)
    answer = []
    return answer
