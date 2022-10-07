# 16928
# 뱀과 사다리 게임

ladder_count, snake_count = map(int, input().split())

# 전개도 그리기
graph = [0] * (100)

# 사다리, 뱀(이동 조건) 저장
map_dic = {}
for i in range(ladder_count + snake_count):
    num1, num2 = map(int, input().split())
    map_dic[num1] = num2



