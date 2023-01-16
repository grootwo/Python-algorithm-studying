# 1654
# 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]

# 케이블을 정렬한다
cables.sort()

# 가장 작은 케이블을 선택한다
min_cable = cables[0]

# 이분 탐색으로 적절한 cm를 찾는다
def find_max_cable():
    # print("--------")
    # print("find")
    # 첫 가능
    temp = binary_search(1, min_cable)
    # print("temp:", temp)
    for i in range(temp + 1, min_cable):
        if is_adequate_cable(i) == -1:
            return i - 1


# cm가 조건을 만족하면서 최대인지 확인하는 함수
def is_adequate_cable(cm):
    # print("--------")
    # print("adequate")
    global n
    count = 0
    for i in cables:
        count += i // cm
    if count == n:
        # print("0")
        return 0
    elif count > n: # 케이블이 최대보다 짧다면
        # print("1")
        return 1
    elif count < n: # 케이블이 최대보다 길다면
        # print("-1")
        return -1


def binary_search(start, end):
    # print("--------")
    # print("binary")
    mid = (end + start) // 2
    if is_adequate_cable(mid) == 0:
        # print("mid:", mid)
        return mid
    elif is_adequate_cable(mid) == 1:
        return binary_search(mid + 1, end)
    elif is_adequate_cable(mid) == -1:
        return binary_search(start, mid - 1)


print(find_max_cable())