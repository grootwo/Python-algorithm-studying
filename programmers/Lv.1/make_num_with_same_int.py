from collections import Counter
def solution(X, Y):
    same_num = []
    X = Counter(X)
    Y = Counter(Y)
    print(X)
    print(Y)
    for num in X:
        if num in Y:
            if X[num] > Y[num]:
                same_num.append([num, Y[num]])
            else:
                same_num.append([num, X[num]])
    print(same_num)
    # same_num.sort(key=lambda x: (-x[0]))
    # print(same_num)
    answer = ''
    return answer
