# 1300
# K번째 수

n = int(input())
find_index = int(input())

array_a = [[0] * n for _ in range(n)]
array_b = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        num = i * j
        array_a[i - 1][j - 1] = num
        array_b.append(num)
array_b.sort()

start = 0
end = n * n - 1
while start <= end:
    mid = (start + end) // 2

    if mid == find_index:
        # 왜 인덱스를 활용하지 않고 이분탐색을 이용하는 거지
    # 왜 행렬을 사용하는 거여?