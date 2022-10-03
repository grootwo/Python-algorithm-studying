# 1697
# 숨바꼭질

now, end = map(int, input().split())

count = 0

def go(start, end):
    global count
    if start == end:
        return count
    start += 1
    start -= 1
    start *= 2
    count += 1

print(count)