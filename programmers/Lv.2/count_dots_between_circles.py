import math
def solution(r1, r2):
    count = 0
    for i in range(r2 + 1):
        for j in range(r1 + 1):
            print(i, j)
            print(math.floor(math.sqrt(i)) - math.floor(math.sqrt(j)))
    print(count)
    return count
