from collections import Counter
def solution(participant, completion):
    all_runner = Counter(participant + completion)
    for runner in all_runner.keys():
        if all_runner[runner] % 2 != 0:
            return runner
