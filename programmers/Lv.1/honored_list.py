# Lv.1
# 명예의 전당 (1)
def solution(k, score):
    from collections import deque
    honor_list = []
    least_score = []
    for i in range(len(score)):
        new_score = score[i]
        honor_list.append(new_score)
        if i >= k:
            honor_list.remove(min(honor_list))
        least_score.append(min(honor_list))
    return least_score