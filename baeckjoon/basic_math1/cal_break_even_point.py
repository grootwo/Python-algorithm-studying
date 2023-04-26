# 1712
# 손익분기점
import math

static_price, variable_price, cost = map(int, input().split())

if variable_price >= cost:
    print(-1)
else:
    # 계산식: static_price + variable_price * x >= cost * x
    tmp_BEP = static_price / (cost - variable_price)
    # 만약 정수로 딱 떨어진다면
    if tmp_BEP % 1 == 0.0:
        BEP = tmp_BEP + 1
    # 만약 소수점 아래로 수가 있다면
    else:
        BEP = math.ceil(tmp_BEP)
    print(int(BEP))

# 이전 반복문 코드
# else:
#     total_variable_price = 0
#     total_cost = 0
#     count = 0
#     while static_price + total_variable_price >= total_cost:
#         total_variable_price += variable_price
#         total_cost += cost
#         count += 1
#     print(count)