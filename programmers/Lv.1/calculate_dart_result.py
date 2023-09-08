# Lv.1
# [1차] 다트 게임
def solution(dartResult):
    answer = [0, 0, 0]
    flag = -1
    i = 0
    while i < len(dartResult):
        if '0' <= dartResult[i] <= '9': # 점수일 경우
            if dartResult[i:i + 2] == '10':
                temp = 10
                i += 2
            else:
                temp = int(dartResult[i])
                i += 1
            flag += 1
            answer[flag] += temp
        elif dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T': # 보너스일 경우
            bonus = dartResult[i]
            if bonus == 'D':
                answer[flag] **= 2
            elif bonus == 'T':
                answer[flag] **= 3
            i += 1
        else: # 옵션일 경우
            option = dartResult[i]
            if option == '*':
                temp = flag - 1
                while temp <= flag:
                    if temp > -1:
                        answer[temp] *= 2
                    temp += 1
            elif option == '#':
                answer[flag] *= -1
            i += 1
    return sum(answer)
