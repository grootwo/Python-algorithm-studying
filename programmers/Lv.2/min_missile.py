def solution(targets):
    count = 0
    while targets:
        print('---------')
        max_location = get_max_location(targets)
        print('max_location:', max_location)
        print('targets:', targets)
        for target in targets:
            print('- target:', target)
            if include_location(max_location, target):
                print('delete target:', target)
                targets.remove(target)
        count += 1
        print('count:', count)
        print(targets)
    return count

def get_max_location(locations):
    locations.sort(key=lambda x: -x[1])
    location_list = [0] * locations[0][1]
    for location in locations:
        for i in range(location[0], location[1]):
            location_list[i] += 1
    return location_list.index(max(location_list))

def include_location(x, location):
    print('include_location')
    if location[0] <= x and x < location[1]:
        print('True')
        return True
    print('False')
    return False
