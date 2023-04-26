# 2805
# 나무 자르기
import sys

tree_count, need = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)


def availableTree(num):
    count = 0
    for i in trees:
        if i > num:
            count += (i - num)
    if count >= need:
        return 1
    else:
        return 0

while start <= end:
    mid = (start + end) // 2

    if availableTree(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)