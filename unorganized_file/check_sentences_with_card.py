def solution(cards1, cards2, goal):
    index_1 = 0
    index_2 = 0
    is_possible = True
    for word in goal:
        if index_1 < len(cards1) and cards1[index_1] == word:
            index_1 += 1
        elif index_2 < len(cards2) and cards2[index_2] == word:
            index_2 += 1
        else:
            is_possible = False
            break
    if is_possible is True:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer

# cards1 = ["i", "water", "drink"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]
# print(solution(cards1, cards2, goal))
#
# # ["i", "drink", "water"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"Yes"
# # ["i", "water", "drink"]	["want", "to"]	["i", "want", "to", "drink", "water"]	"No"