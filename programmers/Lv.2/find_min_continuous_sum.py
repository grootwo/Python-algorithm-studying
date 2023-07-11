from itertools import combinations
def solution(sequence, k):
    answer = []
    for i in range(len(sequence)):
        for j in combinations(sequence, i):
            if sum(j) == k:
                answer.append(j)
    print(answer)
    return answer
