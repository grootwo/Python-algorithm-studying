# Lv.1
# 옹알이 (2)
from collections import deque
def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    count = 0
    for i in range(len(babbling)):
        temp = deque(list(babbling[i]))
        flag = -1
        while temp:
            if temp[0] == "a" and len(temp) >= 3:
                if str(temp[0] + temp[1] + temp[2]) == "aya" and flag != 0:
                    for j in range(3):
                        temp.popleft()
                    flag = 0
                else:
                    flag = False
            elif temp[0] == "y" and len(temp) >= 2:
                if str(temp[0] + temp[1]) == "ye" and flag != 1:
                    for j in range(2):
                        temp.popleft()
                    flag = 1
                else:
                    flag = False
            elif temp[0] == "w" and len(temp) >= 3:
                if str(temp[0] + temp[1] + temp[2]) == "woo" and flag != 2:
                    for j in range(3):
                        temp.popleft()
                    flag = 2
                else:
                    flag = False
            elif temp[0] == "m" and len(temp) >= 2:
                if str(temp[0] + temp[1]) == "ma" and flag != 3:
                    for j in range(2):
                        temp.popleft()
                    flag = 3
                else:
                    flag = False
            else:
                 flag = False
            if flag is False:
                break
        if len(temp) == 0:
            count += 1
    answer = count
    return answer
