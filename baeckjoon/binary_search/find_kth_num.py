# 1300
# K번째 수
# ref(https://hongcoding.tistory.com/13)

n = int(input())
find_index = int(input())


def binary_search(target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid // i, n)

        if cnt >= target:
            end = mid-1
        else:
            start = mid+1
    return start


print(binary_search(find_index, 1, n * n))