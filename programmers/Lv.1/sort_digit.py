# Lv.1
# 정수 내림차순으로 배치하기
def solution(n):
    nums = sorted(list(str(n)), reverse = True)
    return int(''.join(nums))
