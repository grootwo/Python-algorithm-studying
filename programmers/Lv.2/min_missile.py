def solution(targets):
    count = 0
    while targets:
        # print('---------')
        max_location = get_max_location(targets)
        # print('max_location:', max_location)
        # print('targets:', targets)
        for i in range(len(targets)):
            # print('- target:', targets[i])
            if include_location(max_location, targets[i]):
                # print('delete target:', targets[i])
                targets[i][0] = 0
                targets[i][1] = 0
        targets = delete_targets(targets)
        count += 1
        # print('count:', count)
        # print(targets)
    return count

def get_max_location(locations):
    locations.sort(key=lambda x: -x[1])
    location_list = [0] * locations[0][1]
    for location in locations:
        for i in range(location[0], location[1]):
            location_list[i] += 1
    return location_list.index(max(location_list))

def include_location(x, location):
    # print('include_location')
    if location[0] <= x and x < location[1]:
        # print('True')
        return True
    # print('False')
    return False

def delete_targets(targets):
    count = 0
    for i in range(len(targets)):
        if targets[i][0] == 0:
            count += 1
    for i in range(count):
        targets.remove([0, 0])
    return targets
    
