# 9086
# 문자열
import sys

string_count = int(input())
strings = [sys.stdin.readline().strip() for _ in range(string_count)]

for i in strings:
    print(i[0], end="")
    print(i[-1])