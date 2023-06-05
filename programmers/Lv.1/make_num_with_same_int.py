def solution(X, Y):
    same_int = []
    X = list(X)
    Y = list(Y)
    for i in X:
        if i in Y:
            same_int.append(i)
            Y.remove(i)
    if same_int:
        same_int.sort()
        same_int.reverse()
        if same_int[0] == "0":
            answer = "0"
        else:
            answer = ''.join(same_int)
    else:
        answer = "-1"
    return answer
