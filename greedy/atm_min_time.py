# 11399소
# ATM

n = int(input())
times = list(map(int, input().split()))
count = 0

times.sort()

for i in range(n):
    count += times[i] * (n - i)

print(count)