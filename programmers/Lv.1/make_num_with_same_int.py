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
        if num in Y:
            if X[num] > Y[num]:
                same_num.append([int(num), Y[num]])
            else:
                same_num.append([int(num), X[num]])
    same_num.sort(key=lambda x: (-x[0]))
    answer = ''
    if same_num and same_num[0][0] != 0:
        for nums in same_num:
            answer += str(nums[0]) * nums[1]
    elif same_num:
        answer = '0'
    else:
        answer = '-1'
    # print(answer)
    return answer
