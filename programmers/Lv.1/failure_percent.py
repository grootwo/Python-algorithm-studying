def solution(N, stages):
    stage_people = {}
    for stage in stages:
        if stage in stage_people:
            stage_people[stage] += 1
        else:
            stage_people[stage] = 1
    answer = []
    for stage in list(stage_people.keys()):
        # 여기서 정렬하려면 list의 sort가 나아보인다.
    return answer
