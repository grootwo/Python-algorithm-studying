def solution(N, stages):
    # stage별 도달 참가자 수 구하기
    stage_score = [0] * (N + 2)
    for stage in stages:
        stage_score[stage] += 1
    # 각 stage별 실패율과 stage 저장하기
    stage_info = []
    for i in range(1, N + 1):
        stage_info.append([i, stage_score[i] / sum(stage_score[i:N + 2])])
    # 실패율을 기준으로 내림차순으로 정리
    stage_info.sort(key=lambda x:-x[1])
    return [i[0] for i in stage_info]
