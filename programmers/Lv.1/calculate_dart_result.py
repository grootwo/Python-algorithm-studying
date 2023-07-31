def solution(dartResult):
    answer = ['', '', '']
    check = -1
    for i in dartResult:
        # 정수라면
        if '0' <= i <= '9':
            check += 1
            answer[check] += i
        # 정수인지 확인
        # 정수를 count하며 1, 2, 3에 더하기
        # 정수라면 각 정답에 더하기
        # SDT에 따라 곱셈 추가
        # 옵션에 따라 마지막에 곱셈 추가
    print(answer)
    return answer
