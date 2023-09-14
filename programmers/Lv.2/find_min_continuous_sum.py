from itertools import combinations
def solution(sequence, k):
    if k in sequence: # 만약 해당 수가 있다면
        return [sequence.index(k), sequence.index(k)]
    start_i = 0
    end_i = 1
    answers = []
    # print(sequence[4:8])
    while start_i <= end_i:
        if sum(sequence[start_i:end_i]) == k:
            answers.append([start_i, end_i - 1])
            start_i += 1
        elif sum(sequence[start_i:end_i]) < k:
            if end_i < len(sequence):
                end_i += 1
            else:
                start_i += 1
        else:
            start_i += 1
    for i in range(len(answers)): # 인덱스 간의 차이 구하기
        answers[i].append(answers[i][1] - answers[i][0])
    answers.sort(key=lambda x: (x[2])) # 인덱스 간의 차이를 순서대로 정렬하기
    return answers[0][0:2]
