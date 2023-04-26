# 3003
# 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

pieces = list(map(int, sys.stdin.readline().split()))
needed_pieces = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(needed_pieces[i] - pieces[i], end=' ')