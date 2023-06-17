def solution(lottos, win_nums):
    count_correct = 0
    count_none = 0
    for num in lottos:
        if num == 0:
            count_none += 1
        elif num in win_nums:
            count_correct += 1
    answer = [count_correct + count_none, count_correct]
    for i in range(2):
        answer[i] = 7 - answer[i]
        print(answer[i])
    return answer
