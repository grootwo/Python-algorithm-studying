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
            print('i', i)
            print('temp', temp)
        else:
            i += 1
    print(answer)
    return 0
