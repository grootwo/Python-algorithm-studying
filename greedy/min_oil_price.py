# 13305
# 주유소

# 제일 끝 도시의 주유 가격은 필요없음
# 만약 가장 싼 가격의 주유소에 도달하면 나머지 거리만큼 다 사야함
# 비싼 주유소라면 다음 도시로 넘어갈 수 있을 만큼 사야함
# 현재 주유소 < 다음 주유소 이거 반복문으로 자기보다 싼 주유소 나오기 전까지 거리만큼 기름 사야 함

import sys

n = int(input())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

# 현재 위치
min_price = prices[0]
price = 0

# 현재 주유소보다 싼 주유소에 닿기 전까지의 거리만큼 기름 구매
for i in range(1, n):
    if min_price > prices[i]:
        price += min_price * distances[i - 1]
        min_price = prices[i]
    else:
        price += min_price * distances[i - 1]

print(price)