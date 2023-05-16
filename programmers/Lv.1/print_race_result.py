# Lv.1
# 달리기 경주

def solution(players, callings):
    players_dic = {} # key: 선수, value: 등수
    scores_dic = {} # key: 등수, value: 선수
    for i in range(len(players)):
        players_dic[players[i]] = i
        scores_dic[i] = players[i]
    # print(players_dic)
    # print(scores_dic)
    for calling in callings:
        now = players_dic[calling]
        # 순위에 따른 선수 수정
        scores_dic[now] = scores_dic[now - 1]
        scores_dic[now - 1] = calling
        # 선수의 등수 수정
        players_dic[calling] -= 1
        players_dic[scores_dic[now]] += 1
        # print(players_dic)
        # print(scores_dic)
    answer = list(scores_dic.values())
    return answer