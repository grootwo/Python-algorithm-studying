# Lv.1
# 푸드 파이트 대회
def solution(food):
    # 한 명이 먹을 음식 양으로 정리하기
    for i in range(len(food)):
        food[i] = food[i] // 2
    # 좌측부터 순서대로 테이블 정렬하기
    food_table = []
    for i in range(1, len(food)):
        for j in range(food[i]):
            food_table.append(i)
    # 물 배치하기
    food_table.append(0)
    # 우측 테이블 정렬하기
    food.reverse()
    for i in range(len(food)):
        for j in range(food[i]):
            food_table.append(len(food) - 1 - i)
    food_table = list(map(str, food_table))
    answer = ''.join(food_table)
    return answer
