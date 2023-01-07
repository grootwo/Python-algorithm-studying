# 25501
# 재귀의 귀재
import sys
sys.setrecursionlimit(10 ** 6)


def recursion(string, l, r, count):
    count += 1
    if l >= r:
        return [1, count]
    if string[l] == string[r]:
        return recursion(string, l + 1, r - 1, count)
    else:
        return [0, count]


def is_palindrome(string):
    count = 0
    results = recursion(string, 0, len(string) - 1, count)
    print(results[0], results[1])


n = int(sys.stdin.readline())
strings = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in strings:
    is_palindrome(i)