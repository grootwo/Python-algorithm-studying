# Lv.1
# [1차] 다트 게임
def solution(dartResult):
    answer = ['', '', '']
    flag = -1
    now_i = 0
    last_i = 0
    # 점수와 추가 옵션 나눠서 저장
    while now_i < len(dartResult):
        if dartResult[now_i:now_i+2] == '10':
            flag += 1
            answer[flag] += 10
            last_i = now_i + 1
            now_i += 2
            if flag:
                answer[flag - 1].append(dartResult[last_i + 1:now_i])
        elif '0' <= dartResult[now_i] <= '9':
            flag += 1
            answer[flag] += int(dartResult[now_i])
            last_i = now_i
            now_i += 1
            if flag:
                answer[flag - 1].append(dartResult[last_i + 1:now_i])
        else:
            continue
    print(answer)
    return 0
