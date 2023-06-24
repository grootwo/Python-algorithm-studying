def solution(targets):
    targets.sort(key=lambda x: -x[1])
    max_num = targets[0][1]
    print(max_num)
    answer = 0
    return answer
