# Lv.1
# [1차] 다트 게임
def solution(dartResult):
    answer = ['', '', '']
    check = -1
    for i in dartResult:
        print('i:', i)
        print('check:', check)
        sqr_dic = {'S': '**1', 'D': '**2', 'T': '**3'}
        # 정수라면
        if '0' <= i <= '9':
            print('1')
            check += 1
            # answer[check] += i
        # 보너스라면
        elif i == 'S' or i == 'D' or i == 'T':
            print('2')
            # answer[check] += sqr_dic[i]
        # 옵션이라면
        else:
            print('3')
            # if i == '#':
            #     answer[check] += '*-1'
            # elif i == '*' and check > 0:
            #     answer[check] += '*2'
            #     answer[check - 1] += '*2'
            # else:
            #     answer[check] += '*2'
    print(answer)
    return answer
