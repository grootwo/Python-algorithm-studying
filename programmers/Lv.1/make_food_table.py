def solution(food):
    food_for_one = 0
    for i in range(len(food)):
        food_for_one += food[i] // 2
        food[i] = food[i] - 1
    food_table = [None] * (food_for_one + 1)
    print(food_table)
    print(food)
    answer = ''
    return answer
