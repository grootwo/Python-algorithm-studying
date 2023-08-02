# Lv.1
# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
    return sorted(answer)
    # from itertools import combinations
    # return sorted(set(sum(i) for i in list(combinations(numbers, 2))))
