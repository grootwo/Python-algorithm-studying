def solution(new_id):
    answer = get_lower_str(new_id)
    answer = remove_not_allowed_cha(answer)
    # 3단계: 연속 . 변경
    # 4단계: 첫, 마지막 . 제거
    # 5단계: 빈 문자열 대체
    # 6단계: 문자열 15자로 인덱싱
    # 7단계: 문자열 3자 이상으로 늘리기
    return answer

def get_lower_str(string): # 1단계: 소문자 변환
    return string.lower()

def remove_not_allowed_cha(string): # 2단계: 비허용 문자 제거
    result = ''
    for cha in string:
        if cha.upper() != cha: # 소문자인지
            result += cha
        elif '0' <= cha <= '9': # 숫자인지
            result += cha
        elif cha in ['-', '_', '.']: # 해당 기호인지
            result += cha
        else:
            continue
    return result
