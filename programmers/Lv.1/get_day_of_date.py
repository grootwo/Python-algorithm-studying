def solution(a, b):
    days = get_days_btw(a, b)
    days_dic = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}
    answer = days_dic[days % 7]
    return answer

def get_days_btw(month, day):
    month_dic = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    result = day # 해당 달의 날 더하기
    for i in range(1, month): # 해당 달 전까지 날 더하기
        result += month_dic[i]
    result -= 1 # 1월 1일 제외
    return result
