def solution(new_id):
    answer = get_lower_str(new_id)
    answer = remove_not_allowed_cha(answer)
    answer = change_continuous_dot(answer)
    answer = remove_first_last_dot(answer)
    if len(answer) == 0:
        answer = get_unblank_string(answer)
    if len(answer) > 15:
        answer = get_15_len_string(answer)
    if len(answer) < 3:
        answer = get_3_len_string(answer)
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

def change_continuous_dot(string): # 3단계: 연속 . 변경
    while '..' in string:
        string = string.replace('..', '.')
    return string

def remove_first_last_dot(string): # 4단계: 첫, 마지막 . 제거
    return string.strip('.')

def get_unblank_string(string): # 5단계: 빈 문자열 대체
    return 'a'

def get_15_len_string(string): # 6단계: 문자열 15자로 인덱싱
    if string[14] != '.':
        return string[:15]
    else:
        return string[:14]
    
def get_3_len_string(string): # 7단계: 문자열 3자 이상으로 늘리기
    return string + 'a' * (3 - len(string))
