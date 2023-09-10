import math
def solution(r1, r2):
    count = 0
    for i in range(r2 + 1):
        for j in range(1, r2 + 1):
            if i ** 2 + j ** 2 <= r2 ** 2:
                count += 1
    # for i in range(r2 + 1):
    #     for j in range(r1 + 1):
    #         count += math.floor(math.sqrt(abs(i ** 2 - j ** 2)))
    #         print(count)
    return count * 4
