from itertools import combinations
def solution(sequence, k):
    if k in sequence: # 만약 해당 수가 있다면
        return [sequence.index(k), sequence.index(k)]
    # start_i = 0
    # end_i = 1
    # answers = []
    # while start_i <= end_i:
    #     if sequence[start_i:end_i] == k:
    #         start_i += 1
    return 0
