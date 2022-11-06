# 1712
# 손익분기점

static_price, variable_price, cost = map(int, input().split())
#
# if variable_price >= cost:
#     print(-1)
# else:
#     total_variable_price = 0
#     total_cost = 0
#     count = 0
#     while static_price + total_variable_price >= total_cost:
#         total_variable_price += variable_price
#         total_cost += cost
#         count += 1
#     print(count)

# static_price + variable_price* >= cost*
# 이 *를 찾아야 함
# static_price / (cost - variable_price) =< *

