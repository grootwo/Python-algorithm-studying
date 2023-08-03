# Lv.1
# [카카오 인턴] 키패드 누르기
def solution(numbers, hand):
    hand_now = {'R': '#', 'L': '*'} # 양손의 현재 위치
    nums_hand = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R', 9: 'R',
                2: None, 5: None, 8: None, 0: None} # 각 키의 해당 손
    answer = ''
    for num in numbers:
        temp = nums_hand[num]
        if temp == None: # 2, 5, 8, 0의 경우 더 가까운 손으로 클릭
            l_distance = get_distance(hand_now['L'], num)
            r_distance = get_distance(hand_now['R'], num)
            if l_distance > r_distance:
                temp = 'R'
            elif l_distance < r_distance:
                temp = 'L'
            else:
                if hand == 'right':
                    temp = 'R'
                else:
                    temp = 'L'
        hand_now[temp] = num
        answer += temp
    return answer

def get_distance(now, dest): # 현재 손의 위치에서 목적지 키의 거리를 구함
    nums_location = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                    4: [1, 0], 5: [1, 1], 6: [1, 2],
                    7: [2, 0], 8: [2, 1], 9: [2, 2],
                    '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    now_r, now_c = nums_location[now][0], nums_location[now][1]
    dest_r, dest_c = nums_location[dest][0], nums_location[dest][1]
    return abs(dest_r - now_r) + abs(dest_c - now_c)
