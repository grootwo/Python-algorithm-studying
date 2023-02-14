import math,sys
input = sys.stdin.readline

n,c = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()
start,end = 1, h[n-1] - h[0]
result = 0

if c == 2:
    print(h[n-1] - h[0])
else:
    while(start < end):
        mid = (start + end)//2

        count = 1
        ts = h[0]
        for i in range(n):
            if h[i] - ts >= mid:
                count+=1
                ts = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)