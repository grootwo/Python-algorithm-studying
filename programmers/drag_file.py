# 바탕화면 정리
def solution(wallpaper):
    row = len(wallpaper)
    col = len(wallpaper[0])
    min_r = row
    min_c = col
    max_r = 0
    max_c = 0
    flag = False
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == "#":
                if i < min_r:
                    min_r = i
                if j < min_c:
                    min_c = j
                if i > max_r:
                    max_r = i
                if j > max_c:
                    max_c = j
    # print(min_r, min_c, max_r, max_c)
    answer = [min_r, min_c, max_r + 1, max_c + 1]
    return answer
