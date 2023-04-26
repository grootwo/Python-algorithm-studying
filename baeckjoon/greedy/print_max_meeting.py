# 1931
# 회의실 배정

case = int(input())

# 회의 시작, 종료 시간 리스트로 저장
meetings = [list(map(int, input().split())) for _ in range(case)]

# 회의 종료 시간 -> 시작 시간을 기준으로 순차적으로 정리
meetings.sort(key=lambda x:(x[1], x[0]))

# 여러 회의의 최대란,
# 종료와 동시에 가장 가까운 시간에 시작하거나
# 짧은 시간에 끝나야 함
count = 1
end_time = meetings[0][1]
for i in range(1, len(meetings)):
    if meetings[i][0] >= end_time:
        count += 1
        end_time = meetings[i][1]

print(count)


