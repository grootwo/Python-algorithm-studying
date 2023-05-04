# Lv.1
def solution(players, callings):
    for i in range(len(callings)):
        faster = callings[i]
        faster_i = players.index(faster)
        later = players[faster_i - 1]
        players[faster_i - 1] = faster
        players[faster_i] = later
    answer = players
    return answer
