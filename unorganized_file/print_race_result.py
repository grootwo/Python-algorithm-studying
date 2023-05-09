# Lv.1
# 달리기 경주

def solution(players, callings):
    from collections import deque
    temp = callings[0]
    count = 1
    commands = []
    for i in range(1, len(callings)):
        if callings[i] == temp:
            count += 1
        else:
            commands.append([temp, count])
            count = 1
            temp = callings[i]
    commands.append([temp, count])
    # print(commands)
    que = deque(players)
    for i in range(len(commands)):
        faster = commands[i][0]
        count = commands[i][1]
        current_i = que.index(faster)
        que.remove(faster)
        que.insert(current_i - count, faster)
        # print(que)
    answer = list(que)
    return answer
