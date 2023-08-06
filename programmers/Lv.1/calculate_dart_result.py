# Lv.1
# [1차] 다트 게임
from collections import deque
def solution(dartResult):
    answer = ['', '', '']
    sqr_dic = {'S': '**1', 'D': '**2', 'T': '**3'}
    check = -1
    dartResult = deque(dartResult)
    while dartResult:
        # 정수라면
        if dartResult[0] + dartResult[1] == '10':
            temp = int(dartResult[0] + dartResult[1])
            dartResult.popleft()
            dartResult.popleft()
            check += 1
            answer[check] += temp
        elif '0' <= dartResult[0] <= '9':
            temp = dartResult[0]
            dartResult.popleft()
            check += 1
            answer[check] += temp
        else:
            dartResult.popleft()
        if check >= len(dartResult):
            break
        # # 보너스라면
        # elif i == 'S' or i == 'D' or i == 'T':
        #     print('2')
        #     answer[check] += sqr_dic[i]
        # # 옵션이라면
        # else:
        #     print('3')
        #     if i == '#':
        #         answer[check] += '*-1'
        #     elif i == '*' and check > 0:
        #         answer[check] += '*2'
        #         answer[check - 1] += '*2'
        #     else:
        #         answer[check] += '*2'
    print(answer)
    return answer
