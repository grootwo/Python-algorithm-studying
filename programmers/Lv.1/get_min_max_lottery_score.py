# Lv.1
# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    # 일치하는 숫자와 모르는 숫자 세기
    count_correct = 0
    count_none = 0
    for num in lottos:
        if num == 0:
            count_none += 1
        elif num in win_nums:
            count_correct += 1
    # 등수 확인하기
    answer = [count_correct + count_none, count_correct]
    for i in range(2):
        answer[i] = 7 - max(answer[i], 1) # 1개나 0개 맞았을 때 결과가 같도록
    return answer
