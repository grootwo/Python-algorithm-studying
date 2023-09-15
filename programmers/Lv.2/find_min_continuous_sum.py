from itertools import combinations
def solution(sequence, k):
    if k in sequence: # 만약 해당 수가 있다면
        return [sequence.index(k), sequence.index(k)]
    start_i = 0
    end_i = 1
    answer = [0, len(sequence)]
    # print(sequence[4:8])
    while start_i <= end_i:
        if sum(sequence[start_i:end_i]) == k and (end_i - start_i) < (answer[1] - answer[0]):
            answer = [start_i, end_i - 1]
            start_i += 1
        elif sum(sequence[start_i:end_i]) < k:
            if end_i < len(sequence):
                end_i += 1
            else:
                start_i += 1
        else:
            start_i += 1
    return answer
# def solution(sequence, k):
#     l = r = 0
#     answer = [0, len(sequence)]
#     sum = sequence[0]

#     while True:
#         if sum < k:
#             r += 1
#             if r == len(sequence): break
#             sum += sequence[r]
#         else:
#             if sum == k:
#                 if r-l < answer[1]-answer[0]:
#                     answer = [l, r]
#             sum -= sequence[l]
#             l += 1
#     return answer
