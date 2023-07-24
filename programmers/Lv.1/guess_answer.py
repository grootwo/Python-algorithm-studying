def solution(answers):
    answer_dic = {'0': [1, 2, 3, 4, 5], '1': [2, 1, 2, 3, 2, 4, 2, 5], '2': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]
        print('answer: ', answer)
        print('0:', answer_dic['0'][i // 5])
        print('1:', answer_dic['1'][i // 8])
        print('2:', answer_dic['2'][i // 10])
        if answer == answer_dic['0'][i // 5]:
            scores[0] += 1
            print(0)
        if answer == answer_dic['1'][i // 8]:
            scores[1] += 1
            print(1)
        if answer == answer_dic['2'][i // 10]:
            scores[2] += 1
            print(2)
    print(scores)
    return scores
