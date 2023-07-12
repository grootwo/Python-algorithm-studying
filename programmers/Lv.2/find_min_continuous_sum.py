from itertools import combinations
def solution(sequence, k):
    answer = []
    check = False
    for i in range(1, len(sequence)):
        if check is True:
            break
        for j in range(len(sequence) - i + 1):
            if sum(sequence[j:j + i]) == k:
                check = True
                answer = [j, j + i - 1]
                break
    return answer
