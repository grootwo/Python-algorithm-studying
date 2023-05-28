def solution(k, m, score):
    score.sort()
    score.reverse()
    total_price = 0
    for i in range(0, len(score), m):
        if i + m > len(score):
            break
        price = min(score[i:i + m])
        total_price += price * m
    answer = total_price
    return answer
