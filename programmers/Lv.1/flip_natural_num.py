def solution(n):
    answer = list(str(n))
    answer.reverse()
    answer = [int(cha) for cha in answer]
    return answer
