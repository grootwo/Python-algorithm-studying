def solution(participant, completion):
    for name in participant:
        if name not in completion:
            return name
        else:
            completion.remove(name)
    return completion[0]
