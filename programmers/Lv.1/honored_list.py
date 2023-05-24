def solution(k, score):
    from collections import deque
    honor_list = deque([])
    least_score = []
    for new_score in range(k):
        honor_list.append(new_score)
        least_score.append(min(honor_list))
    honor_list.sort()
    for new_score in range(k, len(score)):
        if new_score > min(honor_list):
            honor_list.pop()
            honor_list.append(new_score)
            honor_list.sort()
        least_score.append(min(honor_list))
    return least_score

