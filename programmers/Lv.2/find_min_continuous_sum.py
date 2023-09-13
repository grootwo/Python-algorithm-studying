from itertools import combinations
def solution(sequence, k):
    if k in sequence: # 만약 해당 수가 있다면
        return [sequence.index(k), sequence.index(k)]
    start_i = 0
    end_i = 1
    answers = []
    while start_i <= end_i:
        if sum(sequence[start_i:end_i]) == k:
            start_i += 1
            answers.append([start_i, end_i])
        elif sum(sequence[start_i:end_i]) < k:
            end_i += 1
        else:
            start_i += 1
    print(answers)
    return 0
