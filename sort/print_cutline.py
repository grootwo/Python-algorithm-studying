# 25305
# 커트라인

std_count, limit = map(int, input().split())
std_record = list(map(int, input().split()))

std_record.sort()
std_record.reverse()

print(std_record[limit - 1])