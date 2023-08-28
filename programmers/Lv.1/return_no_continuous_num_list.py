# Lv.1
# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for num in arr[1:]:
        if answer[-1] != num: # 연속으로 같은 숫자가 아닌 경우
            answer.append(num)
        else: # 연속으로 같은 숫자가 나타날 경우
            continue
    return answer
