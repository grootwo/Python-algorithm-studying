# Lv.1
# 개인정보 수집 유효기간
def solution(today, terms, privacies):
    today = dateToDay(today)
    # print(today)
    terms_dic = {}
    for i in range(len(terms)):
        terms_dic[terms[i][0:1]] = int(terms[i][2:])
    answer = []
    for i in range(len(privacies)):
        privacy = privacies[i][-1]
        deadline = privacies[i][0:10]
        deadline = dateToDay(deadline) + terms_dic[privacy] * 28
        # print(privacy, deadline)
        if deadline <= today:
            answer.append(i + 1)
    return answer

def dateToDay(date):
    y, m, d = map(int, date.split("."))
    return y * 28 * 12 + m * 28 + d