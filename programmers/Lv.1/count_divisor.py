def solution(left, right):
    int_list = [0] * 1000
    for i in range(1, right + 1):
        for j in range(left, right + 1):
            if j >= i and j % i == 0:
                int_list[j] += 1
    # print(int_list[left : right + 1])
    answer = 0
    for i in range(left, right + 1):
        if int_list[i] % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
