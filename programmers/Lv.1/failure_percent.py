def solution(N, stages):
    stage_score = []
    for i in range(N + 2):
        stage_score.append([i, 0, 0])
    for stage in stages:
        stage_score[stage][1] += 1
    for i in range(1, N + 1):
        stage_score[stage][2] = stage_score[i][1] / sum(stage_score[i:N + 2])
    print(stage_score)
    answer = []
    return answer
