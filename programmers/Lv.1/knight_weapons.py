def solution(number, limit, power):
    answer = [0] * number
    for i in range(1, number + 1):
        for num in range(1, number + 1):
            if num % i == 0:
                answer[num - 1] += 1
    for i in range(number):
        if answer[i] > limit:
            answer[i] = power
    # print(answer)
    return sum(answer)