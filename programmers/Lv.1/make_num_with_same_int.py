# Lv.1
# 숫자 짝궁
from collections import Counter
def solution(X, Y):
    same_num = []
    X = Counter(X)
    Y = Counter(Y)
    # print(X)
    # print(Y)
    for num in X:
        if num in Y: # 만약 겹치는 숫자라면
            # 해당 숫자와 둘 중 적은 숫자를 기록
            if X[num] > Y[num]:
                same_num.append([int(num), Y[num]])
            else:
                same_num.append([int(num), X[num]])
    same_num.sort(key=lambda x: (-x[0]))
    answer = ''
    # 문자열 만들기
    if same_num and same_num[0][0] != 0:
        for nums in same_num:
            answer += str(nums[0]) * nums[1]
    elif same_num: # 0만 있다면
        answer = '0'
    else: # 겹치는 숫자가 없다면
        answer = '-1'
    # print(answer)
    return answer
