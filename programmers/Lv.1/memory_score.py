# 추억 점수
# Lv.1

def solution(name, yearning, photo):
    # 사람별 추억 지수 사전에 저장
    per_dic = {}
    for i in range(len(name)):
        per_dic[name[i]] = yearning[i] 
    # 사진마다 추억 점수 매기기
    total_count = []
    for a_photo in photo:
        count = 0
        for person in a_photo:
            if per_dic.get(person):
                count += per_dic.get(person)
        total_count.append(count)
    answer = total_count
    return answer
