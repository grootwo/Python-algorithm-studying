# 1931
# 회의실 배정

case = int(input())

# 회의 시작, 종료 시간 리스트로 저장
meetings = [list(map(int, input().split())) for _ in range(case)]

# 여러 회의의 최대란,
# 종료와 동시에 가장 가까운 시간에 시작하거나
# 짧은 시간에 끝나야 함


