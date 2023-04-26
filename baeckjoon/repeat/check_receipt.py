# 25304
# 영수증
import sys

total_price = int(input())
num = int(input())
total_sum = 0

for i in range(num):
    price, count = map(int, sys.stdin.readline().split())
    total_sum += price * count

if total_price == total_sum:
    print("Yes")
else:
    print("No")