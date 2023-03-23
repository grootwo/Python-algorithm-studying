# 12865
# 평범한 배낭
import sys

things = []
things_count, max_kg = map(int, sys.stdin.readline().split())
for i in range(things_count):
    kg, value = map(int, sys.stdin.readline().split())
    things.append([kg, value])

def get_max_value():
    sum_value = 0
    sum_kg = 0
    for i in range(len(things)):
        if sum_kg == max_kg:
            break
        if sum_kg + things[i][0] <= max_kg:
            # print("add kg:", things[i][0], "add value:", things[i][1])
            sum_kg += things[i][0]
            sum_value += things[i][1]
            # print("sum_value:", sum_value)
    return sum_value


# value 기준 정렬
things.sort(key=lambda x: (-x[1], x[0]))
# print(things)
max_value_value = get_max_value()
# print(max_value_value)

# kg 기준 정렬
things.sort(key=lambda x: (x[0], -x[1]))
# print(things)
max_value_kg = get_max_value()
# print(max_value_kg)


if max_value_value >= max_value_kg:
    print(max_value_value)
else:
    print(max_value_kg)