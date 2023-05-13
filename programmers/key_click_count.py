# Lv.1
# 대충 만든 자판

def solution(keymap, targets):
    min_key_dic = {}
    # 각 글자다마 최소 클릭 횟수 계산 및 저장
    for key in keymap:
        for cha in key:
            if cha in min_key_dic:
                if key.index(cha) < min_key_dic[cha]:
                    min_key_dic[cha] = key.index(cha) + 1
                else:
                    continue
            else:
                min_key_dic[cha] = key.index(cha) + 1
    # print(min_key_dic)
    total_count = []
    # 각 target마다 총 클릭 횟수 계산
    for target in targets:
        count = 0
        for cha in target:
            if cha in min_key_dic:
                count += min_key_dic[cha]
            else: # 만약 만들 수 없는 글자라면
                count = -1
                break
        total_count.append(count)
    answer = total_count
    return answer