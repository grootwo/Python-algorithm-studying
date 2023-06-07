# Lv.1
# 성격 유형 검사하기
def solution(survey, choices):
    score_dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(choices)):
        choice = choices[i]
        survey_type = survey[i]
        if choice >= 5:
            score_dic[survey_type[1]] += choice - 4
        elif choice <= 3:
            score_dic[survey_type[0]] += 4 - choice
    result = ''
    if score_dic['R'] >= score_dic['T']:
        result += 'R'
    else:
        result += 'T'
    if score_dic['C'] >= score_dic['F']:
        result += 'C'
    else:
        result += 'F'
    if score_dic['J'] >= score_dic['M']:
        result += 'J'
    else:
        result += 'M'
    if score_dic['A'] >= score_dic['N']:
        result += 'A'
    else:
        result += 'N'
    return result
