def solution(park, routes):
    # define map
    row = len(park)
    col = len(park[0])
    # find start point
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                now_r = i
                now_c = j
    # move per command
    ahead_i = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(len(routes)):
        print("-------------------")
        next_r = now_r
        next_c = now_c
        ahead = routes[i][0]
        block = int(routes[i][2])
        check = 0
        if ahead == "E":
            go = ahead_i[0]
        elif ahead == "W":
            go = ahead_i[1]
        elif ahead == "S":
            go = ahead_i[2]
        elif ahead == "N":
            go = ahead_i[3]
        for j in range(block):
            next_r += go[0]
            next_c += go[1]
            # check
            print("now: ", now_r, now_c)
            print("next: ", next_r, next_c)
            if next_r < 0 or row <= next_r or next_c < 0 or col <= next_c or park[next_r][next_c] == "X":
                print("can't go")
                check = 1
                break
                
        if check == 1:
            continue
        else:
            now_r = next_r
            now_c = next_c
                
    answer = [now_r, now_c]
    return answer
