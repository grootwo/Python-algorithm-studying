# Lv.2
# 광물 캐기

def solution(picks, minerals):
    # 도구로 캘 수 있는 만큼만 인덱싱
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    # 각 광물을 5단위로 개수 정리
    minerals_count = []
    for i in range(0, len(minerals) // 5):
        minerals_tmp = minerals[i*5:i*5+5]
        dia_count = minerals_tmp.count("diamond")
        iron_count = minerals_tmp.count("iron")
        stone_count = minerals_tmp.count("stone")
        minerals_count.append([dia_count, iron_count, stone_count])
    if len(minerals) % 5 != 0:
        minerals_tmp = minerals[-(len(minerals) % 5) : len(minerals)]
        # print("last", minerals_tmp)
        dia_count = minerals_tmp.count("diamond")
        iron_count = minerals_tmp.count("iron")
        stone_count = minerals_tmp.count("stone")
        minerals_count.append([dia_count, iron_count, stone_count])
    # 다이아몬드, 철, 돌이 많은 순서대로 정렬
    minerals_count.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    # print(minerals_count)
    # 피로도 계산
    total_stress = 0
    for tmp in minerals_count:
        if picks[0] > 0:
            picks[0] -= 1
            total_stress += (tmp[0] + tmp[1] + tmp[2])
        elif picks[1] > 0:
            picks[1] -= 1
            total_stress += (tmp[0] * 5 + tmp[1] + tmp[2])
        elif picks[2] > 0:
            picks[2] -= 1
            total_stress += (tmp[0] * 25 + tmp[1] * 5 + tmp[2])
    # print('total stress: ', total_stress)
    answer = total_stress
    return answer
