# Lv.1
# 바탕화면 정리
def solution(wallpaper):
    cols = []
    rows = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                cols.append(j)
                rows.append(i)
    answer = [min(rows), min(cols), max(rows) + 1, max(cols) + 1]
    return answer
