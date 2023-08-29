# Lv.1
# 완주하지 못한 선수
from collections import Counter
def solution(participant, completion):
    all_runner = Counter(participant + completion)
    for runner in all_runner.keys():
        if all_runner[runner] % 2 != 0:
            return runner
