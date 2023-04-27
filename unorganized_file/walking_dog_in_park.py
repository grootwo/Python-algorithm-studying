def solution(park, routes):
    # define map
    row = len(park)
    col = len(park[0])
    # find start point
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                start_r = i
                start_c = j
    # move per command
    now_r = start_r
    now_c = start_c
    for i in range(len(routes)):
        ahead = routes[i][0]
        block = int(routes[i][2])
        # row = 0 col = 1
        change_check = 0
        if ahead == "E":
            next_c = now_c + block
            next_r = now_r 
            change_check = 1
        elif ahead == "W":
            next_c = now_c - block
            next_r = now_r
            change_check = 1
        elif ahead == "S":
            next_c = now_c
            next_r = now_r + block
            change_check = 0
        elif ahead == "N":
            next_c = now_c
            next_r = now_r - block
            change_check = 0
        print("-------------------")
        print("[", next_r, ",", next_c, "]")
        if next_r < 0 or row <= next_r or next_c < 0 or col <= next_c:
            print("out of range")
            continue
        loop_continue = False
        # how notice that obstacles are in load
        if change_check:
            for j in range(now_c + 1, next_c):
                if park[now_r][j] == "X":
                    print("find X in col route")
                    loop_continue = True
        else:
            for j in range(now_r + 1, next_r):
                if park[j][now_r] == "X":
                    print("find X in row route")
                    loop_continue = True
        if loop_continue is True:
            print("find X in root")
            continue
        now_c = next_c
        now_r = next_r
        print("can go")
                
    answer = [now_r, now_c]
    return answer
