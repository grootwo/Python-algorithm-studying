from collections import deque
def solution(s):
    count_dic = {
        'zer': [4, '0'],
        'one': [3, '1'],
        'two': [3, '2'],
        'thr': [5, '3'],
        'fou': [4, '4'],
        'fiv': [4, '5'],
        'six': [3, '6'],
        'sev': [5, '7'],
        'eig': [5, '8'],
        'nin': [4, '9']
    }
    answer = ''
    que = deque(s)
    while que:
        if ord(que[0]) >= 97:
            temp = ''
            for i in range(3):
                temp += que[i]
            cha = count_dic[temp]
            for i in range(cha[0]):
                que.popleft()
            answer += cha[1]
        else:
            answer += que.popleft()
    answer = int(answer)
    return answer
