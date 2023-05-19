def solution(today, terms, privacies):
    now_y = int(today[0:4])
    now_m = int(today[5:7])
    now_d = int(today[8:10])
    # print(now_y, now_m, now_d)
    # print("----------------")
    terms_dic = {}
    for i in range(len(terms)):
        terms_dic[terms[i][0:1]] = int(terms[i][2:])
    # print(terms_dic)
    answer = []
    for i in range(len(privacies)):
        # print("---------")
        y = int(privacies[i][0:4])
        m = int(privacies[i][5:7])
        d = int(privacies[i][8:10])
        privacy = privacies[i][-1]
        temp = m + terms_dic[privacy]
        m = temp % 12
        y += temp // 12
        # print(y, m, d)
        # print(terms_dic[privacy])
        if y > now_y:
            continue
        elif y < now_y:
            answer.append(i + 1)
            # print(1)
        elif y == now_y:
            if m > now_m:
                continue
            elif m < now_m:
                answer.append(i + 1)
                # print(2)
            elif m == now_m:
                if d > now_d:
                    continue
                else:
                    answer.append(i + 1)
                    # print(3)
    return answer
