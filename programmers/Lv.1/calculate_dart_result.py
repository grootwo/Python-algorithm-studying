# Lv.1
# [1차] 다트 게임
def solution(dartResult):
    answer = ['', '', '']
    check = -1
    for i in dartResult:
        sqr_dic = {'S': '**1', 'D': '**2', 'T': '**3'}
        # 정수라면
        if '0' <= i <= '9':
            check += 1
            answer[check] += i
        elif i == 'S' or 'D' or 'T':
            answer[check] += sqr_dic[i]
        else:
            if i == '#':
                answer[check] += '*-1'
            elif i == '*' and check > 0:
                answer[check] += '*2'
                answer[check - 1] += '*2'
            else:
                answer[check] += '*2'
        # 정수인지 확인
        # 정수를 count하며 1, 2, 3에 더하기
        # 정수라면 각 정답에 더하기
        # SDT에 따라 곱셈 추가
        # 옵션에 따라 마지막에 곱셈 추가
    print(answer)
    return answer
