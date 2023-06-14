# Lv.1
# 부족한 금액 계산하기
def solution(price, money, count):
    # 등차수열을 이용하여 총 비용 계산하기
    total_price = count * (price + price * count) // 2
    if total_price <= money:
        answer = 0
    else:
        answer = total_price - money
    return answer
