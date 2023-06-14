def solution(price, money, count):
    total_price = count * (price + price * count) // 2
    if total_price <= money:
        answer = 0
    else:
        answer = total_price - money
    return answer
