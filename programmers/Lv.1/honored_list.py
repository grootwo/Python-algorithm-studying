def solution(k, score):
    from collections import deque
    honor_list = []
    least_score = []
    for i in range(k):
        new_score = score[i]
        honor_list.append(new_score)
        least_score.append(min(honor_list))
    honor_list.sort()
    honor_list.reverse()
    for i in range(k, len(score)):
        new_score = score[i]
        if new_score > min(honor_list):
            honor_list[-1] = new_score
        honor_list.sort()
        honor_list.reverse()
        least_score.append(min(honor_list))
    return least_score