# Lv.1
# 가장 가까운 같은 글자
def solution(s):
    last_location_dic = {}
    answer = []
    for i in range(len(s)):
        cha = s[i]
        if cha not in last_location_dic:
            last_location_dic[cha] = i
            answer.append(-1)
        else:
            answer.append(i - last_location_dic[cha])
            last_location_dic[cha] = i
    return answer
