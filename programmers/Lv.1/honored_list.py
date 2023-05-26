# Lv.1
# 명예의 전당 (1)
def solution(k, score):
    from collections import deque
    honor_list = []
    least_score = []
    for i in range(len(score)):
        new_score = score[i]
        if i < k:
            honor_list.append(new_score)
        else:
            if new_score > min(honor_list):
                honor_list.remove(min(honor_list))
                honor_list.append(new_score)
        least_score.append(min(honor_list))
    return least_score